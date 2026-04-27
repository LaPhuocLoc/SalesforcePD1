# Salesforce PD1 Exam Prep App — Design Document

> **Version:** 1.0 | **Date:** 2026-04-24 | **Status:** Confirmed ✅

---

## 1. Understanding Summary

| # | Item | Decision |
|---|------|----------|
| 1 | **What** | Web app ôn thi Salesforce PD1 — 200 câu hỏi, 2 chế độ học |
| 2 | **Why** | Ôn thi cá nhân, cần giải thích sâu theo phong cách Salesforce Architect |
| 3 | **Who** | Single user — chỉ bản thân người build |
| 4 | **Platform** | Responsive web, mobile-first (iOS Safari / Chrome) + PC |
| 5 | **Constraints** | Không có login, cross-device sync, no database (Vercel KV) |
| 6 | **Non-goals** | Không multi-user, không auth, không admin UI, không chia sẻ kết quả |

---

## 2. Assumptions

- ⚠️ Vercel KV (Redis free tier) dùng để lưu tiến độ ôn tập — free ~30MB, đủ cho 200 câu
- Câu hỏi được embed tĩnh vào app dưới dạng `questions_full.json` (không fetch từ API ngoài)
- AI generate explanation 1 lần duy nhất trước khi build app
- Không cần lưu lịch sử nhiều lần thi — chỉ lưu tiến độ lần ôn tập gần nhất
- Deploy trên Vercel free tier là đủ

---

## 3. Decision Log

| # | Quyết định | Lựa chọn bị loại | Lý do chọn |
|---|-----------|-----------------|-----------|
| 1 | Platform: Responsive web | Mobile app native | Không cần cài app, truy cập ngay qua browser |
| 2 | Single user | Multi-user | App chỉ dùng cho 1 người, đơn giản hóa hoàn toàn |
| 3 | Progress: Vercel KV | localStorage | localStorage mất data khi đổi thiết bị; Vercel KV sync cross-device |
| 4 | Data: JSON tĩnh | Database | 200 câu là tập cố định, không cần query động |
| 5 | Explanation: Pre-generated | AI real-time | Zero runtime cost, nhanh hơn, có thể review trước |
| 6 | Review: VS Code | Admin UI | Đơn giản nhất cho single user, không cần build thêm tool |
| 7 | Tech: Next.js 15 | Vite + React | Full-stack trong 1 project, API routes cho Vercel KV |
| 8 | Design: "Night Mode" Dark Focus | Exam Room / SF Blueprint | Tối giản, bảo vệ mắt khi học đêm, high contrast |

---

## 4. Feature Specification

### 4.1 Chế độ Thi Thử (Exam Mode)

- **Câu hỏi:** 65 câu random từ pool 200 câu
- **Thời gian:** Đếm ngược 105 phút (hiển thị realtime)
- **Trong lúc thi:**
  - Navigation: Prev / Next / Flag (đánh dấu câu chưa chắc)
  - Không có nút "Xem đáp án"
  - Progress bar hiển thị số câu đã làm / tổng
- **Khi nộp bài (hoặc hết giờ):**
  - Hiển thị: Điểm số, Pass/Fail (ngưỡng 65%)
  - Review toàn bộ 65 câu với đáp án + explanation
  - Thống kê: câu đúng/sai, % per topic (nếu câu hỏi có tag topic)

### 4.2 Chế độ Ôn Tập (Study Mode)

#### 4.2.1 Ôn từ đầu (Fresh Start)
- Reset toàn bộ progress về 0
- Bắt đầu từ câu 1 → 200
- Không lưu lựa chọn cũ

#### 4.2.2 Ôn tiếp (Continue)
- Load tiến độ từ Vercel KV
- Tiếp tục từ câu cuối cùng đã làm
- Lưu lại lựa chọn và trạng thái từng câu

### 4.3 Màn hình câu hỏi (shared giữa 2 mode)

**Buttons:**
| Nút | Hành động |
|-----|-----------|
| ← Trước | Câu trước |
| Sau → | Câu tiếp theo |
| Xem đáp án | Hiện explanation panel (chỉ Study Mode) |
| Tiếp tục | Lưu + sang câu tiếp (Study Mode) / Next (Exam Mode) |

