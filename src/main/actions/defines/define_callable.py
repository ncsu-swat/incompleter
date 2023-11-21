from main.utils.snippet import Snippet
from main.actions.action_base_class import ActionBaseClass
from main.actions.defines.define_func import DefineFunc
from typing import Any
import ast

class DefineCallable(ActionBaseClass):
    def __init__(self, snippet: Snippet=None, lineno: int=0, **kwargs: dict) -> None:
        super().__init__(snippet, lineno)

        self.class_name = None
        if 'class_name' in kwargs: 
            self.class_name = kwargs['class_name']

    def __str__(self) -> str:
        desc = super().__str__()
        desc += 'Callable Class name: {}\n'.format(self.class_name)

        return desc

    def check_criteria(self) -> bool:
        return True

    def apply_pattern(self) -> None:
        # Define __call__ function inside the erroneous TBD class
        self.__define_call()

        return

    def __find_func_name(self) -> str:
        # e.g. Let's consider a statement: ident_0 = TBD#() --> In this function, we will try to find the original function name ident_0 from the TBD class name TBD#. We know that ident_0 will be a function name because we are in the DefineCallable action class. And, we need to find the original name of the function in order to get its argument information using DefineFunc#check_criteria (lookahead static analysis).
        class FuncNameFinderVisitor(ast.NodeVisitor):
            def __init__(self, **kwargs: dict) -> None:
                self.class_name = kwargs['class_name']
                self.func_name = None

            def visit_Assign(self, node) -> ast.Module:
                if isinstance(node.value, ast.Call) and isinstance(node.value.func, ast.Name):
                    if node.value.func.id == self.class_name:
                        if type(node.targets[0]) == ast.Attribute:
                            self.func_name = node.targets[0].attr
                        elif type(node.targets[0]) == ast.Name:
                            self.func_name = node.targets[0].id
                return node

        tree = ast.parse(self.snippet.get_latest())
        func_name_finder_visitor = FuncNameFinderVisitor(class_name=self.class_name)
        func_name_finder_visitor.visit(tree)

        return func_name_finder_visitor.func_name

    def __define_call(self) -> None:
        kwargs = {}
        kwargs['func_name'] = self.__find_func_name()

        if kwargs['func_name'] is not None:
            kwargs['class_scope'] = self.class_name
            arg_finder = DefineFunc(snippet=self.snippet, lineno=self.lineno, **kwargs)

            if arg_finder.check_criteria():
                arg_finder.func_name = '__call__'
                arg_finder.func_args.insert(0, ast.arg(arg='self'))
                arg_finder.apply_pattern()
        
        return