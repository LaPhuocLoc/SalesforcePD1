import json

with open('scripts/output/questions_full.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

for q in questions:
    if q['id'] in [36, 40, 72, 74, 165, 168]:
        print("="*60)
        print(f"ID: {q['id']} | Correct: {q.get('correct')}")
        print(f"Question text: {q['question'][:100]}...")
        print("Options:")
        for opt in q['options']:
            print(f"  {opt['key']}: {opt['text']}")
