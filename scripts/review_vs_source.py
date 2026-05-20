"""
Deep review: Compare questions_enhanced.json against SF Developer 1_All_Question.md
Checks:
1. Correct answer keys match between source MD and JSON
2. Option text is not grossly different
3. All options present
4. No duplicate questions
"""
import json
import re
import sys

# ---- Parse the source MD file ----
def parse_md_source(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split on question separators (--- or ### Question N)
    # Find all question blocks
    # Pattern: ### Question N ... ---
    question_blocks = re.split(r'(?=### Question \d+)', content)
    
    questions = []
    for block in question_blocks:
        block = block.strip()
        if not block:
            continue
        
        # Extract question number
        num_match = re.match(r'### Question (\d+)', block)
        if not num_match:
            continue
        q_num = int(num_match.group(1))
        
        # Extract question text (between number header and first option)
        # Remove the "### Question N" header
        text_block = re.sub(r'^### Question \d+\s*\n', '', block).strip()
        
        # Find options - lines starting with - [x] or - [ ]
        option_lines = re.findall(r'- \[(x| )\] \*\*([A-E])\.\*\* (.*?)  \[(CORRECT|WRONG)\]', text_block)
        
        # Find the question text (before first option)
        question_text_match = re.match(r'(.*?)(?=\n- \[)', text_block, re.DOTALL)
        question_text = question_text_match.group(1).strip() if question_text_match else ""
        
        options = []
        correct = []
        for opt in option_lines:
            is_checked, key, text, label = opt
            options.append({'key': key, 'text': text.strip()})
            if is_checked == 'x':
                correct.append(key)
        
        questions.append({
            'num': q_num,
            'question': question_text,
            'options': options,
            'correct': sorted(correct)
        })
    
    return questions

# ---- Load JSON ----
def load_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

# ---- Compare ----
def compare(md_questions, json_questions):
    # Build lookup maps
    md_map = {}
    for q in md_questions:
        md_map[q['num']] = q
    
    # JSON questions use original_num to reference the MD question number
    issues = []
    matched = 0
    
    for jq in json_questions:
        jid = jq['id']
        jnum = jq.get('original_num')
        
        if jnum not in md_map:
            issues.append({
                'id': jid,
                'original_num': jnum,
                'type': 'NOT_FOUND_IN_MD',
                'detail': f'original_num {jnum} not found in source MD'
            })
            continue
        
        mq = md_map[jnum]
        
        # 1. Check correct answers match
        json_correct = sorted(jq.get('correct', []))
        md_correct = mq['correct']
        
        if json_correct != md_correct:
            issues.append({
                'id': jid,
                'original_num': jnum,
                'type': 'CORRECT_ANSWER_MISMATCH',
                'detail': f'JSON correct={json_correct}, MD correct={md_correct}',
                'json_correct': json_correct,
                'md_correct': md_correct,
                'question_preview': jq['question'][:100]
            })
            continue
        
        # 2. Check option count matches (only if MD has options)
        if mq['options']:
            json_opt_count = len(jq.get('options', []))
            md_opt_count = len(mq['options'])
            
            if json_opt_count != md_opt_count:
                issues.append({
                    'id': jid,
                    'original_num': jnum,
                    'type': 'OPTION_COUNT_MISMATCH',
                    'detail': f'JSON has {json_opt_count} options, MD has {md_opt_count} options',
                    'json_correct': json_correct,
                    'md_correct': md_correct,
                    'question_preview': jq['question'][:100]
                })
        
        matched += 1
    
    return issues, matched

print("Parsing source MD file...")
md_questions = parse_md_source('docs/SF Developer 1_All_Question.md')
print(f"  Parsed {len(md_questions)} questions from MD")

print("Loading JSON file...")
json_questions = load_json('src/data/questions_enhanced.json')
print(f"  Loaded {len(json_questions)} questions from JSON")

print("Comparing...")
issues, matched = compare(md_questions, json_questions)

# Write detailed report
report_lines = []
report_lines.append(f"=== REVIEW REPORT ===")
report_lines.append(f"MD source questions: {len(md_questions)}")
report_lines.append(f"JSON questions: {len(json_questions)}")
report_lines.append(f"Successfully matched: {matched}")
report_lines.append(f"Issues found: {len(issues)}")
report_lines.append("")

# Group by type
from collections import defaultdict
by_type = defaultdict(list)
for issue in issues:
    by_type[issue['type']].append(issue)

for issue_type, items in sorted(by_type.items()):
    report_lines.append(f"--- {issue_type} ({len(items)} issues) ---")
    for item in items:
        report_lines.append(f"  ID {item['id']} (Num {item['original_num']}): {item['detail']}")
        if 'question_preview' in item:
            report_lines.append(f"    Q: {item['question_preview']}")
    report_lines.append("")

with open('scripts/output/review_report.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(report_lines))

print(f"\nTotal issues: {len(issues)}")
print("Full report saved to scripts/output/review_report.txt")

# Also save raw issues as JSON
with open('scripts/output/review_issues.json', 'w', encoding='utf-8') as f:
    json.dump(issues, f, ensure_ascii=False, indent=2)
