from typing import Tuple

from main.utils.snippet import Snippet
from main.errors.error import _Error

class Moxecutor():
    def __init__(self, snippet_path: str) -> None:
        self.LIFETIME = 4
        self.snippet = Snippet(snippet_path)

    def moxecute(self):
        epoch = 0
        report = {}
        while(epoch < self.LIFETIME):
            out, err = self.snippet.run_latest()

            # print('Error: {}\n'.format(str(err)))

            if len(err) > 0:
                epoch += 1
                e = _Error(path=self.snippet.snippet_path, snippet=self.snippet, stack_trace=err)
                report[epoch] = e.err_type

                ActionClass, kwargs = e.find_action_class()

                if ActionClass is not None and kwargs is not None:
                    action = ActionClass(snippet=self.snippet, lineno=e.lineno, **kwargs)
                    rewritten_snippet = action.apply_pattern()

                    self.snippet.add(rewritten_snippet)
                    out, err = self.snippet.run_latest()

            # print('LATEST SNIPPET:\n{}\n'.format(self.snippet.get_latest()))

            if len(err) == 0:
                report[epoch] = 'Fixed'
                return report

        return report