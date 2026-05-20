import json

with open('scripts/output/missing_explanations_report.json', 'r', encoding='utf-8') as f:
    report = json.load(f)

with open('scripts/output/enriched_questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

q_map = {q['id']: q for q in questions}

empty_ids = [36, 40, 72, 74, 165, 168, 231, 236, 240, 290, 343]

typos = []
missing_content = []
others = []

for item in report:
    qid = item['id']
    if qid in empty_ids:
        continue
        
    q = q_map[qid]
    incorrect_keys = item['incorrect_keys']
    current_keys = item['current_why_wrong_keys']
    missing_keys = item['missing_keys']
    extra_keys = item['extra_keys']
    
    # If the number of current explanations is equal to the number of incorrect options,
    # it's likely a simple key mismatch/typo
    if len(current_keys) == len(incorrect_keys):
        typos.append({
            'id': qid,
            'num': item['num'],
            'incorrect_keys': incorrect_keys,
            'current_keys': current_keys,
            'missing_keys': missing_keys,
            'extra_keys': extra_keys,
            'reason': 'Same number of keys, mismatch in keys (typos)'
        })
    elif len(current_keys) < len(incorrect_keys):
        # We are actually missing some explanations
        missing_content.append({
            'id': qid,
            'num': item['num'],
            'incorrect_keys': incorrect_keys,
            'current_keys': current_keys,
            'missing_keys': missing_keys,
            'extra_keys': extra_keys,
            'reason': f"Missing explanation text for keys: {missing_keys}"
        })
    else:
        others.append({
            'id': qid,
            'num': item['num'],
            'incorrect_keys': incorrect_keys,
            'current_keys': current_keys,
            'missing_keys': missing_keys,
            'extra_keys': extra_keys,
            'reason': 'More explanation keys than incorrect options'
        })

print(f"Total report items: {len(report)}")
print(f"Empty option questions: {len(empty_ids)}")
print(f"Key Typos/Swaps (Same count): {len(typos)}")
print(f"Truly Missing Content (Fewer keys): {len(missing_content)}")
print(f"Other mismatches (More keys): {len(others)}")

# Let's inspect some of the 'Truly Missing Content'
print("\nSample Truly Missing Content:")
for idx, m in enumerate(missing_content[:10]):
    print(f"  {idx+1}. ID {m['id']} (Num {m['num']}): Missing {m['missing_keys']} | Current: {m['current_keys']}")
