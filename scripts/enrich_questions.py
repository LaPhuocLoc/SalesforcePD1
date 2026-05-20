"""
Enrich SF PD1 questions with Vietnamese translations, why_correct, why_wrong, and tip.
Uses Google Gemini API to generate content for all 349 questions from the MD file.

Usage:
    set GEMINI_API_KEY=your_key_here
    python scripts/enrich_questions.py

Checkpointing: saves progress every batch, so can resume if interrupted.
"""
import json
import os
import time
import re
import sys
from pathlib import Path

# --- CONFIG ---
INPUT_FILE = 'scripts/output/parsed_questions.json'
CHECKPOINT_FILE = 'scripts/output/enrichment_checkpoint.json'
OUTPUT_FILE = 'scripts/output/enriched_questions.json'
BATCH_SIZE = 5   # questions per API call
SLEEP_BETWEEN_BATCHES = 2  # seconds

PROMPT_TEMPLATE = """
Bạn là chuyên gia Salesforce PD1 (Platform Developer 1). Nhiệm vụ của bạn là làm phong phú thêm các câu hỏi trắc nghiệm sau đây.

Với MỖI câu hỏi, hãy tạo ra các nội dung sau (bằng tiếng Việt):
1. "vi_question": Dịch câu hỏi sang tiếng Việt (GIỮ NGUYÊN thuật ngữ kỹ thuật, tên nút, tên method, keyword như Apex, SOQL, LWC, DML, trigger, governor limit, v.v.)
2. "why_correct": Giải thích ngắn gọn (2-4 câu) TẠI SAO đáp án đúng là đúng
3. "why_wrong": Object với key là chữ cái của đáp án sai, value là giải thích tại sao ĐÁP ÁN ĐÓ SAI (1-2 câu mỗi cái)
4. "tip": Keyword/gợi nhớ cực ngắn (1 câu, max 20 từ) để nhớ câu này lần sau không chọn sai

QUY TẮC BẮT BUỘC:
- Giữ nguyên thuật ngữ Salesforce/Apex/code tiếng Anh (không dịch: Apex, SOQL, SOSL, DML, trigger, flow, LWC, Aura, Visualforce, apex:page, @InvocableMethod, v.v.)
- Giữ nguyên tên object/field/method (Account, Contact, Opportunity, insert, update, etc.)
- vi_question phải là bản dịch tự nhiên, không robot
- tip phải ngắn gọn, dễ nhớ, có thể dùng ví dụ vui

Trả về JSON array với format:
[
  {
    "id": <id câu hỏi>,
    "vi_question": "...",
    "why_correct": "...",
    "why_wrong": {"A": "...", "B": "..."},
    "tip": "..."
  },
  ...
]

Chỉ trả về JSON, không có text thêm, không có markdown code block.

Đây là danh sách câu hỏi cần xử lý:
{questions_json}
"""

