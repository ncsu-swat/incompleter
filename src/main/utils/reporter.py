from tabulate import tabulate

from matplotlib_venn import venn2
from matplotlib import pyplot as plt

class Reporter():
    lexecutor_success = set(['24', '224', '350', '340', '589', '618', '14', '71', '271', '321', '30', '292', '679', '668', '639', '15', '177', '355', '392', '231', '382', '60', '629', '678', '718', '749', '351', '211', '190', '341', '759', '708', '499', '445', '713', '593', '746', '657', '723', '632', '501', '400', '434', '804', '756', '587', '389', '607', '565', '780', '681', '541', '646', '586', '159', '299', '777', '652', '561', '571', '582', '685', '138', '426', '692', '770', '682', '453', '38', '416', '665', '711', '490', '750', '797', '359', '786', '446', '775', '650', '813', '710', '481', '491', '700', '462', '516', '687', '209', '369', '817', '413', '823', '792', '452', '239', '268', '39', '698', '80', '362', '140', '381', '150', '317', '206', '688', '479', '115', '303', '12', '121', '313', '36', '105', '267', '478', '353', '130', '95', '237', '175', '291', '62', '151', '233', '322', '134', '316', '196'])

    def __init__(self, is_cov: bool) -> None:
        self.total_count = 0
        self.fexec_count = 0
        self.pexec_count = 0

        self.error_report = {}
        self.fixed_report = {}
        
        self.is_cov = is_cov
        self.avg_stmt_cov = {}
        self.avg_br_cov = {}

        self.action_iteration_report = {}
        self.action_progress_report = {}
        self.total_action_sequence_length = 0
        self.fexec_action_sequence_length = 0
        self.pexec_action_sequence_length = 0

        self.unresolved_report = {}
        
        # Attributes for Venn Diagram
        self.all_cases = set()
        self.resolved_cases = set()
        
        self.only_lexecutor = set()
        self.only_incompleter = set()
        self.common = set()
        self.none = set()

        self.only_lexecutor_perc = 0
        self.only_incompleter_perc = 0
        self.common_perc = 0
        self.none_perc = 0

        print()

    def __str__(self) -> str:
        report_str = '\n\n==========================================\n Total errors at the beginning: {}\n==========================================\n\n'.format(str(self.total_count))
        report_str += '\n\n==========================================\n TABLE I. Cumulative Metrics:\n==========================================\n\n'.format(str(self.total_count))
        report_str += 'This table shows a cumulative measure of full executability, statement coverage, and branch coverage from one iteration to the next.\n\n'

        max_rows = max(list(self.fixed_report.keys())+list(self.avg_stmt_cov.keys())+list(self.avg_br_cov.keys()))
        table = []
        headers = ['iter#', 'exec(cnt)', 'stmt(%)', 'br(%)']

        cumm_fixed = self.fixed_report[0] if 0 in self.fixed_report.keys() else 0
        cumm_stmt = self.avg_stmt_cov[0] if 0 in self.avg_stmt_cov.keys() else 0
        cumm_br = self.avg_br_cov[0] if 0 in self.avg_br_cov.keys() else 0
        for _iter in range(1, max_rows+1):
            # Report complete executablity
            cumm_fixed += self.fixed_report[_iter] if _iter in self.fixed_report.keys() else 0
            cumm_stmt = (cumm_stmt + self.avg_stmt_cov[_iter])/2 if _iter in self.avg_stmt_cov.keys() else cumm_stmt
            cumm_br = (cumm_br + self.avg_br_cov[_iter])/2 if _iter in self.avg_br_cov.keys() else cumm_br

            row = ['Iter#{}'.format(_iter), cumm_fixed]
            if self.is_cov:
                # Report average statement coverage
                row.append(round(cumm_stmt*100))
                # Report average branch coverage
                row.append(round(cumm_br*100))
            table.append(row)
        report_str += tabulate(table, headers, tablefmt='github')

        # Report error type count by iteration
        report_str += '\n\n\n\n====================================\n TABLE II. Error Type vs. Iteration:\n====================================\n\n'
        report_str += 'This table shows a list of error types and the number of times they occur at each iteration. This table shows the gradual resolution of certain error types and the gradual appearance of others. The gradual appearance of other error types can be attributed to side-effects from some prior applied action pattern. Or, if an action pattern was able to execute a previously erroneous statement, other error types could originate from the following statements in the code.\n\n'
        table = []
        headers = ['error-type'] + [str(i) for i in range(max_rows+1)]
        for err_type, err_counts in self.error_report.items():
            row = [err_type]
            for i in range(max_rows+1):
                row.append(str(err_counts[i]) if i in err_counts.keys() else 0)
            table.append(row)
        report_str += tabulate(table, headers, tablefmt='github')

        # Report applied action pattern count by iteration
        report_str += '\n\n\n\n=========================================\n TABLE III. Action Pattern vs. Iteration:\n=========================================\n\n'
        report_str += 'This table shows a list of action patterns and the number of times they had been applied at each iteration. This metric could be a proxy for the impact of an action pattern since an action pattern is likely to be impactful if it has been applied a large number of times.\n\n'
        table = []
        headers = ['action-pattern'] + [str(i) for i in range(max_rows+1)]
        for action_pattern, action_counts in self.action_iteration_report.items():
            row = [action_pattern]
            for i in range(max_rows+1):
                row.append(str(action_counts[i]) if i in action_counts.keys() else 0)
            table.append(row)
        report_str += tabulate(table, headers, tablefmt='github')

        # Report impact of each action pattern. Count how many times an action pattern was part of an action sequence that made a snippet fully executable (f-exec) and count how many times an action pattern helped a snippet's execution to progress beyond its corresponding error.
        report_str += '\n\n\n\n==================================\n TABLE IV. Action Pattern Impact:\n==================================\n\n'
        report_str += 'This table shows the impact of each action pattern. The column f-exec represents the number of snippets where a certain action pattern contributed towards full executability. Let\'s define an action sequence as the sequence of action patterns that had been applied to a snippet. If a certain action pattern was part of the action sequence for a fully executable sequence, we increment f-exec by 1 (regardless of how many times the action pattern appears in the action sequence). On the other hand, p-exec (partial executability) represents the number of times a certain action pattern advanced the execution beyond a previously erroneous statement. However, p-exec has no association with full executability.\n\n'
        table = []
        headers = ['action-pattern', 'f-exec', 'p-exec']
        for action_pattern, impact_dict in self.action_progress_report.items():
            row = [action_pattern, self.action_progress_report[action_pattern]['f-exec'], self.action_progress_report[action_pattern]['p-exec']]
            table.append(row)
        report_str += tabulate(table, headers, tablefmt='github')

        # Report average action sequence lengths
        report_str += '\n\n\n\n==================================\n TABLE V. Action Sequence Length:\n==================================\n\n'
        report_str += 'This table shows the average action sequence length for different sets of snippets. The row for the total set represents the average length of action sequences for all snippets. The row for fexec set represents the average action sequence length for snippets that were fully executed. The row for pexec set represents the average action sequence length for snippets that were partially executed.\n\n'
        table = []
        headers = ['set', 'avg-action-seq-len']
        if self.total_count > 0:
            table.append(['total', '{} actions'.format(int(self.total_action_sequence_length/self.total_count))])
            
            if self.fexec_count == 0: table.append(['f-exec', '0 actions'])
            else: table.append(['f-exec', '{} actions'.format(int(self.fexec_action_sequence_length/self.fexec_count))])
            
            if self.pexec_count == 0: table.append(['p-exec', '0 actions'])
            else: table.append(['p-exec', '{} actions'.format(int(self.pexec_action_sequence_length/self.pexec_count))])
        
            report_str += tabulate(table, headers, tablefmt='github')

        # Report unresolved errors.
        report_str += '\n\n\n\n==================================\n TABLE VI. UNRESOLVED ERRORS:\n==================================\n\n'
        for err_type, err_msgs in self.unresolved_report.items():
            report_str += '  ------------------------------------------------\n   {}s ({} count):\n  ------------------------------------------------\n'.format(err_type, len(err_msgs))
            for (idx, err_msg) in enumerate(err_msgs):
                report_str += '     {}. {}\n'.format(idx, err_msg)
            report_str += '\n'

        # Report Venn diagram statistics
        if self.only_lexecutor is not None and self.only_incompleter is not None and self.common is not None and self.none is not None:
            report_str += '\n\n\n\n==================================\n TABLE VII. VENN DIAGRAM STATISTICS:\n==================================\n\n'
            report_str += 'This table shows the venn diagram statistics between LExecutor and incompleter.\n\n'
            table = []
            headers = ['Set', 'snippet_cnt(%)']
            
            table.append(['(only) lexecutor', self.only_lexecutor_perc])
            table.append(['(only) incompleter', self.only_incompleter_perc])
            table.append(['(both) common', self.common_perc])
            table.append(['(none) unsolved', self.none_perc])

            report_str += tabulate(table, headers, tablefmt='github')

            report_str += '\n\n\n\n  ----------------------------\n   Only LExecutor\n  ----------------------------\n\n   '
            report_str += str(self.only_lexecutor)
            report_str += '\n\n  ----------------------------\n   Only Incompleter\n  ----------------------------\n\n   '
            report_str += str(self.only_incompleter)
            report_str += '\n\n  ----------------------------\n   Common\n  ----------------------------\n\n   '
            report_str += str(self.common)
            report_str += '\n\n  ----------------------------\n   None\n  ----------------------------\n\n   '
            report_str += str(self.none)
            report_str += '\n\n'

        return report_str

    def collect_report(self, file_name: str, executability_report_by_iter: dict, action_report_by_iter: dict, action_report_by_progress: dict, action_sequence_length: int, coverage_report_by_iter: dict, unresolved_dict: dict) -> None:
        snippet_number = file_name.split('/')[-1].split('.')[0].split('snippet_')[-1]
        self.total_count += 1
        self.total_action_sequence_length += action_sequence_length
        self.is_fixed = False

        if self.is_cov:
            for _iter, covs in coverage_report_by_iter.items():
                if covs['stmt'] is not None:
                    if _iter not in self.avg_stmt_cov.keys():
                        self.avg_stmt_cov[_iter] = covs['stmt']
                    else:
                        self.avg_stmt_cov[_iter] = (self.avg_stmt_cov[_iter] + covs['stmt'])/2

                if covs['br'] is not None:
                    if _iter not in self.avg_br_cov.keys():
                        self.avg_br_cov[_iter] = covs['br']
                    else:
                        self.avg_br_cov[_iter] = (self.avg_br_cov[_iter] + covs['br'])/2

        for _iter, err_type in executability_report_by_iter.items():
            self.all_cases.add(snippet_number)
            if err_type == 'Fixed':
                self.resolved_cases.add(snippet_number)
                self.is_fixed = True
                if _iter not in self.fixed_report.keys():
                    self.fixed_report[_iter] = 0
                self.fixed_report[_iter] += 1
            else:
                if err_type not in self.error_report.keys():
                    self.error_report[err_type] = {}
                if _iter not in self.error_report[err_type].keys():
                    self.error_report[err_type][_iter] = 0
                self.error_report[err_type][_iter] += 1

        if self.is_fixed:
            self.fexec_action_sequence_length += action_sequence_length
            self.fexec_count += 1
        else:
            self.pexec_action_sequence_length += action_sequence_length
            self.pexec_count += 1

        for _iter, action_pattern in action_report_by_iter.items():
            if action_pattern not in self.action_iteration_report.keys():
                self.action_iteration_report[action_pattern] = {}
            if _iter not in self.action_iteration_report[action_pattern].keys():
                self.action_iteration_report[action_pattern][_iter] = 0
            self.action_iteration_report[action_pattern][_iter] += 1

        for action_pattern, impact_dict in action_report_by_progress.items():
            if action_pattern not in self.action_progress_report.keys():
                self.action_progress_report[action_pattern] = { 'f-exec': 0, 'p-exec': 0 }
            self.action_progress_report[action_pattern]['f-exec'] += impact_dict['f-exec']
            self.action_progress_report[action_pattern]['p-exec'] += impact_dict['p-exec']

        for err_type, err_msg in unresolved_dict.items():
            if err_type not in self.unresolved_report.keys():
                self.unresolved_report[err_type] = []
            self.unresolved_report[err_type].append(err_msg)

    def sort(self) -> None:
        # Sorting the complete executablity report
        self.fixed_report = dict(sorted(self.fixed_report.items()))
        
        # Sorting the error report
        for err_type in self.error_report.keys():
            self.error_report[err_type] = dict(sorted(self.error_report[err_type].items()))

    def compute_venn(self) -> None:
        self.only_lexecutor = set()
        self.only_incompleter = set()
        self.common = set()
        self.none = set()

        self.common = self.resolved_cases.intersection(Reporter.lexecutor_success)
        self.only_lexecutor = Reporter.lexecutor_success.difference(self.common)
        self.only_incompleter = self.resolved_cases.difference(self.common)
        self.none = self.all_cases.difference(self.common.union(self.only_lexecutor, self.only_incompleter))
    
        self.only_lexecutor_perc = round(len(self.only_lexecutor)/self.total_count, 2)
        self.only_incompleter_perc = round(len(self.only_incompleter)/self.total_count, 2)
        self.common_perc = round(len(self.common)/self.total_count, 2)
        self.none_perc = round(len(self.none)/self.total_count, 2)