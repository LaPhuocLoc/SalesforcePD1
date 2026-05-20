import json

with open('scripts/output/enriched_questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

empty_ids = [36, 40, 72, 74, 165, 168, 231, 236, 240, 290, 343]

output = []
for q in questions:
    if q['id'] in empty_ids:
        output.append("="*60)
        output.append(f"ID: {q['id']} | Num: {q.get('original_num')}")
        output.append(f"Question text:\n{q['question']}")
        ex = q.get('explanation', {})
        output.append(f"Explanation why_correct: {ex.get('why_correct')}")
        output.append(f"Explanation why_wrong keys: {list(ex.get('why_wrong', {}).keys())}")
        for k, v in ex.get('why_wrong', {}).items():
            output.append(f"  {k}: {v}")

with open('scripts/output/inspect_empty_output.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(output))
print("Wrote inspect empty output successfully.")
