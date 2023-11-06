from typing import Tuple

from main.utils.snippet import Snippet
from main.errors.error_coordinator import ErrorCoordinator

class Moxecutor():
    def __init__(self, snippet_path: str) -> None:
        self.MAX_ITER = 4
        self.snippet = Snippet(snippet_path)

    def moxecute(self):
        _iter = 0
        report = {}
        while(_iter < self.MAX_ITER):
            out, err = self.snippet.run_latest()

            if len(err) > 0:
                print('Error: {}\n'.format(str(err)))
                
                e = ErrorCoordinator(path=self.snippet.snippet_path, snippet=self.snippet, stack_trace=err)
                report[_iter] = e.err_type

                action = e.find_action()

                if action is not None:
                    rewritten_snippet = action.apply_pattern()

                    self.snippet.add(rewritten_snippet)
                    out, err = self.snippet.run_latest()
            else:
                report[_iter] = 'Fixed'
                return report

            _iter += 1
            # print('LATEST SNIPPET:\n{}\n'.format(self.snippet.get_latest()))

        self.snippet.cleanup()
        
        print('\nMocked values:\n')
        print(self.snippet.mocked_values)
        print('\nDefinition history:\n')
        print(self.snippet.def_history)

        return report