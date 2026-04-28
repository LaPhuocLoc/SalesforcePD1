import json

# Test with Q1: Application Events tuân theo mô hình...
# tuân = t u \u00e2 n
# mô = m \u00f4
# hình = h \u00ec n h

translations = {
    1: "Application Events tu\u00e2n theo m\u00f4 h\u00ecnh publish-subscribe truy\u1ec1n th\u1ed1ng. Ph\u01b0\u01a1ng th\u1ee9c n\u00e0o \u0111\u01b0\u1ee3c s\u1eed d\u1ee5ng \u0111\u1ec3 k\u00edch ho\u1ea1t (fire) m\u1ed9t event?"
}

with open('src/data/questions.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for q in data:
    if q['id'] == 1:
        q['explanation']['vi_question'] = translations[1]

with open('src/data/questions.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Test fixed Q1.")
