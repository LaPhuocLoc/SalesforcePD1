import json

filepaths = [
    'scripts/output/questions_raw.json',
    'scripts/output/parsed_questions.json',
    'scripts/output/questions_full.json'
]

empty_ids = [36, 40, 72, 74, 165, 168, 231, 236, 240, 290, 343]

for path in filepaths:
    print("="*60)
    print(f"FILE: {path}")
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Check if list or dict
        if isinstance(data, dict):
            # Try to get values
            data_list = list(data.values())
        else:
            data_list = data
            
        found = 0
        for q in data_list:
            qid = q.get('id')
            if qid in empty_ids:
                print(f"  ID {qid}: options={len(q.get('options', []))}, correct={q.get('correct')}")
                found += 1
        print(f"Total found in this file: {found}")
    except Exception as e:
        print(f"Error reading {path}: {e}")
