"""
Deep investigation: WHY are there 251 mismatches?
Check:
1. Are there multiple questions with the same original_num (from different sets)?
2. Is the MD parser reading wrong answers?
"""
import json, re

# Check duplicate original_num in JSON
with open('src/data/questions_enhanced.json', 'r', encoding='utf-8') as f:
    json_qs = json.load(f)

# Count original_num distribution
from collections import Counter
num_counts = Counter(q.get('original_num') for q in json_qs)
duplicates = {k:v for k,v in num_counts.items() if v > 1}
print(f"Total JSON questions: {len(json_qs)}")
print(f"Unique original_num values: {len(num_counts)}")
print(f"original_num values with duplicates: {len(duplicates)}")
print(f"Duplicate nums: {sorted(duplicates.items())[:20]}")

# Also check: what is the range of original_num?
nums = sorted(q.get('original_num',0) for q in json_qs)
print(f"\noriginal_num range: {nums[0]} to {nums[-1]}")

# Check: do questions have a 'set' field?
sets = set(q.get('set','') for q in json_qs)
print(f"\nSets present: {sets}")

# Show some questions with duplicate nums
print("\nSample questions with same original_num:")
from collections import defaultdict
by_num = defaultdict(list)
for q in json_qs:
    by_num[q.get('original_num')].append(q)

for num, qs in sorted(by_num.items()):
    if len(qs) > 1 and num and num <= 10:
        print(f"\n  original_num={num} ({len(qs)} questions):")
        for q in qs:
            print(f"    ID={q['id']} correct={q['correct']} Q={q['question'][:60]}...")
