import json
import os

from sklearn.metrics import precision_recall_fscore_support, accuracy_score, roc_auc_score

def eval_br_cov():
    path = '../../covs'
    # path = '../../../../LExecutor-new-data/covs'

    br_dist = {}
    br_total = 0
    br_cov = 0
    pos_counter = 0

    for file in os.listdir(path):
        with open(os.path.join(path, file), 'r') as cov_file:
            if file.startswith('snippet') and file.endswith('.json'):
                cov_json = json.load(cov_file)
                
                if cov_json['num_branches'] not in br_dist.keys():
                    br_dist[cov_json['num_branches']] = 1
                else:
                    br_dist[cov_json['num_branches']] += 1

                if cov_json['num_branches'] > 0:
                    br_total += cov_json['num_branches']
                    br_cov += cov_json['covered_branches']
                    pos_counter += 1

    print('>0 BR COV: {}'.format(br_cov/br_total))

def eval_type_pred():
    ref = None
    with open('assignments_info.json', 'r') as ref_file, open('snippets_info_chunk100_incompleter.json', 'r') as pred_file:
        ref = json.load(ref_file)
        pred = json.load(pred_file)

        refs, preds = {}, {}
        snippet_nos, vars, ref_val, lex_val, inc_val = [], [], [], [], []

        for (snippet_no, snippet_dict) in ref.items():
            if snippet_no not in refs.keys():
                refs[snippet_no] = {}
            if snippet_dict['variable'] not in refs[snippet_no].keys():
                refs[snippet_no][snippet_dict['variable']] = snippet_dict['type']

        for pred_dict in pred:
            if pred_dict['snippet_no'] not in preds.keys():
                preds[pred_dict['snippet_no']] = {}
            for (var, type_dict) in pred_dict['identifiers'].items():
                if pred_dict['snippet_no'] in refs.keys():
                    if var in refs[pred_dict['snippet_no']].keys():
                        if 'did not implement' not in type_dict['lexecutor_predicted_type'] and 'todo' not in type_dict['incompleter_predicted_type']:
                            snippet_nos.append(pred_dict['snippet_no'])
                            vars.append(var)
                            ref_val.append(refs[pred_dict['snippet_no']][var])
                            lex_val.append(type_dict['lexecutor_predicted_type'])
                            inc_val.append(type_dict['incompleter_predicted_type'])


        lex_p, lex_r, lex_f1, lex_sup = precision_recall_fscore_support(ref_val, lex_val, average='weighted')
        lex_acc = accuracy_score(ref_val, lex_val)
        # lex_auc = 

        inc_p, inc_r, inc_f1, inc_sup = precision_recall_fscore_support(ref_val, inc_val, average='weighted')
        inc_acc = accuracy_score(ref_val, inc_val)

        print('(lex_acc, lex_p, lex_r, lex_f1): ({}, {}, {}, {})\n(inc_acc, inc_p, inc_r, inc_f1): ({}, {}, {}, {})'.format(lex_acc, lex_p, lex_r, lex_f1, inc_acc, inc_p, inc_r, inc_f1))
            
        only_inc, only_lex, both, none = 0, 0, 0, 0
        for (s, v, r, l, i) in zip(snippet_nos, vars, ref_val, lex_val, inc_val):
            if r != l and r == i:
                only_inc += 1
            if r == l and r != i:
                # print('{}\t{}\t{}\t{}\t{}'.format(s, v, r, l, i))
                only_lex += 1
            if r == l and r == i:
                both += 1
            if r != l and r != i:
                print('{}\t{}\t{}\t{}\t{}'.format(s, v, r, l, i))
                if r == 'DataFrame' or r == 'ndarray':
                    none += 1

        print('\n\nTotal:{}\nOnly Incompleter:{}\nOnly Lexecutor:{}\nBoth:{}\nNone:{}\n\n'.format(len(ref_val), only_inc, only_lex, both, none))

# eval_br_cov()

eval_type_pred()