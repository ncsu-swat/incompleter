from main.utils.snippet import Snippet
from main.actions.action_base_class import ActionBaseClass
from typing import Any
import ast

class ChangeReturn(ActionBaseClass):
    def __init__(self, snippet: Snippet=None, lineno: int=0, **kwargs: dict) -> None:
        super().__init__(snippet, lineno)

        self.func_name = kwargs['func_name']
        self.old_val = kwargs['old_val']
        self.new_val = kwargs['new_val']

    def __str__(self) -> str:
        desc = super().__str__()
        desc += 'Change return value of function: `{}`, from old value: `{}` to new value: `{}`\n'.format(self.func_name, self.old_val, self.new_val)

        return desc

    def check_criteria(self) -> bool:
        class FuncDefVisitor(ast.NodeVisitor):
            def __init__(self, **kwargs: dict) -> None:
                self.func_found = False
                self.func_name = kwargs['func_name']
                self.old_val = kwargs['old_val']

            def visit_FunctionDef(self, node):
                # if 'id' in dir(node.func):
                #     if node.func.id == self.func_name:
                #         self.func_found = True

                #         if 'args' in dir(node):
                #             for (arg_i, arg) in enumerate(node.args):
                #                 self.func_args.append(ast.arg(arg='arg'+str(arg_i)))
                #         if 'keywords' in dir(node):
                #             for kw in node.keywords:
                #                 self.func_keywords[ast.arg(arg=kw.arg)] = ast.Constant(value=None)

                # if 'attr' in dir(node.func):
                #     if node.func.attr == self.func_name:
                #         self.func_found = True
                    
                return node

        tree = ast.parse(self.snippet.get_latest())
        
        func_visitor = FuncDefVisitor(func_name=self.func_name, func_args=self.func_args, func_keywords=self.func_keywords)
        func_visitor.visit(tree)

        return func_visitor.func_found

    def apply_pattern(self) -> str:
        class ChangeReturnTransformer(ast.NodeTransformer):
            def __init__(self, **kwargs: Any) -> None:
                self.lineno: int = kwargs['lineno']
                self.func_name: str = kwargs['func_name']
                self.old_val: Any = kwargs['old_val']
                self.new_val: Any = kwargs['new_val']

            def visit_FunctionDef(self, node: ast.Module) -> ast.Module:
                

                return node

        tree = ast.parse(self.snippet.get_latest())
        # print(ast.dump(tree, indent=4))

        ChangeReturnTransformer(lineno=self.lineno, func_name=self.func_name, old_val=self.old_val, new_val=self.new_val).visit_Body(tree)

        print(ast.unparse(ast.fix_missing_locations(tree)))
        
        return ast.unparse(ast.fix_missing_locations(tree))

