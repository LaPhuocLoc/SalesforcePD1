"""
Step 2: Text → questions_raw.json
Parse plain text extracted via pdfplumber.

Format:
  Question N:Correct
  <question text>
  ● Option A text
  ● Option B text(Correct)
"""

import json
import re
from pathlib import Path

# ─── Paths ───────────────────────────────────────────────────────────────────
SCRIPT_DIR   = Path(__file__).parent
INPUT_TXT    = SCRIPT_DIR / "output" / "questions_raw.txt"
OUTPUT_JSON  = SCRIPT_DIR / "output" / "questions_raw.json"

def parse_questions(text: str) -> list[dict]:
    questions = []
    
    # Split by "Question N:Correct" or "Question N:"
    # Use re.split to keep the question number if possible, or just split on the boundary
    blocks = re.split(r'\n(?=Question\s+\d+:)', '\n' + text, flags=re.IGNORECASE)
    
    option_letters = list("ABCDEFGH")

    for block in blocks:
        block = block.strip()
        if not block:
            continue

        # Extract question number
        q_num_match = re.match(r'^Question\s+(\d+):', block, re.IGNORECASE)
        if not q_num_match:
            continue
        q_id = int(q_num_match.group(1))

        # Split block into lines
        lines = block.split('\n')
        
        # Line 0 is the header "Question N:Correct"
        body_lines = lines[1:]
        
        question_lines = []
        option_lines = []
        
        in_options = False
        
        for line in body_lines:
            line = line.strip()
            if not line:
                continue
                
            # Check if line starts with ● (U+25CF) - NEW OPTION
            if line.startswith('●'):
                in_options = True
                option_lines.append(line)
            # Check if line starts with ○ (U+25CB) or is already in options - CONTINUATION
            elif in_options:
                # If we are in options and a line doesn't start with a black bullet,
                # it's likely a continuation of the previous option
                if option_lines:
                    # Use newline for code blocks
                    option_lines[-1] += "\n" + line
                else:
                    # Fallback
                    option_lines.append(line)
            else:
                question_lines.append(line)

        q_text = '\n'.join(question_lines).strip()
        
        options = []
        correct = []

        for i, opt_line in enumerate(option_lines):
            # Remove leading bullets (both types) and strip each line if multi-line
            lines = opt_line.split('\n')
            clean_lines = [re.sub(r'^[●○]\s*', '', l).strip() for l in lines]
            opt_text = '\n'.join(clean_lines).strip()
            
            # Check if this is correct answer
            is_correct = False
            if re.search(r'\(Correct\)\s*$', opt_text, re.IGNORECASE):
                is_correct = True
                opt_text = re.sub(r'\s*\(Correct\)\s*$', '', opt_text, flags=re.IGNORECASE).strip()

            letter = option_letters[i] if i < len(option_letters) else str(i + 1)
            options.append({"key": letter, "text": opt_text})

            if is_correct:
                correct.append(letter)

        q_type = "multi" if len(correct) > 1 else "single"

        if not options:
            print(f"  [WARN] Q{q_id}: No options found, might be a formatting issue")
        if not correct and options:
            print(f"  [WARN] Q{q_id}: No correct answer found!")

        questions.append({
            "id":       q_id,
            "question": q_text,
            "options":  options,
            "correct":  correct,
            "type":     q_type,
            "topic":    "",
            "explanation": {
                "vi_question": "",
                "why_correct":  "",
                "why_wrong":    {},
                "tip":          "",
            }
        })

    # Sort by ID just in case
    questions.sort(key=lambda x: x["id"])
    return questions

def main():
    if not INPUT_TXT.exists():
        raise FileNotFoundError(f"Text file not found: {INPUT_TXT}")

    text = INPUT_TXT.read_text(encoding="utf-8")
    print(f"[*] Parsing {len(text):,} chars of text...")

    questions = parse_questions(text)

    total = len(questions)
    has_correct = sum(1 for q in questions if q["correct"])
    no_correct  = total - has_correct
    multi       = sum(1 for q in questions if q["type"] == "multi")

    print(f"\n[RESULT] Parsed {total} questions")
    print(f"  With correct answer:  {has_correct}")
    print(f"  Missing answer:       {no_correct}")
    print(f"  Multi-select:         {multi}")
    print(f"  Single-select:        {total - multi}")

    print(f"\n[Sample] First 3 questions:")
    for q in questions[:3]:
        print(f"\n  Q{q['id']}: {q['question'][:80]}...")
        for opt in q['options']:
            marker = " <-- CORRECT" if opt['key'] in q['correct'] else ""
            print(f"    {opt['key']}. {opt['text'][:70]}{marker}")

    OUTPUT_JSON.write_text(
        json.dumps(questions, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )
    print(f"\n[OK] Saved to: {OUTPUT_JSON}")

if __name__ == "__main__":
    main()
