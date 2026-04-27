import json
import os

def merge_explanations():
    base_dir = r"c:\Development\Antigravity\Salesforce-PD1\scripts\output"
    master_file = os.path.join(base_dir, "questions_full.json")
    
    # Load master data
    with open(master_file, 'r', encoding='utf-8') as f:
        master_data = json.load(f)
    
    # Create a mapping for quick lookup
    master_map = {q['id']: q for q in master_data}
    
    # Merge each explanation file
    for i in range(1, 12):
        explan_file = os.path.join(base_dir, f"explan_{i}.json")
        if os.path.exists(explan_file):
            print(f"Processing {explan_file}...")
            with open(explan_file, 'r', encoding='utf-8') as f:
                explan_data = json.load(f)
                
            for item in explan_data:
                q_id = item.get('id')
                if q_id in master_map:
                    master_map[q_id]['explanation'] = item.get('explanation', master_map[q_id]['explanation'])
                else:
                    print(f"Warning: ID {q_id} from {explan_file} not found in master data.")
        else:
            print(f"Warning: {explan_file} not found.")

    # Save merged data back to questions_full.json
    with open(master_file, 'w', encoding='utf-8') as f:
        json.dump(master_data, f, ensure_ascii=False, indent=2)
    
    print(f"Successfully merged all explanations into {master_file}")

if __name__ == "__main__":
    merge_explanations()
