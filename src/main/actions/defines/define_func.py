from main.utils.snippet import Snippet
from main.actions.action_base_class import ActionBaseClass
from main.actions.defines.define_class import DefineClass
from typing import Any
import ast

class DefineFunc(ActionBaseClass):
    def __init__(self, snippet: Snippet=None, lineno: int=0, **kwargs: dict) -> None:
        super().__init__(snippet, lineno)

        self.func_name = kwargs['func_name']

        self.func_vararg = []
        self.func_kwarg = []
        self.func_args = []
        if 'func_args' in kwargs: self.func_args = kwargs['func_args']
        self.func_keywords = {}
        if 'func_keywords' in kwargs: self.func_keywords = kwargs['func_keywords']
        
        self.func_body = []
        if 'func_body' in kwargs: 
            self.func_body = kwargs['func_body']
        else:
            self.ret_val_id = 'TBD'+str(self.snippet.tbd_counter)
            self.func_body.append(ast.Return(value=ast.Call(
                                                func=ast.Name(id=self.ret_val_id, ctx=ast.Load()),
                                                args=[],
                                                keywords=[])
                                            ))

    def __str__(self) -> str:
        desc = super().__str__()
        desc += 'Func name: {}\nFunc args: {}\nFunc keywords: {}\nFunc body: {}\n'.format(self.func_name, self.func_args, self.func_keywords, self.func_body)

        return desc

    def check_criteria(self) -> bool:
        class FuncCallVisitor(ast.NodeVisitor):
            def __init__(self, **kwargs: dict) -> None:
                self.func_found = False
                self.func_name = kwargs['func_name']
                self.func_vararg = kwargs['func_vararg']
                self.func_kwarg = kwargs['func_kwarg']
                self.func_args = kwargs['func_args']
                self.func_keywords = kwargs['func_keywords']

            def visit_Call(self, node):
                if 'id' in dir(node.func):
                    if node.func.id == self.func_name:
                        self.func_found = True

                        if node.args:
                            for (arg_i, arg) in enumerate(node.args):
                                if isinstance(arg, ast.Starred):
                                    self.func_vararg.append(ast.arg(arg='arg'+str(arg_i)))
                                else:
                                    self.func_args.append(ast.arg(arg='arg'+str(arg_i)))
                        if node.keywords:
                            for kw in node.keywords:
                                if kw.arg:
                                    self.func_keywords[ast.arg(arg=kw.arg)] = ast.Constant(value=None)
                                else:
                                    self.func_kwarg.append(ast.arg(arg=kw.value.id))
                    
                return node

        tree = ast.parse(self.snippet.get_latest())
        
        func_visitor = FuncCallVisitor(func_name=self.func_name, func_vararg=self.func_vararg, func_kwarg=self.func_kwarg, func_args=self.func_args, func_keywords=self.func_keywords)
        func_visitor.visit(tree)

        return func_visitor.func_found

    def apply_pattern(self) -> str:
        class DefineLazyFuncTransformer(ast.NodeTransformer):
            def __init__(self, **kwargs: Any) -> None:
                self.snippet: Snippet = kwargs['snippet']
                self.lineno: int = kwargs['lineno']
                self.func_name: str = kwargs['func_name']
                self.func_vararg: str = kwargs['func_vararg']
                self.func_kwarg: str = kwargs['func_kwarg']
                self.func_args = kwargs['func_args']
                self.func_keywords = kwargs['func_keywords']
                self.func_body: str = kwargs['func_body']

            @ActionBaseClass.add_to_history
            def visit_Body(self, node: ast.Module) -> ast.Module:
                func_def = ast.FunctionDef(
                    name=self.func_name,
                    args=ast.arguments(
                        posonlyargs=[],
                        vararg=None,
                        kwarg=None,
                        args=[],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[]
                    ),
                    body=self.func_body,
                    decorator_list=[]
                )

                if len(self.func_args):
                    func_def.args.args = self.func_args
                if len(self.func_keywords):
                    func_def.args.args = list(self.func_keywords.keys())
                    func_def.args.defaults = list(self.func_keywords.values())
                if len(self.func_vararg):
                    func_def.args.vararg = self.func_vararg[0]
                if len(self.func_kwarg):
                    func_def.args.kwarg = self.func_kwarg[0]

                node.body.insert(0, func_def)

                return node

        tree = ast.parse(self.snippet.get_latest())
        DefineLazyFuncTransformer(snippet=self.snippet, lineno=self.lineno, func_name=self.func_name, func_vararg=self.func_vararg, func_kwarg=self.func_kwarg, func_args=self.func_args, func_keywords=self.func_keywords, func_body=self.func_body).visit_Body(tree)

        if self.ret_val_id: 
            DefineClass(snippet=self.snippet, lineno=self.lineno, class_name=self.ret_val_id).apply_pattern()
        self.snippet.register_mock_definition(iter_n=self.snippet.get_current_iter(), target=self.func_name, value=self.ret_val_id)
        
        return

