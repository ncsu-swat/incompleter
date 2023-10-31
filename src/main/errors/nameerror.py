from main.actions.action import Action
from main.actions.defines.define_var import DefineVar
from main.actions.modules.add_import import AddImport

import re

mappings = {
    r'name \'(\S+)\' is not defined': [ AddImport, DefineVar ]
}

class _NameError:
    def __init__(self, err_msg) -> None:
        self.err_msg = err_msg

    def find_action_class(self) -> Action:
        for err_msg_pattern, action_class_list in mappings.items():
            if m := re.search(err_msg_pattern, self.err_msg):
                for ActionClass in action_class_list:
                    kwargs = {}
                    if ActionClass == AddImport:
                        kwargs['module_name'] = m.groups()[0]
                    elif ActionClass == DefineVar:
                        kwargs['var_name'] = m.groups()[0]
                        kwargs['var_val'] = 1

                    if ActionClass(**kwargs).check_criteria():
                        return ActionClass, kwargs
        
        return None, None