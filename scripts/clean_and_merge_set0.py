import json
import re
import os

def clean_option_text(text):
    # Remove markers like ✅, **D. ✅**, etc.
    text = re.sub(r'\s*\-?\s*\*\*[A-H]\.\s*✅\s*\*\*', '', text)
    text = re.sub(r'✅', '', text)
    return text.strip()

def clean_and_merge():
    src_dir = r"c:\Development\Antigravity\Salesforce-PD1\src\data"
    set0_file = os.path.join(src_dir, "pd1_set0.json")
    questions_file = os.path.join(src_dir, "questions.json")

    with open(set0_file, 'r', encoding='utf-8') as f:
        set0_data = json.load(f)

    with open(questions_file, 'r', encoding='utf-8') as f:
        questions_data = json.load(f)

    cleaned_set0 = []
    
    for q in set0_data:
        # 1. Handle nested options and correct markers
        new_options = []
        correct_keys = set(q.get('correct', []))
        
        for opt in q['options']:
            text = opt['text']
            # Check for nested options (e.g. "- **D. ✅ ...")
            nested_match = re.search(r'\n\s*\-?\s*\*\*([A-H])\.\s*✅\s*\*\*\s*(.*)', text, re.DOTALL)
            if nested_match:
                # Split current option text
                main_text = text[:nested_match.start()].strip()
                opt['text'] = clean_option_text(main_text)
                new_options.append(opt)
                
                # Add the nested option
                nested_key = nested_match.group(1)
                nested_text = nested_match.group(2)
                new_options.append({
                    "key": nested_key,
                    "text": clean_option_text(nested_text)
                })
                correct_keys.add(nested_key)
            else:
                # Check if this option itself has the checkmark
                if '✅' in text:
                    # Try to extract key if it's explicitly marked like "**B. ✅**"
                    key_match = re.search(r'\*\*([A-H])\.\s*✅\s*\*\*', text)
                    if key_match:
                        correct_keys.add(key_match.group(1))
                    else:
                        correct_keys.add(opt['key'])
                
                opt['text'] = clean_option_text(text)
                new_options.append(opt)

        # 2. Try to infer correct answer from explanation if still empty
        if not correct_keys:
            why_correct = q.get('explanation', {}).get('why_correct', '')
            # Look for "A đúng", "B đúng", etc.
            match = re.search(r'([A-H])\s*đúng', why_correct)
            if match:
                correct_keys.add(match.group(1))
            
            # Also check why_wrong keys to infer correct if there's only one missing
            # (But that's risky)

        q['options'] = new_options
        q['correct'] = sorted(list(correct_keys))
        
        # Ensure type is correct
        q['type'] = 'multi' if len(q['correct']) > 1 else 'single'
        
        cleaned_set0.append(q)

    # Merge
    # Check if they are already there
    existing_ids = {q['id'] for q in questions_data}
    new_questions_added = 0
    for q in cleaned_set0:
        if q['id'] not in existing_ids:
            questions_data.append(q)
            new_questions_added += 1
        else:
            # Update existing? Maybe better to just leave it if it's already there
            pass

    # Sort by ID
    questions_data.sort(key=lambda x: x['id'])

    # Save
    with open(questions_file, 'w', encoding='utf-8') as f:
        json.dump(questions_data, f, ensure_ascii=False, indent=2)

    print(f"Cleaned {len(cleaned_set0)} questions from set0.")
    print(f"Added {new_questions_added} new questions to questions.json.")
    print(f"Total questions now: {len(questions_data)}")

if __name__ == "__main__":
    clean_and_merge()