**Explanation Panel (khi nhấn "Xem đáp án"):**
```
📌 Đáp án đúng: [A, C]
📝 Bản dịch: [Vietnamese translation]
✅ Tại sao đúng: [Analysis]
❌ Tại sao sai: [Per wrong option]
💡 Mẹo ghi nhớ: [Key takeaway]
```

---

## 5. Data Schema

### questions_full.json

```json
[
  {
    "id": 1,
    "question": "Which of the following...",
    "options": [
      { "key": "A", "text": "Option A text" },
      { "key": "B", "text": "Option B text" },
      { "key": "C", "text": "Option C text" },
      { "key": "D", "text": "Option D text" }
    ],
    "correct": ["A"],
    "type": "single",
    "topic": "Apex Basics",
    "explanation": {
      "vi_question": "Câu hỏi dịch tiếng Việt...",
      "why_correct": "A đúng vì...",
      "why_wrong": {
        "B": "B sai vì...",
        "C": "C sai vì...",
        "D": "D sai vì..."
      },
      "tip": "Mẹo ghi nhớ: ..."
    }
  }
]
```

### Vercel KV — Progress Schema

```json
{
  "study_progress": {
    "current_index": 42,
    "answers": {
      "1": ["A"],
      "2": ["B", "C"],
      "3": null
    },
    "last_updated": "2026-04-24T21:00:00Z"
  }
}
```

---

## 6. Design System — "Night Mode" Dark Focus

### Color Palette

```css
--bg-primary:    #000000;   /* Pure black */
--bg-surface:    #0D0D0D;   /* Cards */
--bg-elevated:   #1A1A1A;   /* Elevated elements */
--border:        #1F2937;   /* Subtle borders */

--accent-cyan:   #00F5FF;   /* Primary CTA, highlights */
--accent-violet: #7C3AED;   /* Secondary, correct answers */
--accent-glow:   #00F5FF33; /* Glow effect */

--text-primary:  #FFFFFF;
--text-secondary:#A1A1AA;
--text-muted:    #4B5563;

--success:       #22C55E;   /* Correct */
--error:         #EF4444;   /* Wrong */
--warning:       #F59E0B;   /* Timer warning */
```

### Typography

```css
--font-display: 'Space Grotesk', sans-serif;  /* Headers, question text */
--font-body:    'DM Sans', sans-serif;         /* Options, explanations */
--font-mono:    'JetBrains Mono', monospace;  /* Code snippets in Apex questions */
```

### Motion Philosophy

- **Sparse + purposeful** — không spam animation
- **One strong entrance:** question card slide-in từ phải khi chuyển câu
- **Hover states:** subtle cyan glow trên answer options
- **Timer:** pulse đỏ khi còn < 10 phút
- **Explanation panel:** smooth expand từ dưới lên

### Mobile Touch Rules (min 44px touch targets)

- Answer option height: tối thiểu 52px (padding đủ)
- Nav buttons: full-width trên mobile, fixed bottom bar
- Timer: sticky top header

---

## 7. Architecture

```
src/
├── app/
│   ├── page.tsx                  # Home — chọn chế độ
│   ├── exam/
│   │   ├── page.tsx              # Exam mode — 65 câu
│   │   └── results/page.tsx      # Kết quả + thống kê
│   ├── study/
│   │   └── page.tsx              # Study mode — 200 câu
│   └── api/
│       └── progress/
│           ├── route.ts          # GET /api/progress
│           └── route.ts          # POST /api/progress
├── components/
│   ├── question/
│   │   ├── QuestionCard.tsx
│   │   ├── AnswerOption.tsx
│   │   └── ExplanationPanel.tsx
│   ├── exam/
│   │   ├── Timer.tsx
│   │   ├── ProgressBar.tsx
│   │   └── ResultsSummary.tsx
│   ├── study/
│   │   └── StudyNav.tsx
│   └── ui/
│       ├── Button.tsx
│       └── Badge.tsx
├── data/
│   └── questions_full.json       # Static data
├── lib/
│   ├── kv.ts                     # Vercel KV client
│   ├── questions.ts              # Question utilities (shuffle, filter)
│   └── scoring.ts                # Exam scoring logic
└── styles/
    └── globals.css               # Design system tokens
```
