from typing import Tuple

from main.utils.snippet import Snippet
from main.errors.error_base_class import ErrorBaseClass
from main.actions.action_base_class import ActionBaseClass
from main.actions.defines.define_func import DefineFunc
from main.actions.defines.define_var import DefineVar

import re

class _AttributeError(ErrorBaseClass):
    mappings = {
        r'\'(\S+)\' object has no attribute \'(\S+)\'': [ DefineFunc, DefineVar ]
    }

    def __init__(self, path: str, snippet: Snippet, stack_trace: str) -> None:
        super().__init__(path=path, snippet=snippet, stack_trace=stack_trace)

    def find_action(self) -> ActionBaseClass:
        for err_msg_pattern, action_class_list in _AttributeError.mappings.items():
            if m := re.search(err_msg_pattern, self.err_msg):
                for ActionClass in action_class_list:
                    kwargs = {}
                    if ActionClass == DefineVar:
                        kwargs['var_name'] = m.groups()[1]
                        kwargs['class_scope'] = m.groups()[0]
                        kwargs['func_scope'] = '__init__'
                    elif ActionClass == DefineFunc:
                        kwargs['func_name'] = m.groups()[1]
                        kwargs['class_scope'] = m.groups()[0]

                    if (action := ActionClass(snippet=self.snippet, lineno=self.lineno, **kwargs)).check_criteria():
                        return action
        
        return None