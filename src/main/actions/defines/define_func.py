from main.utils.snippet import Snippet
from main.actions.action_base_class import ActionBaseClass
from typing import Any
import ast

class DefineFunc(ActionBaseClass):
    def __init__(self, snippet: Snippet=None, lineno: int=0, **kwargs: dict) -> None:
        super().__init__(snippet, lineno)

        self.func_name = kwargs['func_name']
        self.func_args = kwargs['func_args']
        self.func_body = kwargs['func_body']

    def __str__(self) -> str:
        desc = super().__str__()
        desc += 'Func name: {}\nFunc args: {}\nFunc body: {}\n'.format(self.func_name, self.func_args, self.func_body)

        return desc

    def check_criteria(self) -> bool:
        class FuncVisitor(ast.NodeVisitor):
            def __init__(self, **kwargs: dict) -> None:
                self.func_found = False
                self.func_name = kwargs['func_name']

            def visit_Call(self, node):
                if 'id' in dir(node.func):
                    if node.func.id == self.func_name:
                        self.func_found = True
                if 'attr' in dir(node.func):
                    if node.func.attr == self.func_name:
                        self.func_found = True
                return node

        tree = ast.parse(self.snippet.get_latest())
        
        func_visitor = FuncVisitor(func_name=self.func_name)
        func_visitor.visit(tree)

        return func_visitor.func_found

    def apply_pattern(self) -> str:
        class AddFuncTransformer(ast.NodeTransformer):
            def __init__(self, **kwargs: Any) -> None:
                self.lineno: int = kwargs['lineno']
                self.func_name: str = kwargs['func_name']
                self.func_args = kwargs['func_args']
                self.func_body: str = kwargs['func_body']

            def visit_Body(self, node: ast.Module) -> ast.Module:
                node.body.insert(0, ast.FunctionDef(
                    name=self.func_name,
                    args=ast.arguments(
                        posonlyargs=[],
                        args=[ast.arg(arg='a')],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[]
                    ),
                    body=[
                        ast.Return(value=ast.Constant(value=None))
                    ],
                    decorator_list=[]
                ))

                return node

        tree = ast.parse(self.snippet.get_latest())
        # print(ast.dump(tree, indent=4))

        AddFuncTransformer(lineno=self.lineno, func_name=self.func_name, func_args=self.func_args, func_body=self.func_body).visit_Body(tree)

        print(ast.unparse(ast.fix_missing_locations(tree)))
        
        return ast.unparse(ast.fix_missing_locations(tree))

