from typing import Tuple

from main.utils.snippet import Snippet
from main.errors.error import Error

class Moxecutor():
    def __init__(self, snippet_path: str) -> None:
        self.LIFETIME = 2
        self.snippet = Snippet(snippet_path)

    def moxecute(self) -> Tuple[bool, int]:
        epoch = 0
        while(epoch < self.LIFETIME):
            out, err = self.snippet.run(epoch)
            
            if len(err) > 0:
                epoch += 1
                e = Error(path=self.snippet.snippet_path, stack_trace=err)

                kwargs, Action_Class = e.find_action_class()

                if kwargs != None and Action_Class != None:
                    action = Action_Class(snippet=self.snippet, lineno=e.lineno, **kwargs)
                    rewritten_snippet = action.apply_pattern()

                    self.snippet.code.append(rewritten_snippet)
                    out, err = self.snippet.run(epoch)

            if len(err) == 0:
                return True, epoch
            if epoch == self.LIFETIME-1:
                return False, epoch

        return False, -1