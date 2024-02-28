from typing import Tuple
from tqdm import tqdm

from main.utils.snippet import Snippet
from main.errors.error_coordinator import ErrorCoordinator
from main.utils.unmocker import unmock_code_snippet

class Moxecutor():
    def __init__(self, snippet_path: str, is_cov: bool) -> None:
        try:
            self.MAX_ITER = 25
            self.is_cov = is_cov

            self.snippet_path = snippet_path
            self.snippet_name = snippet_path.split('/')[-1]
            self.snippet = Snippet(snippet_path)

            # self.is_infinite = self.snippet.is_infinite()
            # if self.is_infinite:
            #     tqdm.write('\n\nInfinite Snippet# {}\n\n'.format(str(self.snippet_path.split('/')[-1].split('.')[0].split('snippet_')[-1])))
        except SyntaxError as e:
            self.snippet = None
            print(e)

    def moxecute(self):
        if self.snippet is not None:
            _iter = 0
            err_coord = None
            executability_report, action_iteration_report, action_progress_report, coverage_report, unresolved_report = {}, {}, {}, {}, {}
            
            tqdm.write('\nSnippet#: {}\n'.format(str(self.snippet_path.split('/')[-1].split('.')[0].split('snippet_')[-1])))
            while _iter < self.MAX_ITER: # Fix-point loop
                try:
                    out, err = None, None
                    if self.is_cov:
                        # If we are computing coverage then check output and error from the coverage wrapper to avoid having to run twice
                        # Compute coverage at the start of each iteration if is_cov flag is True
                        out, err, stmt_cov, br_cov = self.snippet.compute_timed_latest_coverage()
                        # print('\n\nOutput:\n{}'.format(out))

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
                    else:
                        # If we are not computing coverage then run snippet without coverage
                        # Execute the snippet and collect the output and error
                        out, err = self.snippet.run_timed_latest()

                    if err is None:
                        executability_report[_iter] = 'Timedout'
                        tqdm.write('\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\nSnippet#: {} -- Potentially Timed Out\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n'.format(str(self.snippet_path.split('/')[-1].split('.')[0].split('snippet_')[-1])))
                        break

                    if len(err) > 0:
                        err_coord = ErrorCoordinator(path=self.snippet.snippet_path, snippet=self.snippet, stack_trace=err)

                        # Even if the length of the error output might be >0, we might only have warnings and no actual error
                        if len(err_coord.err_type):
                            tqdm.write('\nSnippet#: {} -- Iter {} -- {}\n'.format(str(self.snippet_path.split('/')[-1].split('.')[0].split('snippet_')[-1]), str(_iter), str(err_coord.err_type) + ': ' + str(err_coord.err_msg)))
                            tqdm.write(err)

                            # Update dictionary to keep track of an action pattern's contribution to full and partial executability of the snippet. We start tracking from _iter == 1 because, at _iter == 0, no action has yet been taken. Only by _iter == 1, we have taken one action and so then we can report the impact of the action pattern that we had taken at the prior iteration, _iter-1.
                            if _iter > 0:
                                prior_action = action_iteration_report[_iter-1]
                                if prior_action not in action_progress_report:
                                    action_progress_report[prior_action] = { 'f-exec': 0, 'p-exec': 0 }
                                
                                if self.snippet.has_progress():
                                    action_progress_report[prior_action]['p-exec'] += 1
                                else:
                                    for i in range(_iter, self.MAX_ITER):
                                        executability_report[i] = err_coord.err_type
                                    break # Fix-point break

                            # Report executability
                            executability_report[_iter] = err_coord.err_type

                            # Find the appropriate action in response to the error
                            action = err_coord.find_action()
                            action_iteration_report[_iter] = type(action).__name__
                            self.snippet.add_to_action_sequence(type(action).__name__)
                            print('\n\nACTION TO APPLY: {}'.format(type(action).__name__))

                            # Carry out the action
                            if action is not None:
                                rewritten_snippet = action.apply_pattern()
                            else:
                                break
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

                            unmocked_snippet = unmock_code_snippet(self.snippet)
                            print('\nLATEST SNIPPET:\n{}\n'.format(self.snippet.get_latest()))
                            print('UNMOCKED SNIPPET:\n{}'.format(unmocked_snippet))

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
                        
                        unmocked_snippet = unmock_code_snippet(self.snippet)
                        print('\nLATEST SNIPPET:\n{}\n'.format(self.snippet.get_latest()))
                        print('UNMOCKED SNIPPET:\n{}'.format(unmocked_snippet))
                        
                        self.snippet.cleanup()
                        return executability_report, action_iteration_report, action_progress_report, len(self.snippet.action_sequence), coverage_report, unresolved_report
                
                except IndentationError as e:
                    pass
                except SyntaxError as e:
                    pass
                finally:
                    # print('\nLATEST SNIPPET:\n{}\n'.format(self.snippet.get_latest()))
                    _iter += 1
                    # unmocked_snippet = unmock_code_snippet(self.snippet.get_latest())
                    # print('UNMOCKED SNIPPET:\n{}'.format(unmocked_snippet))

            if err_coord is not None:
                unresolved_report[err_coord.err_type] = err_coord.err_msg + ' (' + self.snippet_name + ')'
            
            self.snippet.cleanup()

            return executability_report, action_iteration_report, action_progress_report, len(self.snippet.action_sequence), coverage_report, unresolved_report
        
        return None, None, None, None, None, None
            