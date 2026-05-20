"""
Test enrich with first 10 questions to validate quality before full run.
Uses google.genai (new SDK).
"""
import json
import os
import re
import sys
from google import genai
from google.genai import types

INPUT_FILE = 'scripts/output/parsed_questions.json'
OUTPUT_FILE = 'scripts/output/test_enriched_10.json'

PROMPT_HEADER = """
Bạn là chuyên gia Salesforce PD1 (Platform Developer 1). Nhiệm vụ của bạn là làm phong phú thêm các câu hỏi trắc nghiệm sau đây.

Với MỖI câu hỏi, hãy tạo ra các nội dung sau (bằng tiếng Việt):
1. "vi_question": Dịch câu hỏi sang tiếng Việt (GIỮ NGUYÊN thuật ngữ kỹ thuật như Apex, SOQL, LWC, DML, trigger, governor limit, metadata API, Process Builder, Flow, Workflow, Visualforce, v.v.)
2. "why_correct": Giải thích ngắn gọn (2-4 câu) TẠI SAO đáp án đúng là đúng
3. "why_wrong": Object với key là chữ cái của TỪNG đáp án sai, value là giải thích TẠI SAO đáp án đó sai (1-2 câu)
4. "tip": Từ khóa/gợi nhớ cực ngắn (1 câu, max 25 từ) để nhớ ngay câu này khi thi

QUY TẮC BẮT BUỘC:
- Giữ nguyên thuật ngữ Salesforce/Apex/code tiếng Anh (KHÔNG dịch: Apex, SOQL, SOSL, DML, trigger, Flow, LWC, Aura, Visualforce, @InvocableMethod, insert, update, delete, etc.)
- vi_question phải tự nhiên, dễ hiểu
- tip phải ngắn, sắc bén, dễ nhớ

Trả về JSON array với format CHÍNH XÁC như sau (chỉ JSON thuần, không có markdown, không có text thêm):
[
  {
    "id": <số id>,
    "vi_question": "...",
    "why_correct": "...",
    "why_wrong": {"A": "lý do A sai", "B": "lý do B sai"},
    "tip": "..."
  }
]

DANH SÁCH CÂU HỎI:
"""

def format_q(q):
    opts = q.get('options', [])
    correct = q.get('correct', [])
    wrong_keys = [o['key'] for o in opts if o['key'] not in correct]
    
    opt_lines = ''
    for o in opts:
        mark = '[CORRECT]' if o['key'] in correct else '[WRONG]'
        opt_lines += f"  {o['key']}. {o['text']} {mark}\n"
    
    explanation = (q.get('explanation_en') or '')[:400]
    
    return (
        f"ID: {q['id']}\n"
        f"Question: {q['question']}\n"
        f"Options:\n{opt_lines}"
        f"Correct: {', '.join(correct)} | Wrong: {', '.join(wrong_keys)}\n"
        f"English Explanation: {explanation}\n"
    )

def main():
    api_key = os.environ.get('GEMINI_API_KEY')
    if not api_key:
        print("ERROR: Set GEMINI_API_KEY environment variable first")
        sys.exit(1)

    client = genai.Client(api_key=api_key)

    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        all_questions = json.load(f)

    # Test with first 10
    test_batch = all_questions[:10]

    sep = '\n' + '=' * 40 + '\n'
    questions_text = sep.join(format_q(q) for q in test_batch)
    prompt = PROMPT_HEADER + '\n' + sep + questions_text

    print(f"Sending {len(test_batch)} questions to Gemini...")
    print(f"Prompt length: {len(prompt)} chars\n")

    # Try models in order of preference
    MODELS = [
        'gemini-2.0-flash-lite',
        'gemini-1.5-flash',
        'gemini-1.5-flash-8b',
        'gemini-2.0-flash',
    ]
    response = None
    for model_name in MODELS:
        try:
            print(f"Trying model: {model_name}")
            response = client.models.generate_content(
                model=model_name,
                contents=prompt,
                config=types.GenerateContentConfig(
                    temperature=0.3,
                    max_output_tokens=8192,
                )
            )
            print(f"Success with: {model_name}")
            break
        except Exception as e:
            print(f"  {model_name} failed: {str(e)[:120]}")
            continue
    if response is None:
        print("All models failed. Check quota/billing.")
        sys.exit(1)

    text = response.text.strip()
    # Strip markdown code fences if present
    text = re.sub(r'^```(?:json)?\s*', '', text)
    text = re.sub(r'\s*```$', '', text)
    text = text.strip()

    results = json.loads(text)
    print(f"Got {len(results)} enriched questions\n")

    # Show first result
    r = results[0]
    print('--- Sample Result (Q1) ---')
    print(f"vi_question:\n  {r['vi_question']}\n")
    print(f"why_correct:\n  {r['why_correct']}\n")
    print(f"why_wrong:")
    for k, v in r['why_wrong'].items():
        print(f"  {k}: {v}")
    print(f"\ntip:\n  {r['tip']}\n")

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print(f"Saved test results to {OUTPUT_FILE}")

if __name__ == '__main__':
    main()
