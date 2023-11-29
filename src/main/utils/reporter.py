from tabulate import tabulate

class Reporter():
    def __init__(self, is_cov: bool) -> None:
        self.total_count = 0
        self.error_report = {}
        self.fixed_report = {}
        
        self.is_cov = is_cov
        self.avg_stmt_cov = {}
        self.avg_br_cov = {}

        self.action_iteration_report = {}
        self.action_progress_report = {}

        self.unresolved_report = {}

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

        # Report unresolved errors.
        report_str += '\n\n\n\n==================================\n TABLE V. UNRESOLVED ERRORS:\n==================================\n\n'
        for err_type, err_msgs in self.unresolved_report.items():
            report_str += '  ------------------------------------------------\n   {}s ({} count):\n  ------------------------------------------------\n'.format(err_type, len(err_msgs))
            for (idx, err_msg) in enumerate(err_msgs):
                report_str += '     {}. {}\n'.format(idx, err_msg)
            report_str += '\n'

        return report_str

    def collect_report(self, executability_report_by_iter: dict, action_report_by_iter: dict, action_report_by_progress: dict, coverage_report_by_iter: dict, unresolved_dict: dict) -> None:
        self.total_count += 1

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
            if err_type == 'Fixed':
                if _iter not in self.fixed_report.keys():
                    self.fixed_report[_iter] = 0
                self.fixed_report[_iter] += 1
            else:
                if err_type not in self.error_report.keys():
                    self.error_report[err_type] = {}
                if _iter not in self.error_report[err_type].keys():
                    self.error_report[err_type][_iter] = 0
                self.error_report[err_type][_iter] += 1

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

    