"""
Parse SF Developer 1_All_Question.md into structured JSON.
Each question has: question text, options (with correct/wrong), explanation.
Output: parsed_questions.json
"""
import re
import json
import os

MD_FILE = 'docs/SF Developer 1_All_Question.md'
OUTPUT_FILE = 'scripts/output/parsed_questions.json'

def parse_md():
    with open(MD_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by "---" (horizontal rule separating questions)
    # Each question block starts with "### Question N"
    blocks = re.split(r'\r?\n---\r?\n', content)
    
    questions = []
    global_id = 0

    for block in blocks:
        block = block.strip()
        if not block:
            continue
        
        # Check if this block has a question
        q_match = re.match(r'### Question (\d+)\r?\n(.*?)$', block, re.DOTALL)
        if not q_match:
            continue
        
        q_num = int(q_match.group(1))
        rest = q_match.group(2).strip()
        
        # Split into lines
        lines = rest.split('\n')
        lines = [l.rstrip('\r') for l in lines]
        
        # Separate: question text, options, explanation
        # Options start with "- [x]" or "- [ ]"
        # OR the question has A. B. C. D. format (code blocks)
        
        question_lines = []
        option_lines = []
        explanation_lines = []
        resources_lines = []
        
        in_options = False
        in_explanation = False
        in_resources = False
        
        for line in lines:
            if re.match(r'- \[.?\] \*\*[A-Z]\.\*\*', line):
                in_options = True
                in_explanation = False
                in_resources = False
                option_lines.append(line)
            elif line.startswith('**Explanation:**') or line.startswith('Explanation'):
                in_options = False
                in_explanation = True
                in_resources = False
            elif line.startswith('**Resources:**'):
                in_options = False
                in_explanation = False
                in_resources = True
            elif in_options:
                if re.match(r'- \[.?\] \*\*[A-Z]\.\*\*', line):
                    option_lines.append(line)
                else:
                    # Could be continuation of an option or end of options
                    # If it's a code block (A. B. C. D. format), stop parsing options
                    in_options = False
                    if not line.startswith('>') and not line.startswith('**'):
                        question_lines.append(line)
            elif in_explanation:
                explanation_lines.append(line)
            elif in_resources:
                resources_lines.append(line)
            else:
                question_lines.append(line)
        
        # Parse options
        options = []
        correct_keys = []
        
        for opt_line in option_lines:
            # "- [x] **A.** Some text  [CORRECT]"
            # "- [ ] **A.** Some text  [WRONG]"
            m = re.match(r'- \[(.?)\] \*\*([A-Z])\.\*\*\s+(.*?)(?:\s+\[(?:CORRECT|WRONG)\])?$', opt_line.strip())
            if m:
                checked = m.group(1)  # 'x' or ' '
                key = m.group(2)
                text = m.group(3).strip()
                # Remove trailing [CORRECT] or [WRONG]
                text = re.sub(r'\s*\[(?:CORRECT|WRONG)\]\s*$', '', text).strip()
                options.append({'key': key, 'text': text})
                if checked == 'x':
                    correct_keys.append(key)
        
        # Parse explanation
        explanation_text = ''
        for line in explanation_lines:
            if line.startswith('>'):
                explanation_text += line[1:].strip() + '\n'
            elif line.strip():
                explanation_text += line.strip() + '\n'
        explanation_text = explanation_text.strip()
        
        # Parse resources
        resources_text = ''
        for line in resources_lines:
            if line.startswith('>'):
                resources_text += line[1:].strip() + '\n'
            elif line.strip():
                resources_text += line.strip() + '\n'
        resources_text = resources_text.strip()
        
        # Clean question text
        question_text = '\n'.join(question_lines).strip()
        
        # Determine type
        q_type = 'multi' if len(correct_keys) > 1 else 'single'
        
        if not options and not correct_keys:
            # Some questions have code-block style options (A. B. C. D.)
            # Parse them differently
            # Look for patterns like "A.\n code...\nB.\n code..."
            # For now, mark as special
            pass
        
        global_id += 1
        
        questions.append({
            'id': global_id,
            'original_num': q_num,
            'question': question_text,
            'options': options,
            'correct': correct_keys,
            'type': q_type,
            'explanation_en': explanation_text,
            'resources': resources_text,
            'explanation': {
                'vi_question': '',
                'why_correct': '',
                'why_wrong': {},
                'tip': ''
            }
        })
    
    return questions

if __name__ == '__main__':
    os.makedirs('scripts/output', exist_ok=True)
    questions = parse_md()
    
    # Stats
    total = len(questions)
    with_opts = sum(1 for q in questions if q['options'])
    without_opts = sum(1 for q in questions if not q['options'])
    with_explanation = sum(1 for q in questions if q['explanation_en'])
    
    print(f'Total questions parsed: {total}')
    print(f'  With options (checkbox format): {with_opts}')
    print(f'  Without options (code block format): {without_opts}')
    print(f'  With English explanation: {with_explanation}')
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)
    
    print(f'\nSaved to {OUTPUT_FILE}')
    
    # Show sample
    print('\n--- Sample Q1 ---')
    q = questions[0]
    print(f'Question: {q["question"][:200]}')
    print(f'Options: {q["options"]}')
    print(f'Correct: {q["correct"]}')
    print(f'Explanation EN: {q["explanation_en"][:200]}')
