from main.utils.snippet import Snippet
from main.actions.action_base_class import ActionBaseClass
from typing import Any
import os
import ast

from pathlib import Path

class StrToInt(ActionBaseClass):
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
                    has_new = any(isinstance(child, ast.FunctionDef) and child.name == '__new__' for child in node.body)
            
                    if not has_new:
                        new_method = self.create_new_method_ast()
                        node.body.insert(0, new_method)
                return node

            def create_new_method_ast(self):
                #  __new__ method: cls, *args, **kwargs
                args = ast.arguments(
                    posonlyargs=[],
                    args=[ast.arg(arg='cls', annotation=None)],
                    vararg=ast.arg(arg='args', annotation=None),
                    kwonlyargs=[],
                    kw_defaults=[],
                    kwarg=ast.arg(arg='kwargs', annotation=None),
                    defaults=[],
                )
                
                # super().__new__(cls, "0.0")
                new_call = ast.Call(
                    func=ast.Attribute(
                        value=ast.Call(
                            func=ast.Name(id='super', ctx=ast.Load()),
                            args=[],
                            keywords=[],
                        ),
                        attr='__new__',
                        ctx=ast.Load(),
                    ),
                    args=[ast.Name(id='cls', ctx=ast.Load()), ast.Constant(value="0")],
                    keywords=[],
                )
                
                return_stmt = ast.Return(value=new_call)
                
                new_method = ast.FunctionDef(
                    name='__new__',
                    args=args,
                    body=[return_stmt],
                    decorator_list=[],
                    returns=None,
                )
                
                return new_method

        tree = ast.parse(self.snippet.get_latest())
        tree = StrClassDefVisitor(snippet=self.snippet, lineno=self.lineno, class_name=self.class_name).visit_Body(tree)

        return None


