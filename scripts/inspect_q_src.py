import json

with open('src/data/questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

for q in questions:
    if q['id'] == 36:
        print("="*60)
        print("IN src/data/questions.json:")
        print(f"ID: {q['id']}")
        print(f"Question: {q['question']}")
        print("Options:")
        for opt in q['options']:
            print(f"  {opt['key']}: {opt['text']}")
        print(f"Correct: {q['correct']}")
        print(f"Type: {q['type']}")
