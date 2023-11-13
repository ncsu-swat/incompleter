from typing import Tuple

from main.utils.snippet import Snippet
from main.errors.error_base_class import ErrorBaseClass
from main.actions.action_base_class import ActionBaseClass
from main.actions.defines.define_var import DefineVar

import re
import ast

class _TypeError(ErrorBaseClass):
    mappings = {
        r'must be str, not int': [],
        r'\'(\S+)\' object is not (\S+)': [],
        r'list indices must be integers or slices, not (\S+)': [],
        r'\'(\S+)\' object is not iterable': [ DefineVar ],
        r'argument of type \'(\S+)\' is not iterable': [],
        r'unsupported operand type(s) for \S+: \'(\S+)\' and \'\S+\'': [],
        r'\'(\S+)\' object does not support item assignment': []
    }

    def __init__(self, path: str, snippet: Snippet, stack_trace: str) -> None:
        super().__init__(path=path, snippet=snippet, stack_trace=stack_trace)

    def find_action(self) -> ActionBaseClass:
        for err_msg_pattern, action_class_list in _TypeError.mappings.items():
            if m := re.search(err_msg_pattern, self.err_msg):
                # print('Matched pattern: {}\n'.format(err_msg_pattern))
                # print(self.snippet.get_latest().split('\n')[self.lineno+1])

                if err_msg_pattern == r'\'(\S+)\' object is not iterable':
                    erroneous_type = m.groups()[0]

                    class ErroneousIdentifierFinderVisitor(ast.NodeVisitor):
                        def __init__(self, **kwargs):
                            self.erroneous_type = kwargs['from_type']
                            self.root_err_identifier = ''
                        def visit_Name(self, node):
                            
                            return node

                    print('\n\nIN TYPEERROR - LATEST SNIPPET\n\n{}'.format(self.snippet.get_latest().split('\n')))
                    tree = ast.parse(self.snippet.get_latest().split('\n')[self.lineno-1])
                    erroneous_identifier_finder_visitor = ErroneousIdentifierFinderVisitor(snippet=self.snippet, from_type=erroneous_type)
                    erroneous_identifier_finder_visitor.visit(tree)
                    
                    kwargs = {}
                    kwargs['var_name'] = erroneous_identifier_finder_visitor.root_err_identifier
                    kwargs['var_val'] = ast.BinOp(
                            left=ast.List(
                                elts=[
                                    ast.Constant(value=None)
                                ],
                                ctx=ast.Load()
                            ),
                            op=ast.Mult(),
                            right=ast.Constant(value=1000)
                        )

                    if len(kwargs['var_name']):
                        return DefineVar(snippet=self.snippet, lineno=self.lineno, **kwargs)

                # for ActionClass in action_class_list:
                #     kwargs = {}
                #     if ActionClass == DefineVar:
                #         kwargs=

                    # if (action := ActionClass(snippet=self.snippet, lineno=self.lineno, **kwargs)).check_criteria():
                    #     return action
        
        return None