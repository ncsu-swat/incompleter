from main.utils.snippet import Snippet
from main.actions.action_base_class import ActionBaseClass
from typing import Any
import os
import ast

from pathlib import Path

class StrToFloat(ActionBaseClass):
    def __init__(self, snippet: Snippet=None, lineno: int=0, **kwargs: dict) -> None:
        super().__init__(snippet, lineno)

        self.class_name = kwargs['class_name']

    def __str__(self) -> str:
        desc = super().__str__()
        desc += 'Class name: {}'.format(self.class_name)

        return desc

    def check_criteria(self) -> bool:
        return True

    def apply_pattern(self) -> str:
        class StrClassDefVisitor(ast.NodeTransformer):
            def __init__(self, **kwargs):
                self.snippet = kwargs['snippet']
                self.lineno = kwargs['lineno']
                self.class_name = kwargs['class_name']

            @ActionBaseClass.add_to_history
            def visit_Body(self, node):
                for (idx, child) in enumerate(node.body):
                    node.body[idx] = self.visit(child)
                return node

            def visit_ClassDef(self, node):
                if node.name == self.class_name:
                    for (idx, child) in enumerate(node.body):
                        if isinstance(child, ast.FunctionDef):
                            if child.name == '__repr__':
                                child.body = [
                                        ast.Return(ast.Constant(value='0.0', ctx=ast.Load()))
                                    ]
                return node

        tree = ast.parse(self.snippet.get_latest())
        tree = StrClassDefVisitor(snippet=self.snippet, lineno=self.lineno, class_name=self.class_name).visit_Body(tree)

        return None


