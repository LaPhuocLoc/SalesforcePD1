import json
import re
import os

def clean_option_text(text):
    # Remove markers like ✅, **D. ✅**, etc.
    text = re.sub(r'\s*\-?\s*\*\*[A-H]\.\s*✅\s*\*\*', '', text)
    text = re.sub(r'✅', '', text)
    return text.strip()

def fix_data_quality():
    src_dir = r"c:\Development\Antigravity\Salesforce-PD1\src\data"
    questions_file = os.path.join(src_dir, "questions.json")

    with open(questions_file, 'r', encoding='utf-8') as f:
        questions_data = json.load(f)

    for q in questions_data:
        if q['id'] < 213:
            continue
            
        # 1. Handle nested options and correct markers
        new_options = []
        correct_keys = set()
        
        # Look for "X đúng" in explanation first as it's often more reliable in this dataset
        why_correct = q.get('explanation', {}).get('why_correct', '')
        # Matches "A đúng", "A và B đúng", "A, B đúng", "A, B, và C đúng"
        matches = re.findall(r'([A-H])(?:\s*(?:,|và|&)\s*)*\s*đúng', why_correct)
        for m in matches:
            correct_keys.add(m)

        for opt in q['options']:
            text = opt['text']
            
            # Check if this option itself has the checkmark
            if '✅' in text:
                key_match = re.search(r'\*\*([A-H])\.\s*✅\s*\*\*', text)
                if key_match:
                    correct_keys.add(key_match.group(1))
                else:
                    correct_keys.add(opt['key'])
            
            # Check for nested options (e.g. "- **D. ✅ ...")
            # We look for ANY letter, not just with checkmark, if it's clearly a new line with a letter
            nested_lines = re.split(r'\n\s*\-?\s*\*\*([A-H])\.', text)
            if len(nested_lines) > 1:
                # First part is the current option's text
                opt['text'] = clean_option_text(nested_lines[0])
                new_options.append(opt)
                
                # Subsequent parts are (letter, text, letter, text...)
                for i in range(1, len(nested_lines), 2):
                    letter = nested_lines[i]
                    content = nested_lines[i+1] if i+1 < len(nested_lines) else ""
                    
                    if '✅' in content:
                        correct_keys.add(letter)
                    
                    new_options.append({
                        "key": letter,
                        "text": clean_option_text(content)
                    })
            else:
                opt['text'] = clean_option_text(text)
                new_options.append(opt)

        # Remove duplicate options by key
        unique_options = {}
        for o in new_options:
            unique_options[o['key']] = o['text']
        
        q['options'] = [{"key": k, "text": v} for k, v in sorted(unique_options.items())]
        
        # Final check for correct keys: if still empty, use what we found in why_correct
        if not correct_keys:
            # Fallback to whatever was there
            pass
        else:
            q['correct'] = sorted(list(correct_keys))
        
        # Ensure type is correct
        q['type'] = 'multi' if len(q['correct']) > 1 else 'single'

    # Save
    with open(questions_file, 'w', encoding='utf-8') as f:
        json.dump(questions_data, f, ensure_ascii=False, indent=2)

    print(f"Refined data quality for questions 213-272 in questions.json.")

if __name__ == "__main__":
    fix_data_quality()
