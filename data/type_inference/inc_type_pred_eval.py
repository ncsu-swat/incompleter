import json

refs = {}
preds = {}
match_counter = 0
total_counter = 0
other_counter = 0
success = set()

with open('snippets_info_chunk100_incompleter.json') as pred_file, open('../new_all/ground_truth_dataset/assignment_removed/assignments_info.json') as ref_file:
    pred = json.load(pred_file)
    ref = json.load(ref_file)

    for (ref_no, ref_dict) in ref.items():
        refs[ref_no] = {
            ref_dict["variable"]: ref_dict["type"]
        }

    for pred_dict in pred:
        preds_key = pred_dict['snippet_no']
        for (ident, ident_dict) in pred_dict['identifiers'].items():
            if ident in list(refs[preds_key].keys()):
                total_counter += 1
                if refs[preds_key][ident] == ident_dict['incompleter_predicted_type']:
                    match_counter += 1
                    success.add(preds_key + '-' + ident)

    print('Match Acc: {}'.format((match_counter+other_counter)/total_counter))
    print(success)