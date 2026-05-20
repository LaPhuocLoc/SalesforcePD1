import json

def analyze():
    filepath = 'scripts/output/enriched_questions.json'
    with open(filepath, 'r', encoding='utf-8') as f:
        questions = json.load(f)
        
    print(f"Total questions: {len(questions)}")
    
    incompletes = []
    
    for q in questions:
        qid = q.get('id')
        qnum = q.get('original_num')
        correct = q.get('correct', [])
        options = q.get('options', [])
        
        # Get all keys in options
        all_option_keys = [opt['key'] for opt in options]
        # Incorrect option keys should be all options that are not correct
        incorrect_option_keys = sorted([k for k in all_option_keys if k not in correct])
        
        explanation = q.get('explanation')
        if not explanation:
            incompletes.append({
                'id': qid,
                'num': qnum,
                'reason': 'No explanation object',
                'correct': correct,
                'incorrect_keys': incorrect_option_keys,
                'current_why_wrong_keys': [],
                'missing_keys': incorrect_option_keys,
                'extra_keys': []
            })
            continue
            
        why_wrong = explanation.get('why_wrong')
        if why_wrong is None:
            incompletes.append({
                'id': qid,
                'num': qnum,
                'reason': 'why_wrong is None',
                'correct': correct,
                'incorrect_keys': incorrect_option_keys,
                'current_why_wrong_keys': [],
                'missing_keys': incorrect_option_keys,
                'extra_keys': []
            })
            continue
            
        if not isinstance(why_wrong, dict):
            incompletes.append({
                'id': qid,
                'num': qnum,
                'reason': f'why_wrong is not a dict (type: {type(why_wrong)})',
                'correct': correct,
                'incorrect_keys': incorrect_option_keys,
                'current_why_wrong_keys': [],
                'missing_keys': incorrect_option_keys,
                'extra_keys': []
            })
            continue
            
        # Check if all incorrect option keys are explained, and no correct/invalid keys are explained
        why_wrong_keys = sorted(list(why_wrong.keys()))
        missing_keys = [k for k in incorrect_option_keys if k not in why_wrong_keys]
        extra_keys = [k for k in why_wrong_keys if k not in incorrect_option_keys]
        
        if missing_keys or extra_keys:
            incompletes.append({
                'id': qid,
                'num': qnum,
                'reason': f'Keys mismatch. Missing: {missing_keys}, Extra: {extra_keys}',
                'correct': correct,
                'incorrect_keys': incorrect_option_keys,
                'current_why_wrong_keys': why_wrong_keys,
                'missing_keys': missing_keys,
                'extra_keys': extra_keys
            })
            
    print(f"Total incomplete/mismatched questions: {len(incompletes)}")
    for idx, inc in enumerate(incompletes[:20]):
        print(f"  {idx+1}. ID {inc['id']} (Num {inc['num']}): {inc['reason']}")
    if len(incompletes) > 20:
        print(f"  ... and {len(incompletes) - 20} more.")
        
    # Write full analysis to a temporary file
    with open('scripts/output/missing_explanations_report.json', 'w', encoding='utf-8') as f:
        json.dump(incompletes, f, ensure_ascii=False, indent=2)
    print("Full report written to scripts/output/missing_explanations_report.json")

if __name__ == '__main__':
    analyze()
