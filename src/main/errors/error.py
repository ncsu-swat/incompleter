import re

from main.actions.action import Action
from main.errors.nameerror import _NameError

mappings = {
    'NameError': _NameError
}

class _Error:
    def __init__(self, path: str, stack_trace: str) -> None:
        if len(stack_trace) == 0: raise ValueError('Unable to instantiate Error object for empty stack trace')

        self.path = path
        self.stack_trace = stack_trace
        
        self.lineno = self.__extract_lineno()
        self.err_type = self.__extract_type()
        self.err_msg = self.__extract_msg()

    def __reformat_snippet_name(self):
        snippet_name = self.path.split('/')[-1]
        return snippet_name.replace('.', '\.')

    def __extract_lineno(self) -> int:
        snippet_name = self.__reformat_snippet_name()
        lineno = -1
        if m := re.search(r'File ".*?/{}", line (\d+)'.format(snippet_name), self.stack_trace):
            lineno = int(m.groups()[0])
        
        if lineno == -1: raise ValueError('Unable to extract error line number from:\n\n{}\n'.format(self.stack_trace))

        return lineno

    def __extract_type(self) -> str:
        err_type = ''
        for line in self.stack_trace.split('\n'):
            if 'Error:' in line:
                err_type = line.split(':')[0]
        
        if err_type == '': raise ValueError('Unable to extract error type from:\n\n{}\n'.format(self.stack_trace))

        return err_type.strip()

    def __extract_msg(self) -> str:
        err_msg = ''
        for line in self.stack_trace.split('\n'):
            if 'Error:' in line:
                err_msg = line.split(':')[1]
        
        if err_msg == '': raise ValueError('Unable to extract error message from:\n\n{}\n'.format(self.stack_trace))

        return err_msg.strip()

    def find_action_class(self) -> Action:
        if self.err_type in mappings.keys():
            ErrorClass = mappings[self.err_type]
            return ErrorClass(err_msg=self.err_msg).find_action_class()
        else:
            # raise NotImplementedError('NotImplementedError: action pattern for error type {} has not been implemented yet.\n'.format(self.err_type))
            pass

        return None, None

                        
