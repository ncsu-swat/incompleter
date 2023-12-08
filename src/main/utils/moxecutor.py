from typing import Tuple
from tqdm import tqdm

from main.utils.snippet import Snippet
from main.errors.error_coordinator import ErrorCoordinator

class Moxecutor():
    def __init__(self, snippet_path: str, is_cov: bool) -> None:
        self.MAX_ITER = 20
        self.snippet_path = snippet_path
        self.snippet_name = snippet_path.split('/')[-1]
        self.snippet = Snippet(snippet_path)
        self.is_cov = is_cov

    def moxecute(self):
        _iter = 0
        err_coord = None
        executability_report, action_iteration_report, action_progress_report, coverage_report, unresolved_report = {}, {}, {}, {}, {}
        
        while True: # Fix-point loop
            try:
                # Compute coverage at the start of each iteration if is_cov flag is True
                if self.is_cov:
                    stmt_cov, br_cov = self.snippet.compute_latest_coverage()

                    if stmt_cov is not None:
                        for iter_idx in range(_iter, self.MAX_ITER):
                            if iter_idx not in coverage_report.keys():
                                coverage_report[iter_idx] = { 'stmt': 0, 'br': 0 }
                            coverage_report[iter_idx]['stmt'] = stmt_cov
                    if br_cov is not None:
                        for iter_idx in range(_iter, self.MAX_ITER):
                            if iter_idx not in coverage_report.keys():
                                coverage_report[iter_idx] = { 'stmt': 0, 'br': 0 }
                            coverage_report[iter_idx]['br'] = br_cov

                # Execute the snippet and collect the output and error
                out, err = self.snippet.run_latest()

                if len(err) > 0:
                    err_coord = ErrorCoordinator(path=self.snippet.snippet_path, snippet=self.snippet, stack_trace=err)

                    # Even if the length of the error output might be >0, we might only have warnings and no actual error
                    if len(err_coord.err_type):
                        # tqdm.write('\nSnippet#: {} -- Iter {} -- {}\n'.format(str(self.snippet_path.split('/')[-1].split('.')[0].split('snippet_')[-1]), str(_iter), str(err_coord.err_type) + ': ' + str(err_coord.err_msg)))
                        
                        # Update dictionary to keep track of an action pattern's contribution to full and partial executability of the snippet. We start tracking from _iter == 1 because, at _iter == 0, no action has yet been taken. Only by _iter == 1, we have taken one action and so then we can report the impact of the action pattern that we had taken at the prior iteration, _iter-1.
                        if _iter > 0:
                            prior_action = action_iteration_report[_iter-1]
                            if prior_action not in action_progress_report:
                                action_progress_report[prior_action] = { 'f-exec': 0, 'p-exec': 0 }
                            
                            if self.snippet.has_progress():
                                action_progress_report[prior_action]['p-exec'] += 1
                            else:
                                break # Fix-point break

                        # Report executability
                        executability_report[_iter] = err_coord.err_type

                        # Find the appropriate action in response to the error
                        action = err_coord.find_action()
                        action_iteration_report[_iter] = type(action).__name__
                        self.snippet.add_to_action_sequence(type(action).__name__)

                        # Carry out the action
                        if action is not None:
                            rewritten_snippet = action.apply_pattern()
                    else:
                        # If there are warnings but no errors, we consider the snippet fully executed
                        executability_report[_iter] = 'Fixed'

                        # After achieving full executability, we can say that all the action patterns that had been applied to this snippet, had contribution(s) towards full executability.
                        if _iter > 0:
                            prior_action = action_iteration_report[_iter-1]
                            if prior_action not in action_progress_report.keys():
                                action_progress_report[prior_action] = { 'f-exec': 0, 'p-exec': 0 }
                            action_progress_report[prior_action]['p-exec'] += 1
                            for action_name, impact_dict in action_progress_report.items():
                                action_progress_report[action_name]['f-exec'] += 1

                        self.snippet.cleanup()
                        return executability_report, action_iteration_report, action_progress_report, len(self.snippet.action_sequence), coverage_report, unresolved_report
                else:
                    # If there are no warnings and errors, we consider the snippet fully executed
                    executability_report[_iter] = 'Fixed'

                    # After achieving full executability, we can say that all the action patterns that had been applied to this snippet, had contribution(s) towards full executability.
                    if _iter > 0:
                        prior_action = action_iteration_report[_iter-1]
                        if prior_action not in action_progress_report.keys():
                            action_progress_report[prior_action] = { 'f-exec': 0, 'p-exec': 0 }
                        action_progress_report[prior_action]['p-exec'] += 1
                        for action_name, impact_dict in action_progress_report.items():
                            action_progress_report[action_name]['f-exec'] += 1 
                    
                    self.snippet.cleanup()
                    return executability_report, action_iteration_report, action_progress_report, len(self.snippet.action_sequence), coverage_report, unresolved_report
            
            except IndentationError as e:
                pass
            except SyntaxError as e:
                pass
            finally:
                # print('\nLATEST SNIPPET:\n{}\n'.format(self.snippet.get_latest()))
                _iter += 1

        if err_coord is not None:
            unresolved_report[err_coord.err_type] = err_coord.err_msg + ' (' + self.snippet_name + ')'

        self.snippet.cleanup()
        return executability_report, action_iteration_report, action_progress_report, len(self.snippet.action_sequence), coverage_report, unresolved_report
        