import json
import os

INPUT_FILE = 'scripts/output/parsed_questions.json'
CHECKPOINT_FILE = 'scripts/output/enrichment_checkpoint.json'
TEMP_BATCH_FILE = 'scripts/output/temp_batch.json'

def main():
    if not os.path.exists(INPUT_FILE):
        print(f"Error: {INPUT_FILE} not found")
        return

    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        parsed = json.load(f)

    checkpoint = {}
    if os.path.exists(CHECKPOINT_FILE):
        with open(CHECKPOINT_FILE, 'r', encoding='utf-8') as f:
            checkpoint = json.load(f)

    missing = [q for q in parsed if str(q['id']) not in checkpoint]
    print(f"Total missing questions: {len(missing)}")

    # Take the first 15 missing questions
    batch = missing[:15]
    
    with open(TEMP_BATCH_FILE, 'w', encoding='utf-8') as f:
        json.dump(batch, f, ensure_ascii=False, indent=2)
    
    print(f"Saved {len(batch)} missing questions to {TEMP_BATCH_FILE}")
    print(f"IDs in this batch: {[q['id'] for q in batch]}")

if __name__ == '__main__':
    main()
