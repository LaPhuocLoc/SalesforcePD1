"""
Fix why_wrong key mismatches in enriched_questions.json
Strategy:
1. For questions with empty options - restore from questions_full.json
2. For key typo/swaps - remap why_wrong keys to correct incorrect keys
3. For truly missing content - mark for manual enrichment
"""
import json
import re

# Load data
with open('scripts/output/enriched_questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

with open('scripts/output/questions_full.json', 'r', encoding='utf-8') as f:
    questions_full = json.load(f)

full_map = {q['id']: q for q in questions_full}

# IDs with empty options (options embedded in question text)
EMPTY_OPTION_IDS = [36, 40, 72, 74, 165, 168, 231, 236, 240, 290, 343]

# For questions with empty options, the options and correct answer are embedded in the question text
# We need to restore them from questions_full.json or define them manually
# Questions 231, 236, 240, 290, 343 don't exist in questions_full (they're from a different set)
# Let's parse them manually from the question text

def parse_options_from_question(question_text):
    """Parse options (A, B, C, D) from question text when they're embedded"""
    lines = question_text.split('\n')
    question_part = []
    options = []
    
    # Find the main question and option blocks
    current_option_key = None
    current_option_text = []
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        
        # Check if line starts with option key
        option_match = re.match(r'^([A-E])\.\s*(.*)', line)
        if option_match:
            # Save previous option if any
            if current_option_key:
                options.append({
                    'key': current_option_key,
                    'text': ' '.join(current_option_text).strip()
                })
            current_option_key = option_match.group(1)
            current_option_text = [option_match.group(2)] if option_match.group(2) else []
        elif current_option_key:
            current_option_text.append(line)
        else:
            question_part.append(line)
    
    # Add last option
    if current_option_key:
        options.append({
            'key': current_option_key,
            'text': ' '.join(current_option_text).strip()
        })
    
    return '\n'.join(question_part), options

# Manual correct answers for questions not in questions_full
MANUAL_CORRECT = {
    231: ['B'],  # Lightning Out requires ltng:outApp
    236: ['B'],  # implements multiple interfaces with single 'implements'
    240: ['C'],  # prop is null by default
    290: ['B'],  # implements with body {}
    343: ['D'],  # bulkified, DML outside loop
}

def fix_questions(questions):
    """Fix all issues in the questions list"""
    fixed_count = 0
    empty_fixed = 0
    key_fixed = 0
    
    for q in questions:
        qid = q['id']
        options = q.get('options', [])
        correct = q.get('correct', [])
        explanation = q.get('explanation', {})
        why_wrong = explanation.get('why_wrong', {}) if explanation else {}
        
        # Step 1: Fix empty options
        if qid in EMPTY_OPTION_IDS:
            if qid in full_map and full_map[qid].get('options'):
                # Restore from questions_full
                original = full_map[qid]
                q['options'] = original['options']
                q['correct'] = original['correct']
                q['type'] = original.get('type', 'single')
                print(f"  Fixed empty options for Q{qid} from questions_full")
                empty_fixed += 1
            else:
                # Parse from question text
                question_text = q.get('question', '')
                clean_question, parsed_options = parse_options_from_question(question_text)
                if parsed_options:
                    q['question'] = clean_question
                    q['options'] = parsed_options
                    if qid in MANUAL_CORRECT:
                        q['correct'] = MANUAL_CORRECT[qid]
                    print(f"  Parsed options for Q{qid} from question text ({len(parsed_options)} options)")
                    empty_fixed += 1
        
        # Step 2: Fix why_wrong key mismatches
        # Recalculate based on current state
        current_options = q.get('options', [])
        current_correct = q.get('correct', [])
        all_option_keys = [opt['key'] for opt in current_options]
        incorrect_keys = sorted([k for k in all_option_keys if k not in current_correct])
        
        if not explanation or not isinstance(why_wrong, dict):
            continue
        
        why_wrong_keys = sorted(list(why_wrong.keys()))
        missing_keys = [k for k in incorrect_keys if k not in why_wrong_keys]
        extra_keys = [k for k in why_wrong_keys if k not in incorrect_keys]
        
        if not missing_keys and not extra_keys:
            continue  # Already correct
        
        # If we have extra keys that are correct answers, they were put in wrong section
        # And we have missing keys from incorrect options
        # Strategy: match by position - remap extra keys to missing keys
        if extra_keys and missing_keys and len(extra_keys) == len(missing_keys):
            # Simple key swap - remap
            new_why_wrong = {}
            for k in why_wrong_keys:
                if k in extra_keys:
                    # Map to corresponding missing key by position
                    pos = extra_keys.index(k)
                    new_key = missing_keys[pos]
                    new_why_wrong[new_key] = why_wrong[k]
                else:
                    new_why_wrong[k] = why_wrong[k]
            
            q['explanation']['why_wrong'] = new_why_wrong
            key_fixed += 1
            fixed_count += 1
        elif extra_keys and not missing_keys:
            # Extra keys - remove the ones that are correct answers
            new_why_wrong = {k: v for k, v in why_wrong.items() if k not in current_correct}
            q['explanation']['why_wrong'] = new_why_wrong
            key_fixed += 1
            fixed_count += 1
        elif missing_keys and not extra_keys:
            # Truly missing - leave as is for now (will be filled by enrichment)
            pass
        elif extra_keys and missing_keys:
            # Complex case - try to remap what we can
            new_why_wrong = {}
            available_missing = list(missing_keys)
            available_extra = list(extra_keys)
            
            for k in why_wrong_keys:
                if k in extra_keys and available_missing:
                    new_key = available_missing.pop(0)
                    available_extra.remove(k)
                    new_why_wrong[new_key] = why_wrong[k]
                elif k not in extra_keys:
                    new_why_wrong[k] = why_wrong[k]
            
            q['explanation']['why_wrong'] = new_why_wrong
            key_fixed += 1
            fixed_count += 1
    
    print(f"\nSummary:")
    print(f"  Empty options fixed: {empty_fixed}")
    print(f"  Key mismatches fixed: {key_fixed}")
    print(f"  Total fixed: {fixed_count + empty_fixed}")
    
    return questions

print("Starting fix process...")
fixed_questions = fix_questions(questions)

# Save fixed questions
with open('scripts/output/enriched_questions.json', 'w', encoding='utf-8') as f:
    json.dump(fixed_questions, f, ensure_ascii=False, indent=2)

print("\nSaved fixed questions to scripts/output/enriched_questions.json")
