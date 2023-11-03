from typing import Tuple

from main.utils.snippet import Snippet
from main.errors.error_base_class import ErrorBaseClass
from main.actions.action_base_class import ActionBaseClass
from main.actions.files.create_file import CreateFile

import re

class _FileNotFoundError(ErrorBaseClass):
    mappings = {
        r'(\S+) not found.*?': [ CreateFile ],
        r'\'(\S+)\' not found.*?': [ CreateFile ],
        r'\[Errno 2\] No such file or directory: \'(\S+)\'': [ CreateFile ],
        r'File (\S+) does not exist': [ CreateFile]
    }

    def __init__(self, path: str, snippet: Snippet, stack_trace: str) -> None:
        super().__init__(path=path, snippet=snippet, stack_trace=stack_trace)

    def find_action_class(self) -> Tuple[ActionBaseClass, dict]:
        for err_msg_pattern, action_class_list in _FileNotFoundError.mappings.items():
            if m := re.search(err_msg_pattern, self.err_msg):
                for ActionClass in action_class_list:
                    kwargs = {}
                    if ActionClass == CreateFile:
                        kwargs['file_name'] = m.groups()[0]
                        kwargs['file_content'] = 'abc'

                    if ActionClass(**kwargs).check_criteria():
                        return ActionClass, kwargs
        
        return None, None