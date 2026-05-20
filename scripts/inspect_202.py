import json

with open('scripts/output/enriched_questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

output = []
for q in questions:
    if q['id'] == 202:
        output.append("="*60)
        output.append(f"ID: {q['id']} | Num: {q.get('original_num')}")
        output.append(f"Question: {q['question']}")
        output.append("Options:")
        for opt in q['options']:
            output.append(f"  {opt['key']}: {opt['text']}")
        output.append(f"Correct: {q['correct']}")
        ex = q.get('explanation', {})
        output.append("Explanation:")
        output.append(f"  why_correct: {ex.get('why_correct')}")
        output.append(f"  why_wrong keys: {list(ex.get('why_wrong', {}).keys())}")
        for k, v in ex.get('why_wrong', {}).items():
            output.append(f"    {k}: {v}")

with open('scripts/output/inspect_202.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(output))
print("Wrote inspect 202 output successfully.")
