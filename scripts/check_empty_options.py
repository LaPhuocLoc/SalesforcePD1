import json

with open('scripts/output/enriched_questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

empty_options = []
empty_correct = []
for q in questions:
    if not q.get('options'):
        empty_options.append(q['id'])
    if not q.get('correct'):
        empty_correct.append(q['id'])

print(f"Questions with empty options: {len(empty_options)} -> {empty_options}")
print(f"Questions with empty correct: {len(empty_correct)} -> {empty_correct}")
