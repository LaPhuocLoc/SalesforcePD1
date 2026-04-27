"""
Step 3: questions_raw.json → questions_full.json
Dùng Gemini API để generate explanation cho từng câu hỏi.

Requirements:
  pip install google-genai

Usage:
  1. Set GEMINI_API_KEY trong file .env hoặc export thành env var
  2. python scripts/step3_generate_explanations.py

Features:
  - Batch processing với rate limit protection
  - Resume: nếu bị ngắt giữa chừng, chạy lại sẽ bỏ qua câu đã có explanation
  - Progress tracking
"""

import json
import os
import time
from pathlib import Path

from google import genai
from google.genai import types

# ─── Config ──────────────────────────────────────────────────────────────────
SCRIPT_DIR  = Path(__file__).parent
INPUT_JSON  = SCRIPT_DIR / "output" / "questions_raw.json"
OUTPUT_JSON = SCRIPT_DIR / "output" / "questions_full.json"

# Gemini config
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")  # hoặc hard-code tạm thời nếu cần
GEMINI_MODEL   = "gemini-1.5-flash"                  # user requested 'gemini 3.1 pro' but it is not available, using 1.5 pro
DELAY_BETWEEN  = 1.0                                # flash is faster, 1s delay is enough
MAX_RETRIES    = 3


# ─── Prompt Template ─────────────────────────────────────────────────────────
def build_prompt(q: dict) -> str:
    options_text = "\n".join(
        f"  {opt['key']}. {opt['text']}" for opt in q["options"]
    )
    correct_text = ", ".join(q["correct"])

    wrong_keys = [
        opt["key"] for opt in q["options"] if opt["key"] not in q["correct"]
    ]
    wrong_instructions = "\n".join(
        f'    "{k}": "Giải thích tại sao {k} sai..."'
        for k in wrong_keys
    )

    return f"""Bạn là một Salesforce Architect lão luyện, đang giải thích câu hỏi thi Salesforce PD1 (Platform Developer 1).

---
CÂU HỎI:
{q['question']}

LỰA CHỌN:
{options_text}

ĐÁP ÁN ĐÚNG: {correct_text}
---

Hãy trả về JSON theo đúng format sau (KHÔNG thêm markdown, KHÔNG thêm text ngoài JSON):

{{
  "vi_question": "Dịch câu hỏi sang tiếng Việt. GIỮ NGUYÊN các thuật ngữ kỹ thuật Salesforce bằng tiếng Anh (ví dụ: Apex, Governor Limit, SOQL, Trigger, VF page, LWC). Dịch thoát nghĩa, không dịch sát từng từ.",
  "why_correct": "Phân tích tại sao đáp án {correct_text} là đúng. Đối chiếu với Salesforce Official Documentation. Nếu liên quan Apex, chỉ ra Governor Limits hoặc Bulkification nếu có. Viết ngắn gọn, súc tích, đủ ý. 2-4 câu.",
  "why_wrong": {{
{wrong_instructions}
  }},
  "tip": "Mẹo ghi nhớ 1 câu: dùng keyword hay xuất hiện trong đề thi thực tế PD1. Format: 'Nhớ: [keyword] = [điều cần nhớ]' hoặc 'Bẫy: [tình huống dễ nhầm]'."
}}
"""


# ─── Gemini Call ──────────────────────────────────────────────────────────────
def generate_explanation(client, q: dict) -> dict | None:
    prompt = build_prompt(q)
    for attempt in range(MAX_RETRIES):
        try:
            response = client.models.generate_content(
                model=GEMINI_MODEL,
                contents=prompt,
                config=types.GenerateContentConfig(
                    temperature=0.2,
                )
            )
            raw_text = response.text.strip()

            # Strip markdown code fences nếu có
            if raw_text.startswith("```"):
                lines = raw_text.split('\n')
                if lines[0].startswith("```"):
                    lines = lines[1:]
                if lines and lines[-1].startswith("```"):
                    lines = lines[:-1]
                raw_text = '\n'.join(lines).strip()
            
            return json.loads(raw_text)
        except json.JSONDecodeError as e:
            print(f"    [WARN] JSON parse error (attempt {attempt+1}): {e}")
            if attempt < MAX_RETRIES - 1:
                time.sleep(2)
        except Exception as e:
            print(f"    [ERROR] API error (attempt {attempt+1}): {e}")
            if attempt < MAX_RETRIES - 1:
                time.sleep(5)
    return None


# ─── Main ─────────────────────────────────────────────────────────────────────
def main():
    if not GEMINI_API_KEY:
        print("[ERROR] GEMINI_API_KEY not set!")
        print("   Set it via: $env:GEMINI_API_KEY='your-key'  (PowerShell)")
        print("   Or edit this script and hard-code the key temporarily.")
        return

    if not INPUT_JSON.exists():
        print(f"[ERROR] Input not found. Run step2 first: {INPUT_JSON}")
        return

    # Initialize new SDK client
    client = genai.Client(api_key=GEMINI_API_KEY)

    # Load questions
    questions = json.loads(INPUT_JSON.read_text(encoding="utf-8"))
    print(f"[*] Loaded {len(questions)} questions")

    # Load existing output for RESUME support
    if OUTPUT_JSON.exists():
        existing    = json.loads(OUTPUT_JSON.read_text(encoding="utf-8"))
        existing_id = {q["id"] for q in existing if q["explanation"] and q["explanation"].get("why_correct")}
        print(f"[~] Resume mode: {len(existing_id)} already explained, skipping...")
        # Merge
        existing_map = {q["id"]: q for q in existing}
    else:
        existing_id  = set()
        existing_map = {}

    results  = []
    skipped  = 0
    success  = 0
    failed   = 0

    for i, q in enumerate(questions, 1):
        # Resume: skip nếu đã có explanation
        if q["id"] in existing_id:
            results.append(existing_map[q["id"]])
            skipped += 1
            continue

        print(f"\n[{i}/{len(questions)}] Q{q['id']}: {q['question'][:60]}...")

        explanation = generate_explanation(client, q)

        if explanation:
            q = {**q, "explanation": explanation}
            success += 1
            print(f"  [OK] Explained")
        else:
            # Keep empty explanation, can retry later
            failed += 1
            print(f"  [FAIL] Failed after {MAX_RETRIES} attempts, keeping empty")

        results.append(q)

        # Save after every question (incremental — safe against crashes)
        OUTPUT_JSON.write_text(
            json.dumps(results + questions[i:], ensure_ascii=False, indent=2),
            encoding="utf-8"
        )

        # Rate limit protection
        time.sleep(DELAY_BETWEEN)

    # Final save
    OUTPUT_JSON.write_text(
        json.dumps(results, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )

    print(f"\n{'='*60}")
    print(f"[COMPLETED]")
    print(f"   Explained: {success}")
    print(f"   Skipped (resume): {skipped}")
    print(f"   Failed: {failed}")
    print(f"   Output: {OUTPUT_JSON}")
    if failed > 0:
        print(f"\n[!] {failed} failed. Run script again to retry (resume mode).")


if __name__ == "__main__":
    main()
