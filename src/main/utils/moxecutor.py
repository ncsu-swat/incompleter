from typing import Tuple

from main.utils.snippet import Snippet
from main.errors.error_coordinator import ErrorCoordinator

class Moxecutor():
    def __init__(self, snippet_path: str, is_cov: bool) -> None:
        self.MAX_ITER = 11
        self.snippet_path = snippet_path
        self.snippet = Snippet(snippet_path)
        self.is_cov = is_cov
        
        self.tmp = []
        self.resolved_cases = []

    def moxecute(self):
        _iter = 0
        executability_report, coverage_report = {}, {}
        while(_iter < self.MAX_ITER):
            try:
                out, err = self.snippet.run_latest()

                if len(err) > 0:
                    e = ErrorCoordinator(path=self.snippet.snippet_path, snippet=self.snippet, stack_trace=err)
                    
                    # Even if the length of the error output might be >0, we might only have warnings and no actual error
                    if len(e.err_type):
                        # print('Iter {} -- {}\n'.format(str(_iter), str(e.err_type) + ': ' + str(e.err_msg)))
                        
                        # Report metrics
                        executability_report[_iter] = e.err_type
                        if self.is_cov:
                            stmt_cov, br_cov = self.snippet.compute_latest_coverage()
                            coverage_report[_iter] = { 'stmt': stmt_cov, 'br': br_cov }

                        # Find the appropriate action in response to the error
                        action = e.find_action()

                        # Carry out the action
                        if action is not None:
                            rewritten_snippet = action.apply_pattern()
                    else:
                        # If there are warnings but no errors, we consider the snippet fully executed
                        executability_report[_iter] = 'Fixed'
                        if self.is_cov:
                            stmt_cov, br_cov = self.snippet.compute_latest_coverage()
                            for iter_idx in range(_iter, self.MAX_ITER):
                                coverage_report[iter_idx] = { 'stmt': stmt_cov, 'br': br_cov }

                        self.resolved_cases.append(self.snippet_path.split('/')[-1].split('.')[0].split('snippet_'))
                        return executability_report, coverage_report
                else:
                    # If there are no warnings and errors, we consider the snippet fully executed
                    executability_report[_iter] = 'Fixed'
                    if self.is_cov:
                        stmt_cov, br_cov = self.snippet.compute_latest_coverage()
                        for iter_idx in range(_iter, self.MAX_ITER):
                            coverage_report[_iter] = { 'stmt': stmt_cov, 'br': br_cov }

                    self.resolved_cases.append(self.snippet_path.split('/')[-1].split('.')[0].split('snippet_'))
                    return executability_report, coverage_report
            
            except IndentationError as e:
                pass
            except SyntaxError as e:
                pass
            finally:
                _iter += 1
                # print('LATEST SNIPPET:\n{}\n'.format(self.snippet.get_latest()))

        self.snippet.cleanup()

        return executability_report, coverage_report
        