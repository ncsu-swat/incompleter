from typing import Tuple

from main.utils.snippet import Snippet
from main.errors.error_base_class import ErrorBaseClass
from main.actions.action_base_class import ActionBaseClass
from main.actions.modules.install_module import InstallModule

import re

class _ModuleNotFoundError(ErrorBaseClass):
    mappings = {
        r'No module named \'(\S+)\'': [ InstallModule ]
    }
    
    def __init__(self, path: str, snippet: Snippet, stack_trace: str) -> None:
        super().__init__(path=path, snippet=snippet, stack_trace=stack_trace)

    def find_action_class(self) -> Tuple[ActionBaseClass, dict]:
        for err_msg_pattern, action_class_list in _ModuleNotFoundError.mappings.items():
            if m := re.search(err_msg_pattern, self.err_msg):
                for ActionClass in action_class_list:
                    kwargs = {}
                    if ActionClass == InstallModule:
                        kwargs['module_name'] = m.groups()[0]

                    if ActionClass(**kwargs).check_criteria():
                        return ActionClass, kwargs
        
        return None, None