import json

refs = {}
preds = {}
match_counter = 0
total_counter = 0

with open('snippets_info_chunk100.json') as pred_file, open('../new_all/assignment_removed/assignments_info.json') as ref_file:
    pred = json.load(pred_file)
    ref = json.load(ref_file)

    for ref_dict in ref:
        refs_key = ref_dict['snippet_name'].split('_')[1]+"_"+ref_dict['snippet_name'].split('_')[2].split('.')[0]
        refs[refs_key] = {
            ref_dict["variable"]: ref_dict["type"]
        }

    for pred_dict in pred:
        preds_key = pred_dict['snippet_no']
        for (ident, ident_dict) in pred_dict['identifiers'].items():
            if ident in list(refs[preds_key].keys()):
                total_counter += 1
                if refs[preds_key][ident] == ident_dict['lexecutor_predicted_type']:
                    match_counter += 1
                elif ident_dict['lexecutor_predicted_type'] == 'object':
                    match_counter += 1

    print('Match Acc: {}'.format(match_counter/total_counter))