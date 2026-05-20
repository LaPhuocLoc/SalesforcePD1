# Salesforce PD1 - Enrichment Pipeline

## Tổng quan

Pipeline này xử lý 349 câu hỏi từ `docs/SF Developer 1_All_Question.md` và bổ sung:
1. **vi_question** - Dịch câu hỏi sang tiếng Việt (giữ nguyên thuật ngữ kỹ thuật)
2. **why_correct** - Giải thích tại sao đáp án đúng là đúng
3. **why_wrong** - Giải thích từng đáp án sai tại sao sai
4. **tip** - Từ khóa ghi nhớ ngắn gọn

## File structure

```
scripts/
├── parse_md_questions.py       # Bước 1: Parse MD → JSON
├── enrich_questions.py         # Bước 2: Enrich với Gemini API (full run)
├── test_enrich_10.py           # Test với 10 câu đầu
├── generate_enhanced_md.py     # Bước 3: JSON → MD đẹp
└── output/
    ├── parsed_questions.json       # Output bước 1
    ├── enrichment_checkpoint.json  # Checkpoint (tự tạo khi chạy)
    ├── enriched_questions.json     # Output bước 2
    └── SF Developer 1_All_Question_ENHANCED.md  # Output cuối
```

## Cách chạy

### Bước 0: Lấy Gemini API Key
1. Vào https://aistudio.google.com/app/apikey
2. Tạo API key mới (miễn phí với gemini-2.0-flash)

### Bước 1: Parse MD (đã xong)
```powershell
python scripts/parse_md_questions.py
```
→ Tạo `scripts/output/parsed_questions.json` (349 câu)

### Bước 2: Test với 10 câu (khuyến nghị trước)
```powershell
$env:GEMINI_API_KEY = "YOUR_API_KEY_HERE"
python scripts/test_enrich_10.py
```

### Bước 3: Chạy full enrichment
```powershell
$env:GEMINI_API_KEY = "YOUR_API_KEY_HERE"
python scripts/enrich_questions.py
```
- Có checkpoint: nếu bị ngắt, chạy lại sẽ tiếp tục từ chỗ dở
- ~70 batch × 5 câu = ~70 lần gọi API
- Thời gian ước tính: ~5-10 phút

### Bước 4: Generate MD đẹp
```powershell
python scripts/generate_enhanced_md.py
```
→ Tạo `docs/SF Developer 1_All_Question_ENHANCED.md`

## Thống kê

- Tổng câu: **349**
- Câu có options checkbox: **338**
- Câu có explanation tiếng Anh: **299**
- Câu code-block format (chưa parse được options): **11**

## Ước tính chi phí Gemini API

Với `gemini-2.0-flash`:
- Input: ~349 câu × ~500 tokens ≈ 174,500 tokens
- Output: ~349 câu × ~200 tokens ≈ 69,800 tokens  
- Gemini Flash miễn phí với quota 15 RPM, 1M tokens/ngày
- **Hoàn toàn miễn phí** nếu dùng free tier
