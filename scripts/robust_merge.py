import json
import re
import os

def clean_text(text):
    if not text: return ""
    # Remove markers like ✅
    text = re.sub(r'✅', '', text)
    # Remove bold markers surrounding the letter like **B. **
    text = re.sub(r'\s*\-?\s*\*\*[A-H]\.\s*\*\*', '', text)
    # Remove any stray bold markers at the start/end
    text = text.strip()
    if text.startswith('**'): text = text[2:]
    if text.endswith('**'): text = text[:-2]
    return text.strip()

def robust_merge():
    src_dir = r"c:\Development\Antigravity\Salesforce-PD1\src\data"
    set0_file = os.path.join(src_dir, "pd1_set0.json")
    questions_file = os.path.join(src_dir, "questions.json")

    with open(questions_file, 'r', encoding='utf-8') as f:
        master_data = json.load(f)
    
    # Keep only the original 212
    master_data = [q for q in master_data if q['id'] <= 212]

    with open(set0_file, 'r', encoding='utf-8') as f:
        set0_raw = json.load(f)

    cleaned_set0 = []
    for q in set0_raw:
        correct_keys = set()
        
        # 1. Extract from why_correct (Vietnamese)
        why_correct = q.get('explanation', {}).get('why_correct', '')
        vn_matches = re.findall(r'([A-H])(?:\s*(?:,|và|&)\s*)*\s*đúng', why_correct)
        for m in vn_matches:
            correct_keys.add(m)
            
        # 2. Extract from options text (markers)
        processed_options = []
        for opt in q['options']:
            key = opt['key']
            text = opt['text']
            
            if '✅' in text:
                m = re.search(r'\*\*([A-H])\.\s*✅', text)
                if m:
                    correct_keys.add(m.group(1))
                else:
                    correct_keys.add(key)
            
            parts = re.split(r'\n\s*\-?\s*\*\*([A-H])\.', text)
            if len(parts) > 1:
                processed_options.append({"key": key, "text": clean_text(parts[0])})
                for i in range(1, len(parts), 2):
                    n_key = parts[i]
                    n_text = parts[i+1] if i+1 < len(parts) else ""
                    if '✅' in n_text:
                        correct_keys.add(n_key)
                    processed_options.append({"key": n_key, "text": clean_text(n_text)})
            else:
                processed_options.append({"key": key, "text": clean_text(text)})

        unique_opts = {}
        for o in processed_options:
            unique_opts[o['key']] = o['text']
        
        q['options'] = [{"key": k, "text": v} for k, v in sorted(unique_opts.items())]
        q['correct'] = sorted(list(correct_keys))
        q['type'] = 'multi' if len(q['correct']) > 1 else 'single'
        cleaned_set0.append(q)

    master_data.extend(cleaned_set0)
    master_data.sort(key=lambda x: x['id'])

    with open(questions_file, 'w', encoding='utf-8') as f:
        json.dump(master_data, f, ensure_ascii=False, indent=2)

    print(f"Successfully performed robust merge of 60 questions with cleaner text.")

if __name__ == "__main__":
    robust_merge()
