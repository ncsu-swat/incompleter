from main.utils.snippet import Snippet
from main.actions.action import Action
from typing import Any
import ast

class Def_Var(Action):
    def __init__(self, snippet: Snippet, lineno: int, **kwargs: Any) -> None:
        super().__init__(snippet, lineno)

        self.var_name = kwargs['var_name']
        self.var_val = kwargs['var_val']

    def __str__(self) -> str:
        desc = super().__str__()
        desc += 'Variable name: {}\nVariable value: {}\n'.format(self.var_name, self.var_val)

        return desc

    def apply_pattern(self) -> ast.Module:
        class AddName(ast.NodeTransformer):
            def __init__(self, **kwargs: Any) -> None:
                self.lineno: int = kwargs['lineno']
                self.var_name: str = kwargs['var_name']
                self.var_val: Any = kwargs['var_val']

            def visit_Body(self, node: ast.Module) -> ast.Module:
                node.body.insert(self.lineno-1, ast.Assign(
                    targets = [
                        ast.Name(id=self.var_name, ctx=ast.Store())
                    ],
                    value=ast.Constant(value=self.var_val)
                ))
                
                return node

        tree = ast.parse(self.snippet.code[0])
        AddName(lineno=self.lineno, var_name=self.var_name, var_val=self.var_val).visit_Body(tree)

        print(ast.unparse(ast.fix_missing_locations(tree)))
        
        return tree

