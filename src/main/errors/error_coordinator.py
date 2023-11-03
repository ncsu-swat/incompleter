from typing import Tuple

from main.utils.snippet import Snippet
from main.actions.action_base_class import ActionBaseClass

from main.errors.error_base_class import ErrorBaseClass
from main.errors.name_error import _NameError
from main.errors.file_not_found_error import _FileNotFoundError
from main.errors.module_not_found_error import _ModuleNotFoundError

class ErrorCoordinator(ErrorBaseClass):
    mappings = {
        'NameError': _NameError,
        'FileNotFoundError': _FileNotFoundError,
        'ModuleNotFoundError': _ModuleNotFoundError
    }

    def __init__(self, path: str, snippet: Snippet, stack_trace: str) -> None:
        super().__init__(path=path, snippet=snippet, stack_trace=stack_trace)

    def find_action_class(self) -> Tuple[ActionBaseClass, dict]:
        if self.err_type in ErrorCoordinator.mappings.keys():
            ErrorClass = ErrorCoordinator.mappings[self.err_type]
            return ErrorClass(path=self.path, snippet=self.snippet, stack_trace=self.stack_trace).find_action_class()
        else:
            # raise NotImplementedError('NotImplementedError: action pattern for error type {} has not been implemented yet.\n'.format(self.err_type))
            pass

        return None, None