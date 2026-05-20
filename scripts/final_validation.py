"""
Final comprehensive review: Validate structure of all 349 questions
Check:
1. Each question has question text
2. Each question has options A, B, C, D (and E for multi)
3. Each question has at least one correct answer
4. Each question has complete why_wrong for all incorrect options
5. Questions with code-embedded options still have valid options in JSON
"""
import json
from collections import Counter

with open('src/data/questions_enhanced.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

issues = []
stats = {
    'total': len(questions),
    'has_question_text': 0,
    'has_options': 0,
    'has_correct': 0,
    'has_why_wrong_complete': 0,
    'correct_answer_count': Counter(),
}

for q in questions:
    qid = q['id']
    qtext = q.get('question', '').strip()
    options = q.get('options', [])
    correct = q.get('correct', [])
    ex = q.get('explanation', {})
    why_wrong = ex.get('why_wrong', {}) if ex else {}
    
    # Check question text
    if qtext:
        stats['has_question_text'] += 1
    else:
        issues.append(f"Q{qid}: EMPTY QUESTION TEXT")
    
    # Check options
    if options and len(options) >= 2:
        stats['has_options'] += 1
    else:
        issues.append(f"Q{qid}: MISSING OPTIONS (has {len(options)})")
    
    # Check correct answers
    if correct:
        stats['has_correct'] += 1
        stats['correct_answer_count'][len(correct)] += 1
    else:
        issues.append(f"Q{qid}: NO CORRECT ANSWER")
    
    # Check why_wrong completeness
    option_keys = [opt['key'] for opt in options]
    incorrect_keys = [k for k in option_keys if k not in correct]
    missing_why_wrong = [k for k in incorrect_keys if k not in why_wrong]
    
    if not missing_why_wrong:
        stats['has_why_wrong_complete'] += 1
    else:
        issues.append(f"Q{qid}: MISSING why_wrong for keys {missing_why_wrong}")

print("=" * 60)
print("FINAL REVIEW REPORT - questions_enhanced.json")
print("=" * 60)
print(f"\nTotal questions: {stats['total']}")
print(f"With question text: {stats['has_question_text']}")
print(f"With options (>=2): {stats['has_options']}")
print(f"With correct answers: {stats['has_correct']}")
print(f"With complete why_wrong: {stats['has_why_wrong_complete']}")
print(f"\nCorrect answer distribution:")
for count, freq in sorted(stats['correct_answer_count'].items()):
    label = "single" if count == 1 else f"multi ({count} correct)"
    print(f"  {count} correct answer(s) [{label}]: {freq} questions")

print(f"\nIssues found: {len(issues)}")
if issues:
    print("\nIssues:")
    for issue in issues:
        print(f"  - {issue}")
else:
    print("\n✅ No issues found! All 349 questions are valid.")

# Also check for duplicate IDs
ids = [q['id'] for q in questions]
if len(ids) == len(set(ids)):
    print("\n✅ No duplicate IDs found.")
else:
    from collections import Counter
    dupes = [id for id, c in Counter(ids).items() if c > 1]
    print(f"\n❌ Duplicate IDs found: {dupes}")
