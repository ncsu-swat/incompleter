from typing import Tuple

from main.utils.snippet import Snippet
from main.actions.action_base_class import ActionBaseClass

from main.errors.error_base_class import ErrorBaseClass
from main.errors.name_error import _NameError
from main.errors.file_not_found_error import _FileNotFoundError
from main.errors.module_not_found_error import _ModuleNotFoundError
from main.errors.attribute_error import _AttributeError
from main.errors.type_error import _TypeError
from main.errors.key_error import _KeyError

class ErrorCoordinator(ErrorBaseClass):
    mappings = {
        'NameError': _NameError,
        'FileNotFoundError': _FileNotFoundError,
        'ModuleNotFoundError': _ModuleNotFoundError,
        'AttributeError': _AttributeError,
        'TypeError': _TypeError,
        'KeyError': _KeyError
    }

    def __init__(self, path: str, snippet: Snippet, stack_trace: str) -> None:
        super().__init__(path=path, snippet=snippet, stack_trace=stack_trace)

    def find_action(self) -> ActionBaseClass:
        if self.err_type in ErrorCoordinator.mappings.keys():
            ErrorClass = ErrorCoordinator.mappings[self.err_type]
            return ErrorClass(path=self.path, snippet=self.snippet, stack_trace=self.stack_trace).find_action()
        else:
            # raise NotImplementedError('NotImplementedError: action pattern for error type {} has not been implemented yet.\n'.format(self.err_type))
            pass

        return None