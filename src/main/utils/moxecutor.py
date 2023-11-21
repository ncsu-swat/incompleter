from typing import Tuple

from main.utils.snippet import Snippet
from main.errors.error_coordinator import ErrorCoordinator

class Moxecutor():
    def __init__(self, snippet_path: str) -> None:
        self.MAX_ITER = 10
        self.snippet_path = snippet_path
        self.snippet = Snippet(snippet_path)
        
        self.resolved_cases = []

    def moxecute(self):
        _iter = 0
        report = {}
        while(_iter < self.MAX_ITER):
            try:
                out, err = self.snippet.run_latest()

                if len(err) > 0:
                    e = ErrorCoordinator(path=self.snippet.snippet_path, snippet=self.snippet, stack_trace=err)
                    
                    # Even if the length of the error output might be >0, we might only have warnings and no actual error
                    if len(e.err_type):
                        print('Error: {}\n'.format(str(err)))
                        report[_iter] = e.err_type

                        action = e.find_action()

                        if action is not None:
                            rewritten_snippet = action.apply_pattern()
                    else:
                        report[_iter] = 'Fixed'
                        self.resolved_cases.append(self.snippet_path.split('/')[-1].split('.')[0].split('snippet_'))
                        return report
                else:
                    report[_iter] = 'Fixed'
                    self.resolved_cases.append(self.snippet_path.split('/')[-1].split('.')[0].split('snippet_'))
                    return report
            
            except IndentationError as e:
                pass
            except SyntaxError as e:
                pass
            finally:
                _iter += 1
                print('LATEST SNIPPET:\n{}\n'.format(self.snippet.get_latest()))

        self.snippet.cleanup()

        return report