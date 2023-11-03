class Reporter():
    def __init__(self) -> None:
        self.total_count = 0
        self.error_report = {}
        self.fixed_report = {}

    def __str__(self) -> str:
        report_str = '==========================================\nTotal errors at the beginning: {}\n==========================================\n'.format(str(self.total_count))

        # Report complete executablity
        report_str += '\n==================================\nExecutablity report:\n==================================\n'
        for _iter, counts in self.fixed_report.items():
            report_str += '  Iter# {}: {} fully executed.\n'.format(_iter, counts)

        # Report partial executablity by error types
        report_str += '\n\n==================================\nError report:\n==================================\n'
        for err_type, err_counts in self.error_report.items():
            report_str += '\n  Error type: {}\n'.format(err_type)
            for _iter, counts in err_counts.items():
                report_str += '    Iter# {}: {} errors\n'.format(_iter, counts)

        return report_str

    def collect_report(self, report_by_iter: dict) -> None:
        self.total_count += 1

        for _iter, err_type in report_by_iter.items():
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
        
        # Sorring the error report
        for err_type in self.error_report.keys():
            self.error_report[err_type] = dict(sorted(self.error_report[err_type].items()))