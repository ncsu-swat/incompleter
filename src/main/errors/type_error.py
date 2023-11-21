from typing import Tuple

from main.utils.snippet import Snippet
from main.errors.error_base_class import ErrorBaseClass
from main.actions.action_base_class import ActionBaseClass
from main.actions.defines.define_callable import DefineCallable
from main.actions.defines.define_iterable_subscriptable import DefineIterableOrSubscriptable

import re
import ast
from enum import Enum

class _TypeError(ErrorBaseClass):
    mappings = {
        r'must be str, not int': [],
        r'\'(\S+)\' object is not (\S+)': [],
        r'list indices must be integers or slices, not (\S+)': [],
        r'\'(\S+)\' object is not callable': [ DefineCallable ],
        r'\'(\S+)\' object is not iterable': [ DefineIterableOrSubscriptable ],
        r'\'(\S+)\' object is not subscriptable': [ DefineIterableOrSubscriptable ],
        r'argument of type \'(\S+)\' is not iterable': [],
        r'unsupported operand type(s) for \S+: \'(\S+)\' and \'\S+\'': [],
        r'\'(\S+)\' object does not support item assignment': [],
        r'can only concatenate str (not "TBD0") to str': []
    }

    def __init__(self, path: str, snippet: Snippet, stack_trace: str) -> None:
        super().__init__(path=path, snippet=snippet, stack_trace=stack_trace)

    def find_action(self) -> ActionBaseClass:
        for err_msg_pattern, action_class_list in _TypeError.mappings.items():
            if m := re.search(err_msg_pattern, self.err_msg):
                # print('Matched pattern: {}\n'.format(err_msg_pattern))
                # print(self.snippet.get_latest().split('\n')[self.lineno+1])

                kwargs = {}
                if err_msg_pattern in [ r'\'(\S+)\' object is not callable', r'\'(\S+)\' object is not iterable', r'\'(\S+)\' object is not subscriptable' ]:
                    kwargs['class_name'] = m.groups()[0]

                for ActionClass in action_class_list:
                    if (action := ActionClass(snippet=self.snippet, lineno=self.lineno, **kwargs)).check_criteria():
                        return action
        
        return None