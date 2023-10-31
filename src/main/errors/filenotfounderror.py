from main.actions.action import Action
from main.actions.files.create_file import CreateFile

import re

mappings = {
    r'(\S+) not found.*?': [ CreateFile ],
    r'\'(\S+)\' not found.*?': [ CreateFile ],
    r'\[Errno 2\] No such file or directory: \'(\S+)\'': [ CreateFile ],
    r'File (\S+) does not exist': [ CreateFile]
}

class _FileNotFoundError:
    def __init__(self, err_msg) -> None:
        self.err_msg = err_msg

    def find_action_class(self) -> Action:
        for err_msg_pattern, action_class_list in mappings.items():
            if m := re.search(err_msg_pattern, self.err_msg):
                for ActionClass in action_class_list:
                    kwargs = {}
                    if ActionClass == CreateFile:
                        kwargs['file_name'] = m.groups()[0]
                        kwargs['file_content'] = 'abc'

                    if ActionClass(**kwargs).check_criteria():
                        return ActionClass, kwargs
        
        return None, None