import json

with open('src/data/questions.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f'Total questions in questions.json: {len(data)}')
print(f'First ID: {data[0]["id"]}')
print(f'Last ID: {data[-1]["id"]}')

# Check how many have all fields filled
complete = sum(1 for q in data 
               if q.get('explanation') 
               and q['explanation'].get('vi_question') 
               and q['explanation'].get('why_correct') 
               and q['explanation'].get('why_wrong') 
               and q['explanation'].get('tip'))

empty = sum(1 for q in data 
            if not q.get('explanation') 
            or not q['explanation'].get('vi_question'))

partial = len(data) - complete - empty
print(f'Questions with COMPLETE explanation: {complete}')
print(f'Questions with PARTIAL explanation: {partial}')
print(f'Questions with EMPTY/MISSING explanation: {empty}')

# Sample some with missing data
print('\nSample questions with missing data:')
count = 0
for q in data:
    if not q.get('explanation') or not q['explanation'].get('vi_question') or not q['explanation'].get('tip'):
        print(f'  ID {q["id"]}: vi_question={bool(q.get("explanation", {}).get("vi_question"))}, '
              f'why_correct={bool(q.get("explanation", {}).get("why_correct"))}, '
              f'why_wrong={bool(q.get("explanation", {}).get("why_wrong"))}, '
              f'tip={bool(q.get("explanation", {}).get("tip"))}')
        count += 1
        if count >= 10:
            break
