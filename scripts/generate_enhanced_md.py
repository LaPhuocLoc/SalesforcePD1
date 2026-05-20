"""
Convert enriched questions JSON back to a beautiful Markdown file.
This generates the final enhanced MD with Vietnamese translations, why correct/wrong, and tips.
"""
import json
import os
from pathlib import Path

INPUT_FILE = 'scripts/output/enriched_questions.json'
OUTPUT_MD = 'docs/SF Developer 1_All_Question_ENHANCED.md'

def generate_md(questions):
    lines = []
    lines.append('# Salesforce PD1 - Bộ Đề Nâng Cấp')
    lines.append('')
    lines.append('> Đã bổ sung: Dịch tiếng Việt • Phân tích đáp án đúng/sai • Từ khóa ghi nhớ')
    lines.append('')
    lines.append('---')
    lines.append('')
    
    for i, q in enumerate(questions):
        q_num = i + 1
        lines.append(f'## Câu {q_num}')
        lines.append('')
        
        # English question
        lines.append(f'**🔵 {q["question"]}**')
        lines.append('')
        
        # Options
        opts = q.get('options', [])
        correct = q.get('correct', [])
        
        for opt in opts:
            key = opt['key']
            text = opt['text']
            is_correct = key in correct
            marker = '✅' if is_correct else '❌'
            lines.append(f'- **{key}.** {text} {marker}')
        
        lines.append('')
        
        # Vietnamese question
        explanation = q.get('explanation', {})
        vi_q = explanation.get('vi_question', '')
        why_correct = explanation.get('why_correct', '')
        why_wrong = explanation.get('why_wrong', {})
        tip = explanation.get('tip', '')
        explanation_en = q.get('explanation_en', '')
        
        if vi_q:
            lines.append(f'**📝 Dịch tiếng Việt:**')
            lines.append(f'> {vi_q}')
            lines.append('')
        
        # Original English explanation
        if explanation_en:
            lines.append(f'**💬 Giải thích gốc (English):**')
            for eline in explanation_en.strip().split('\n'):
                if eline.strip():
                    lines.append(f'> {eline.strip()}')
            lines.append('')
        
        # Why correct
        if why_correct:
            lines.append('**✅ Tại sao đáp án đúng:**')
            lines.append(f'> {why_correct}')
            lines.append('')
        
        # Why wrong
        if why_wrong:
            lines.append('**❌ Tại sao đáp án sai:**')
            for key, reason in why_wrong.items():
                lines.append(f'> **{key}.** {reason}')
            lines.append('')
        
        # Tip
        if tip:
            lines.append(f'**💡 Từ khóa ghi nhớ:** `{tip}`')
            lines.append('')
        
        lines.append('---')
        lines.append('')
    
    return '\n'.join(lines)

def main():
    if not os.path.exists(INPUT_FILE):
        print(f"ERROR: {INPUT_FILE} not found. Run enrich_questions.py first.")
        return
    
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        questions = json.load(f)
    
    print(f"Loaded {len(questions)} enriched questions")
    
    md_content = generate_md(questions)
    
    with open(OUTPUT_MD, 'w', encoding='utf-8') as f:
        f.write(md_content)
    
    print(f"Generated enhanced MD: {OUTPUT_MD}")
    print(f"File size: {os.path.getsize(OUTPUT_MD) / 1024:.1f} KB")

if __name__ == '__main__':
    main()
