"""Analyze markdown to find gaps and problematic questions."""
import re
from pathlib import Path

md = Path('scripts/output/questions_raw.md').read_text(encoding='utf-8')

# Find Q23 context (no options detected)
idx = md.find('## Question 23')
if idx >= 0:
    snippet = md[idx:idx+600].encode('ascii', errors='replace').decode('ascii')
    print('=== Q23 RAW ===')
    print(snippet)
print()

# Count all question headers
headers = re.findall(r'## Question (\d+)', md, re.IGNORECASE)
nums = sorted(int(h) for h in headers)
print(f'Total question headers: {len(nums)}')

# Find gaps
all_expected = set(range(1, 201))
found = set(nums)
missing = sorted(all_expected - found)
print(f'Missing: {missing}')
print(f'Questions with no options (from step2 output):')
print('  Q23, Q54, Q108, Q124, Q130, Q134, Q136')
