"""
Step 1: PDF → Markdown
Dùng docling DocumentConverter để convert PDF thành Markdown sạch.
Output: scripts/output/questions_raw.md
"""

from pathlib import Path
from docling.document_converter import DocumentConverter
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.datamodel.base_models import InputFormat
from docling.document_converter import PdfFormatOption

# ─── Paths ───────────────────────────────────────────────────────────────────
SCRIPT_DIR = Path(__file__).parent
PDF_PATH   = SCRIPT_DIR.parent / "docs" / "Salesforce_PD1_Questions.pdf.pdf"
OUTPUT_DIR = SCRIPT_DIR / "output"
OUTPUT_MD  = OUTPUT_DIR / "questions_raw.md"

def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    if not PDF_PATH.exists():
        raise FileNotFoundError(f"PDF not found: {PDF_PATH}")

    print(f"[*] Converting PDF: {PDF_PATH.name}")
    print("[~] Mode: text extraction only (no OCR, no table analysis - faster)...")

    # Disable OCR and heavy models - PDF is text-based, not scanned
    pipeline_options = PdfPipelineOptions()
    pipeline_options.do_ocr = False
    pipeline_options.do_table_structure = False

    converter = DocumentConverter(
        format_options={
            InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
        }
    )
    result    = converter.convert(str(PDF_PATH))

    markdown = result.document.export_to_markdown()

    OUTPUT_MD.write_text(markdown, encoding="utf-8")

    print(f"\n[OK] Done! Markdown saved to: {OUTPUT_MD}")
    print(f"   Total chars: {len(markdown):,}")
    print(f"\n[Preview] First 2000 chars:\n{'='*60}")
    print(markdown[:2000])
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
