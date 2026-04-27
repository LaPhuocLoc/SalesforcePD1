"""
Step 1: PDF → Text using pdfplumber
Extract text from PDF reliably without memory issues.
Output: scripts/output/questions_raw.txt
"""

import pdfplumber
from pathlib import Path

# ─── Paths ───────────────────────────────────────────────────────────────────
SCRIPT_DIR = Path(__file__).parent
PDF_PATH   = SCRIPT_DIR.parent / "docs" / "Salesforce_PD1_Questions.pdf.pdf"
OUTPUT_DIR = SCRIPT_DIR / "output"
OUTPUT_TXT = OUTPUT_DIR / "questions_raw.txt"

def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    if not PDF_PATH.exists():
        raise FileNotFoundError(f"PDF not found: {PDF_PATH}")

    print(f"[*] Extracting text from PDF: {PDF_PATH.name}")

    full_text = []
    with pdfplumber.open(str(PDF_PATH)) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                full_text.append(text)

    # Join pages
    final_text = "\n\n".join(full_text)

    OUTPUT_TXT.write_text(final_text, encoding="utf-8")

    print(f"\n[OK] Done! Text saved to: {OUTPUT_TXT}")
    print(f"   Total chars: {len(final_text):,}")
    print(f"\n[Preview] First 1000 chars:\n{'='*60}")
    print(final_text[:1000])
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
