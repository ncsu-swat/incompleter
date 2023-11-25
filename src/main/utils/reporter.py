from tabulate import tabulate

class Reporter():
    def __init__(self, is_cov: bool) -> None:
        self.total_count = 0
        self.error_report = {}
        self.fixed_report = {}
        
        self.is_cov = is_cov
        self.avg_stmt_cov = {}
        self.avg_br_cov = {}

    def __str__(self) -> str:
        report_str = '==========================================\nTotal errors at the beginning: {}\n==========================================\n\n'.format(str(self.total_count))
        report_str += '==========================================\nTABLE I. Cumulative Metrics:\n==========================================\n\n'.format(str(self.total_count))

        max_rows = max(list(self.fixed_report.keys())+list(self.avg_stmt_cov.keys())+list(self.avg_br_cov.keys()))
        table = []
        headers = ['iter#', 'exec(cnt)', 'stmt(%)', 'br(%)']

        cumm_fixed = self.fixed_report[0] if 0 in self.fixed_report.keys() else 0
        cumm_stmt = self.avg_stmt_cov[0] if 0 in self.avg_stmt_cov.keys() else 0
        cumm_br = self.avg_br_cov[0] if 0 in self.avg_br_cov.keys() else 0
        for _iter in range(1, max_rows+1):
            # Report complete executablity
            cumm_fixed += self.fixed_report[_iter] if _iter in self.fixed_report.keys() else 0
            cumm_stmt = (cumm_stmt + self.avg_stmt_cov[_iter])/2 if _iter in self.avg_stmt_cov.keys() else 0
            cumm_br = (cumm_br + self.avg_br_cov[_iter])/2 if _iter in self.avg_br_cov.keys() else 0

            row = ['Iter#{}'.format(_iter), cumm_fixed]
            if self.is_cov:
                # Report average statement coverage
                row.append(round(cumm_stmt*100))
                # Report average branch coverage
                row.append(round(cumm_br*100))
            table.append(row)
        report_str += tabulate(table, headers, tablefmt='github')

        # Report partial executablity by error types
        report_str += '\n\n==================================\nTABLE II. Error Type vs. Iteration:\n==================================\n\n'
        table = []
        headers = ['Error type'] + [str(i) for i in range(max_rows+1)]
        for err_type, err_counts in self.error_report.items():
            row = [err_type]
            for i in range(max_rows+1):
                row.append(str(err_counts[i]) if i in err_counts.keys() else 0)
            table.append(row)

        report_str += tabulate(table, headers, tablefmt='github')

        return report_str

    def collect_report(self, executability_report_by_iter: dict, coverage_report_by_iter: dict) -> None:
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

    def sort(self) -> None:
        # Sorting the complete executablity report
        self.fixed_report = dict(sorted(self.fixed_report.items()))
        
        # Sorting the error report
        for err_type in self.error_report.keys():
            self.error_report[err_type] = dict(sorted(self.error_report[err_type].items()))

    