def load_checkpoint():
    if os.path.exists(CHECKPOINT_FILE):
        with open(CHECKPOINT_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_checkpoint(data):
    with open(CHECKPOINT_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def format_question_for_prompt(q):
    """Format a question into a compact representation for the prompt."""
    opts = q.get('options', [])
    correct = q.get('correct', [])
    wrong = [o['key'] for o in opts if o['key'] not in correct]
    
    opt_text = ''
    for o in opts:
        mark = '[CORRECT]' if o['key'] in correct else '[WRONG]'
        opt_text += f"  {o['key']}. {o['text']} {mark}\n"
    
    explanation = q.get('explanation_en', '')
    
    result = f"""ID: {q['id']}
Câu hỏi: {q['question']}
Đáp án:
{opt_text}Đáp án đúng: {', '.join(correct)}
Đáp án sai: {', '.join(wrong)}
Giải thích tiếng Anh (nếu có): {explanation[:500] if explanation else 'Không có'}
"""
    return result

def call_gemini(questions_batch, api_key):
    """Call Gemini API to enrich a batch of questions."""
    import google.generativeai as genai
    
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.0-flash')
    
    # Build questions JSON for prompt
    questions_text = ''
    for i, q in enumerate(questions_batch):
        questions_text += f'\n=== Câu {i+1} ===\n'
        questions_text += format_question_for_prompt(q)
    
    prompt = PROMPT_TEMPLATE.format(questions_json=questions_text)
    
    response = model.generate_content(
        prompt,
        generation_config={
            'temperature': 0.3,
            'max_output_tokens': 8192,
        }
    )
    
    text = response.text.strip()
    
    # Clean up JSON if wrapped in code block
    text = re.sub(r'^```(?:json)?\n?', '', text)
    text = re.sub(r'\n?```$', '', text)
    text = text.strip()
    
    return json.loads(text)

def main():
    api_key = os.environ.get('GEMINI_API_KEY')
    if not api_key:
        print("ERROR: GEMINI_API_KEY not set!")
        print("Run: set GEMINI_API_KEY=your_key_here")
        sys.exit(1)
    
    # Load parsed questions
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        questions = json.load(f)
    
    print(f"Loaded {len(questions)} questions from {INPUT_FILE}")
    
    # Load checkpoint
    checkpoint = load_checkpoint()
    print(f"Checkpoint has {len(checkpoint)} enriched questions")
    
    # Find questions not yet enriched
    to_process = [q for q in questions if str(q['id']) not in checkpoint]
    print(f"Questions to process: {len(to_process)}")
    
    if not to_process:
        print("All questions already enriched!")
    else:
        # Process in batches
        total_batches = (len(to_process) + BATCH_SIZE - 1) // BATCH_SIZE
        
        for batch_num in range(total_batches):
            batch_start = batch_num * BATCH_SIZE
            batch_end = min(batch_start + BATCH_SIZE, len(to_process))
            batch = to_process[batch_start:batch_end]
            
            print(f"\nBatch {batch_num + 1}/{total_batches}: Questions {batch[0]['id']} - {batch[-1]['id']}")
            
            max_retries = 3
            for attempt in range(max_retries):
                try:
                    results = call_gemini(batch, api_key)
                    
                    # Save to checkpoint
                    for r in results:
                        checkpoint[str(r['id'])] = r
                    
                    save_checkpoint(checkpoint)
                    print(f"  ✓ Enriched {len(results)} questions. Total: {len(checkpoint)}")
                    break
                    
                except json.JSONDecodeError as e:
                    print(f"  ✗ JSON parse error (attempt {attempt+1}): {e}")
                    if attempt < max_retries - 1:
                        time.sleep(5)
                except Exception as e:
                    print(f"  ✗ API error (attempt {attempt+1}): {e}")
                    if attempt < max_retries - 1:
                        time.sleep(10)
            
            if batch_num < total_batches - 1:
                time.sleep(SLEEP_BETWEEN_BATCHES)
    
    # Merge checkpoint into questions
    print("\nMerging enrichment data into questions...")
    
    enriched_count = 0
    for q in questions:
        key = str(q['id'])
        if key in checkpoint:
            enrichment = checkpoint[key]
            q['explanation'] = {
                'vi_question': enrichment.get('vi_question', ''),
                'why_correct': enrichment.get('why_correct', ''),
                'why_wrong': enrichment.get('why_wrong', {}),
                'tip': enrichment.get('tip', '')
            }
            enriched_count += 1
    
    # Save final output
    Path('scripts/output').mkdir(exist_ok=True)
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)
    
    print(f"\n✓ Done! {enriched_count}/{len(questions)} questions enriched.")
    print(f"Output saved to: {OUTPUT_FILE}")
    
    # Stats
    missing = [q for q in questions if not q.get('explanation', {}).get('vi_question')]
    if missing:
        print(f"\nWARNING: {len(missing)} questions still missing enrichment:")
        for q in missing[:10]:
            print(f"  ID {q['id']}: {q['question'][:80]}...")

if __name__ == '__main__':
    main()
