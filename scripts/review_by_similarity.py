"""
Correct review: Match JSON questions to MD source by question text similarity.
The dataset has multiple question sets with the same original_num (1-60) for different questions.
We must match by text content, not by num.
"""
import json
import re
from difflib import SequenceMatcher

def normalize(text):
    """Normalize text for comparison"""
    text = text.lower().strip()
    # Remove extra whitespace and newlines
    text = re.sub(r'\s+', ' ', text)
    # Remove code formatting
    text = re.sub(r'[`*_]', '', text)
    # Take just first 100 chars for quick comparison
    return text[:150]

def similarity(a, b):
    return SequenceMatcher(None, normalize(a), normalize(b)).ratio()

# Parse MD source
def parse_md_source(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    question_blocks = re.split(r'(?=### Question \d+)', content)
    
    questions = []
    for block in question_blocks:
        block = block.strip()
        if not block:
            continue
        
        num_match = re.match(r'### Question (\d+)', block)
        if not num_match:
            continue
        q_num = int(num_match.group(1))
        
        text_block = re.sub(r'^### Question \d+\s*\n', '', block).strip()
        
        # Find options
        option_lines = re.findall(r'- \[(x| )\] \*\*([A-E])\.\*\* (.*?)  \[(CORRECT|WRONG)\]', text_block)
        
        # Question text = before first option
        question_text_match = re.match(r'(.*?)(?=\n- \[)', text_block, re.DOTALL)
        question_text = question_text_match.group(1).strip() if question_text_match else text_block[:200]
        
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

print("Parsing MD source...")
md_questions = parse_md_source('docs/SF Developer 1_All_Question.md')
print(f"  {len(md_questions)} MD questions parsed")

print("Loading JSON...")
with open('src/data/questions_enhanced.json', 'r', encoding='utf-8') as f:
    json_questions = json.load(f)
print(f"  {len(json_questions)} JSON questions loaded")

# For each MD question, find the best matching JSON question
print("\nMatching by text similarity...")

results = []
unmatched_md = []
matched_pairs = []

for md_q in md_questions:
    best_score = 0
    best_json_q = None
    
    for jq in json_questions:
        score = similarity(md_q['question'], jq['question'])
        if score > best_score:
            best_score = score
            best_json_q = jq
    
    if best_score >= 0.7:  # threshold for a good match
        matched_pairs.append((md_q, best_json_q, best_score))
    else:
        unmatched_md.append((md_q, best_score, best_json_q))

print(f"  Matched: {len(matched_pairs)}")
print(f"  Unmatched MD (score < 0.7): {len(unmatched_md)}")

# Check correct answer mismatches among matched pairs
correct_mismatches = []
correct_matches = 0

for md_q, jq, score in matched_pairs:
    md_correct = md_q['correct']
    json_correct = sorted(jq.get('correct', []))
    
    if md_correct == json_correct:
        correct_matches += 1
    else:
        correct_mismatches.append({
            'json_id': jq['id'],
            'json_original_num': jq.get('original_num'),
            'md_num': md_q['num'],
            'match_score': round(score, 3),
            'md_correct': md_correct,
            'json_correct': json_correct,
            'question_preview': md_q['question'][:100]
        })

print(f"\n  Correct answer MATCHES: {correct_matches}")
print(f"  Correct answer MISMATCHES: {len(correct_mismatches)}")

# Show unmatched
if unmatched_md:
    print("\nUnmatched MD questions (might be code-heavy questions):")
    for md_q, score, best in unmatched_md[:10]:
        print(f"  MD Q{md_q['num']} (best_score={score:.2f}): {md_q['question'][:80]}...")
        if best:
            print(f"    Best JSON match: {best['question'][:80]}...")

# Save mismatches report
output_lines = [
    f"=== CORRECT MATCH REVIEW ===",
    f"Total MD questions: {len(md_questions)}",
    f"Matched pairs: {len(matched_pairs)}",
    f"Correct answer matches: {correct_matches}",
    f"Correct answer MISMATCHES: {len(correct_mismatches)}",
    ""
]

for item in correct_mismatches:
    output_lines.append(f"JSON ID {item['json_id']} (MD Q{item['md_num']}, match={item['match_score']})")
    output_lines.append(f"  MD correct:   {item['md_correct']}")
    output_lines.append(f"  JSON correct: {item['json_correct']}")
    output_lines.append(f"  Q: {item['question_preview']}")
    output_lines.append("")

with open('scripts/output/correct_answer_review.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(output_lines))

with open('scripts/output/correct_answer_mismatches.json', 'w', encoding='utf-8') as f:
    json.dump(correct_mismatches, f, ensure_ascii=False, indent=2)

print("\nSaved to scripts/output/correct_answer_review.txt")
