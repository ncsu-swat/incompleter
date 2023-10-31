from main.actions.action import Action
from main.actions.modules.install_module import InstallModule

import re

mappings = {
    r'No module named \'(\S+)\'': [ InstallModule ]
}

class _ModuleNotFoundError:
    def __init__(self, err_msg) -> None:
        self.err_msg = err_msg

    def find_action_class(self) -> Action:
        for err_msg_pattern, action_class_list in mappings.items():
            if m := re.search(err_msg_pattern, self.err_msg):
                for ActionClass in action_class_list:
                    kwargs = {}
                    if ActionClass == InstallModule:
                        kwargs['module_name'] = m.groups()[0]

                    if ActionClass(**kwargs).check_criteria():
                        return ActionClass, kwargs
        
        return None, None