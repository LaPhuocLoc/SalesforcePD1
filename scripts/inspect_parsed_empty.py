import json

with open('scripts/output/parsed_questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

for q in questions:
    if q['id'] == 36:
        print("="*60)
        print("IN scripts/output/parsed_questions.json:")
        print(f"ID: {q['id']}")
        print(f"Question: {q['question']}")
        print(f"Options: {q.get('options')}")
        print(f"Correct: {q.get('correct')}")
        print(f"Type: {q.get('type')}")
