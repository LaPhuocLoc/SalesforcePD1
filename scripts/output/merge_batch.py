import json
import os
import sys

CHECKPOINT_FILE = 'scripts/output/enrichment_checkpoint.json'

def main():
    if len(sys.argv) < 2:
        print("Usage: python merge_batch.py <path_to_batch_json>")
        return

    batch_file = sys.argv[1]
    if not os.path.exists(batch_file):
        print(f"Error: {batch_file} not found")
        return

    with open(batch_file, 'r', encoding='utf-8') as f:
        new_data = json.load(f)

    checkpoint = {}
    if os.path.exists(CHECKPOINT_FILE):
        with open(CHECKPOINT_FILE, 'r', encoding='utf-8') as f:
            checkpoint = json.load(f)

    # If new_data is a list
    if isinstance(new_data, list):
        for item in new_data:
            q_id = str(item['id'])
            checkpoint[q_id] = item
    # If new_data is a dict
    elif isinstance(new_data, dict):
        for q_id, item in new_data.items():
            checkpoint[str(q_id)] = item
    
    with open(CHECKPOINT_FILE, 'w', encoding='utf-8') as f:
        json.dump(checkpoint, f, ensure_ascii=False, indent=2)

    print(f"Successfully merged data into {CHECKPOINT_FILE}. Total enriched: {len(checkpoint)}")

if __name__ == '__main__':
    main()
