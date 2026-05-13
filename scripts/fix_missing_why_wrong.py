import json
import os
import time
from pathlib import Path
from google import genai
from google.genai import types

# ─── Config ──────────────────────────────────────────────────────────────────
SCRIPT_DIR  = Path(__file__).parent
PROJECT_DIR = SCRIPT_DIR.parent
QUESTIONS_JSON = PROJECT_DIR / "src" / "data" / "questions.json"

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
GEMINI_MODEL   = "gemini-flash-latest"
DELAY_BETWEEN  = 1.0
MAX_RETRIES    = 3

def build_prompt(q: dict, missing_keys: list) -> str:
    options_text = "\n".join(
        f"  {opt['key']}. {opt['text']}" for opt in q["options"]
    )
    correct_text = ", ".join(q["correct"])

    wrong_instructions = "\n".join(
        f'    "{k}": "Giải thích tại sao {k} sai..."'
        for k in missing_keys
    )

    return f"""Bạn là một Salesforce Architect lão luyện, đang giải thích câu hỏi thi Salesforce PD1 (Platform Developer 1).

---
CÂU HỎI:
{q['question']}

LỰA CHỌN:
{options_text}

ĐÁP ÁN ĐÚNG: {correct_text}
---

Lưu ý: Câu hỏi này đã có giải thích cho một số lựa chọn, nhưng đang thiếu giải thích cho các lựa chọn sai sau: {', '.join(missing_keys)}.
Hãy trả về JSON theo đúng format sau (KHÔNG thêm markdown, KHÔNG thêm text ngoài JSON), chỉ chứa giải thích cho các lựa chọn bị thiếu này:

{{
{wrong_instructions}
}}

Yêu cầu: Giải thích ngắn gọn, súc tích, đủ ý (1-2 câu). Dịch thuật ngữ kỹ thuật sang tiếng Việt nhưng giữ nguyên thuật ngữ gốc (VD: Apex, SOQL, Flow).
"""

def generate_missing_explanations(client, q: dict, missing_keys: list) -> dict | None:
    prompt = build_prompt(q, missing_keys)
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

            # Strip markdown code fences if any
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

def main():
    if not GEMINI_API_KEY:
        print("[ERROR] GEMINI_API_KEY not set!")
        print("   Vui lòng set API key trên terminal trước khi chạy:")
        print("   $env:GEMINI_API_KEY='your-key-here'")
        print("   node/python script của bạn.")
        return

    if not QUESTIONS_JSON.exists():
        print(f"[ERROR] Không tìm thấy file {QUESTIONS_JSON}")
        return

    client = genai.Client(api_key=GEMINI_API_KEY)
    questions = json.loads(QUESTIONS_JSON.read_text(encoding="utf-8"))
    
    success = 0
    skipped = 0
    failed = 0
    
    print(f"[*] Bắt đầu kiểm tra {len(questions)} câu hỏi...")
    
    for i, q in enumerate(questions):
        if not q.get("options"):
            continue
            
        option_keys = [o["key"] for o in q["options"]]
        correct_keys = q.get("correct", [])
        wrong_keys = [k for k in option_keys if k not in correct_keys]
        
        why_wrong_keys = []
        if q.get("explanation") and q["explanation"].get("why_wrong"):
            why_wrong_keys = list(q["explanation"]["why_wrong"].keys())
            
        missing_keys = [k for k in wrong_keys if k not in why_wrong_keys]
        
        if not missing_keys:
            skipped += 1
            continue
            
        print(f"\n[Q{q['id']}] Đang thiếu giải thích cho: {', '.join(missing_keys)}")
        
        if not q.get("explanation"):
            q["explanation"] = {"why_wrong": {}}
        elif not q["explanation"].get("why_wrong"):
            q["explanation"]["why_wrong"] = {}
            
        # Gọi API để lấy giải thích cho các keys bị thiếu
        new_explanations = generate_missing_explanations(client, q, missing_keys)
        
        if new_explanations:
            for k in missing_keys:
                if k in new_explanations:
                    q["explanation"]["why_wrong"][k] = new_explanations[k]
                else:
                    print(f"    [WARN] API không trả về giải thích cho {k}")
            success += 1
            print(f"  [OK] Đã bổ sung thành công")
        else:
            failed += 1
            print(f"  [FAIL] Không thể bổ sung sau {MAX_RETRIES} lần thử")
            
        # Lưu file ngay sau mỗi câu để tránh mất data
        QUESTIONS_JSON.write_text(
            json.dumps(questions, ensure_ascii=False, indent=2),
            encoding="utf-8"
        )
        time.sleep(DELAY_BETWEEN)

    print(f"\n{'='*60}")
    print(f"[HOÀN THÀNH]")
    print(f"   Đã bổ sung: {success} câu hỏi")
    print(f"   Bỏ qua (đã đủ): {skipped} câu hỏi")
    print(f"   Thất bại: {failed} câu hỏi")

if __name__ == "__main__":
    main()
