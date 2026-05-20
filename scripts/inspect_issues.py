import json
import sys

with open('scripts/output/enriched_questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

ids_to_inspect = [3, 12, 13, 36, 71]
output = []
for q in questions:
    if q['id'] in ids_to_inspect:
        output.append("="*60)
        output.append(f"ID: {q['id']} | Num: {q.get('original_num')}")
        output.append(f"Question: {q['question']}")
        output.append("Options:")
        for opt in q['options']:
            output.append(f"  {opt['key']}: {opt['text']}")
        output.append(f"Correct: {q['correct']}")
        output.append(f"Type: {q['type']}")
        ex = q.get('explanation')
        if ex:
            output.append("Explanation:")
            output.append(f"  vi_question: {ex.get('vi_question')}")
            output.append(f"  why_correct: {ex.get('why_correct')}")
            output.append(f"  why_wrong keys: {list(ex.get('why_wrong', {}).keys())}")
            for k, v in ex.get('why_wrong', {}).items():
                output.append(f"    {k}: {v}")
        else:
            output.append("Explanation: None")

with open('scripts/output/inspect_output.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(output))
print("Output written to scripts/output/inspect_output.txt successfully.")
