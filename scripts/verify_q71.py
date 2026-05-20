import json

with open('src/data/questions_enhanced.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

for q in questions:
    if q['id'] == 71:
        ex = q.get('explanation', {})
        out = []
        out.append(f"ID: {q['id']} | Correct: {q['correct']}")
        out.append(f"Question: {q['question']}")
        out.append("Options:")
        for opt in q['options']:
            out.append(f"  {opt['key']}: {opt['text']}")
        out.append(f"why_correct: {ex.get('why_correct')}")
        out.append("why_wrong:")
        for k, v in ex.get('why_wrong', {}).items():
            out.append(f"  {k}: {v}")
        
        with open('scripts/output/verify_q71.txt', 'w', encoding='utf-8') as f:
            f.write('\n'.join(out))
        print("Done")
