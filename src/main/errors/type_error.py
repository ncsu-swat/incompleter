from typing import Tuple

from main.utils.snippet import Snippet
from main.errors.error_base_class import ErrorBaseClass
from main.actions.action_base_class import ActionBaseClass

import re

class _TypeError(ErrorBaseClass):
    mappings = {
        r'must be str, not int': [],
        r'\'(\S+)\' object is not callable': [],
        r'list indices must be integers or slices, not str': [],
        r'\'(\S+)\' object is not iterable': [],
        r'unsupported operand type(s) for \S+: \'(\S+)\' and \'\S+\'': [],
    }

    def __init__(self, path: str, snippet: Snippet, stack_trace: str) -> None:
        super().__init__(path=path, snippet=snippet, stack_trace=stack_trace)

    def find_action(self) -> ActionBaseClass:
        for err_msg_pattern, action_class_list in _TypeError.mappings.items():
            if m := re.search(err_msg_pattern, self.err_msg):
                print('Matched pattern: {}\n'.format(err_msg_pattern))
                # print(self.snippet.get_latest().split('\n')[self.lineno+1])

                for ActionClass in action_class_list:
                    kwargs = {}
                    # if ActionClass == :
                        

                    # if (action := ActionClass(snippet=self.snippet, lineno=self.lineno, **kwargs)).check_criteria():
                    #     return action
        
        return None