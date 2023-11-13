from main.utils.snippet import Snippet
from main.actions.action_base_class import ActionBaseClass
from main.actions.defines.define_class import DefineClass
from typing import Any
import ast

class DefineVar(ActionBaseClass):
    def __init__(self, snippet: Snippet=None, lineno: int=0, **kwargs: dict) -> None:
        super().__init__(snippet, lineno)

        self.var_name = kwargs['var_name']
        
        # Lazy definition
        self.var_val_id = 'TBD'+str(self.snippet.tbd_counter)
        self.var_val = ast.Call(
                func=ast.Name(id=self.var_val_id, ctx=ast.Load()),
                args=[],
                keywords=[]
            )

        self.rewritten_snippet = ''

    def __str__(self) -> str:
        desc = super().__str__()
        desc += 'Variable name: {}\nVariable value: {}\n'.format(self.var_name, self.var_val)

        return desc

    def check_criteria(self) -> bool:
        return True

    def apply_pattern(self) -> str:
        class DefineLazyVarTransformer(ast.NodeTransformer):
            def __init__(self, **kwargs: Any) -> None:
                self.snippet: Snippet = kwargs['snippet']
                self.lineno: int = kwargs['lineno']
                self.var_name: str = kwargs['var_name']
                self.var_val_id: str = kwargs['var_val_id']
                self.var_val: ast.Module = kwargs['var_val']

            @ActionBaseClass.rewrite_wrapper
            def visit_Body(self, node: ast.Module) -> ast.Module:
                node.body.insert(0, ast.Assign(
                        targets = [
                            ast.Name(id=self.var_name, ctx=ast.Store())
                        ],
                        value=self.var_val
                    )
                )
                
                return node

        tree = ast.parse(self.snippet.get_latest())
        DefineLazyVarTransformer(snippet=self.snippet, lineno=self.lineno, var_name=self.var_name, var_val_id=self.var_val_id, var_val=self.var_val).visit_Body(tree)

        DefineClass(snippet=self.snippet, lineno=self.lineno, class_name=self.var_val_id).apply_pattern()
        self.snippet.register_mock_definition(iter_n=self.snippet.get_current_iter(), target=self.var_name, value=self.var_val_id)
        
        return

