import json

with open('scripts/output/enriched_questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

missing_ids = [17, 63, 71, 80, 154, 162, 167, 171, 216, 222, 226, 274, 330]
q_map = {q['id']: q for q in questions}

output = []
for qid in missing_ids:
    q = q_map[qid]
    ex = q.get('explanation', {})
    
    all_keys = [opt['key'] for opt in q.get('options', [])]
    incorrect_keys = [k for k in all_keys if k not in q.get('correct', [])]
    why_wrong_keys = list(ex.get('why_wrong', {}).keys())
    missing_keys = [k for k in incorrect_keys if k not in why_wrong_keys]
    
    output.append("="*70)
    output.append(f"ID: {qid} | Num: {q.get('original_num')} | Correct: {q.get('correct')}")
    output.append(f"MISSING keys: {missing_keys}")
    output.append(f"Question: {q['question']}")
    output.append(f"Options:")
    for opt in q.get('options', []):
        marker = "[CORRECT]" if opt['key'] in q.get('correct', []) else "[WRONG]"
        missing_marker = "[NEED EXPLANATION]" if opt['key'] in missing_keys else ""
        output.append(f"  {opt['key']}: {opt['text']} {marker} {missing_marker}")
    output.append(f"why_correct: {ex.get('why_correct')}")
    output.append(f"Existing why_wrong:")
    for k, v in ex.get('why_wrong', {}).items():
        output.append(f"  {k}: {v}")

with open('scripts/output/need_enrichment.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(output))
print("Written need_enrichment.txt successfully")
