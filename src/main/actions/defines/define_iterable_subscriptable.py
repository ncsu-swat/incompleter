from main.utils.snippet import Snippet
from main.actions.action_base_class import ActionBaseClass
from main.actions.defines.define_func import DefineFunc
from typing import Any
import ast

class DefineIterableOrSubscriptable(ActionBaseClass):
    def __init__(self, snippet: Snippet=None, lineno: int=0, **kwargs: dict) -> None:
        super().__init__(snippet, lineno)

        self.class_name = None
        if 'class_name' in kwargs: 
            self.class_name = kwargs['class_name']

        self.container_values = None
        if 'container_values' in kwargs:
            self.container_values = kwargs['container_values']
        else:
            self.container_values = ast.Dict(keys=[], values=[])

    def __str__(self) -> str:
        desc = super().__str__()
        desc += 'Iterable/Subscriptable Class name: {}\n'.format(self.class_name)

        return desc

    def check_criteria(self) -> bool:
        return True

    def apply_pattern(self) -> str:
        # define attributes inside __init__(self)
        self.__redefine_init()

        # define function __refresh_keys(self)
        self.__define_refresh_keys()

        # define function __str__(self)
        self.__define_str()

        # define function __getitem__(self, key)
        self.__define_getitem()

        # define function __setitem__(self, key, val)
        self.__define_setitem()

        # define function __iter__(self)
        self.__define_iter()

        # define function __len__(self)
        self.__define_len()

        return

    def __redefine_init(self) -> None:
        kwargs = {}
        kwargs['func_name'] = '__init__'
        kwargs['class_scope'] = self.class_name
        kwargs['func_args'] = [ast.arg(arg='self')]
        kwargs['func_body'] = [
            ast.Assign(
                targets=[
                    ast.Attribute(
                    value=ast.Name(id='self', ctx=ast.Load()),
                    attr='container',
                    ctx=ast.Store())],
                value=self.container_values),
            ast.Assign(
                targets=[
                    ast.Attribute(
                    value=ast.Name(id='self', ctx=ast.Load()),
                    attr='keys',
                    ctx=ast.Store())],
                value=ast.Call(
                    func=ast.Name(id='list', ctx=ast.Load()),
                    args=[
                        ast.Call(
                            func=ast.Attribute(
                            value=ast.Attribute(
                                value=ast.Name(id='self', ctx=ast.Load()),
                                attr='container',
                                ctx=ast.Load()),
                            attr='keys',
                            ctx=ast.Load()),
                            args=[],
                            keywords=[])],
                    keywords=[])),
            ast.Assign(
                targets=[
                    ast.Attribute(
                    value=ast.Name(id='self', ctx=ast.Load()),
                    attr='iter_current',
                    ctx=ast.Store())],
                value=ast.Constant(value=0))
        ]
        DefineFunc(snippet=self.snippet, lineno=self.lineno, **kwargs).apply_pattern()

        return

    def __define_refresh_keys(self) -> None:
        kwargs = {}
        kwargs['func_name'] = '__refresh_keys'
        kwargs['class_scope'] = self.class_name
        kwargs['func_args'] = [ast.arg(arg='self')]
        kwargs['func_body'] = [
            ast.Assign(
                targets=[
                    ast.Attribute(
                    value=ast.Name(id='self', ctx=ast.Load()),
                    attr='keys',
                    ctx=ast.Store())],
                value=ast.Call(
                    func=ast.Name(id='list', ctx=ast.Load()),
                    args=[
                        ast.Call(
                            func=ast.Attribute(
                            value=ast.Attribute(
                                value=ast.Name(id='self', ctx=ast.Load()),
                                attr='container',
                                ctx=ast.Load()),
                            attr='keys',
                            ctx=ast.Load()),
                            args=[],
                            keywords=[])],
                    keywords=[])),
            ast.Expr(
                value=ast.Call(
                    func=ast.Name(id='sorted', ctx=ast.Load()),
                    args=[
                        ast.Attribute(
                            value=ast.Name(id='self', ctx=ast.Load()),
                            attr='keys',
                            ctx=ast.Load())],
                    keywords=[]))
        ]
        DefineFunc(snippet=self.snippet, lineno=self.lineno, **kwargs).apply_pattern()

        return

    def __define_str(self) -> None:
        kwargs = {}
        kwargs['func_name'] = '__str__'
        kwargs['class_scope'] = self.class_name
        kwargs['func_args'] = [ast.arg(arg='self')]
        kwargs['func_body'] = [
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(
                    value=ast.Name(id='self', ctx=ast.Load()),
                    attr='__refresh_keys',
                    ctx=ast.Load()),
                    args=[],
                    keywords=[])),
            ast.Assign(
                targets=[
                    ast.Name(id='ret_str', ctx=ast.Store())],
                value=ast.Constant(value='')),
            ast.AugAssign(
                target=ast.Name(id='ret_str', ctx=ast.Store()),
                op=ast.Add(),
                value=ast.Constant(value='[ ')),
            ast.For(
                target=ast.Tuple(
                    elts=[
                    ast.Name(id='idx', ctx=ast.Store()),
                    ast.Tuple(
                        elts=[
                        ast.Name(id='key', ctx=ast.Store()),
                        ast.Name(id='val', ctx=ast.Store())],
                        ctx=ast.Store())],
                    ctx=ast.Store()),
                iter=ast.Call(
                    func=ast.Name(id='enumerate', ctx=ast.Load()),
                    args=[
                        ast.Call(
                            func=ast.Attribute(
                            value=ast.Attribute(
                                value=ast.Name(id='self', ctx=ast.Load()),
                                attr='container',
                                ctx=ast.Load()),
                            attr='items',
                            ctx=ast.Load()),
                            args=[],
                            keywords=[])],
                    keywords=[]),
                body=[
                    ast.AugAssign(
                        target=ast.Name(id='ret_str', ctx=ast.Store()),
                        op=ast.Add(),
                        value=ast.Call(
                            func=ast.Name(id='str', ctx=ast.Load()),
                            args=[
                            ast.Name(id='val', ctx=ast.Load())],
                            keywords=[])),
                    ast.If(
                        test=ast.Compare(
                            left=ast.Name(id='idx', ctx=ast.Load()),
                            ops=[
                                ast.Lt()],
                            comparators=[
                            ast.BinOp(
                                left=ast.Call(
                                func=ast.Name(id='len', ctx=ast.Load()),
                                args=[
                                    ast.Attribute(
                                    value=ast.Name(id='self', ctx=ast.Load()),
                                    attr='keys',
                                    ctx=ast.Load())],
                                keywords=[]),
                                op=ast.Sub(),
                                right=ast.Constant(value=1))]),
                        body=[
                            ast.AugAssign(
                                target=ast.Name(id='ret_str', ctx=ast.Store()),
                                op=ast.Add(),
                                value=ast.Constant(value=', '))],
                        orelse=[])],
                orelse=[]),
            ast.AugAssign(
                target=ast.Name(id='ret_str', ctx=ast.Store()),
                op=ast.Add(),
                value=ast.Constant(value=' ]')),
            ast.Return(
                value=ast.Name(id='ret_str', ctx=ast.Load()))
        ]
        DefineFunc(snippet=self.snippet, lineno=self.lineno, **kwargs).apply_pattern()

        return None

    def __define_getitem(self) -> None:
        kwargs = {}
        kwargs['func_name'] = '__getitem__'
        kwargs['class_scope'] = self.class_name
        kwargs['func_args'] = [ast.arg(arg='self'), ast.arg(arg='key')]
        kwargs['func_body'] = [
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(
                    value=ast.Name(id='self', ctx=ast.Load()),
                    attr='__refresh_keys',
                    ctx=ast.Load()),
                    args=[],
                    keywords=[])),
            ast.Assign(
                targets=[
                    ast.Name(id='ret_val', ctx=ast.Store())],
                value=ast.Constant(value=None)),
            ast.If(
                test=ast.Call(
                    func=ast.Name(id='isinstance', ctx=ast.Load()),
                    args=[
                        ast.Name(id='key', ctx=ast.Load()),
                        ast.Name(id='slice', ctx=ast.Load())],
                    keywords=[]),
                body=[
                    ast.Assign(
                        targets=[
                            ast.Name(id='list_to_return', ctx=ast.Store())],
                        value=ast.List(elts=[], ctx=ast.Load())),
                    ast.Assign(
                        targets=[
                            ast.Name(id='start', ctx=ast.Store())],
                        value=ast.BoolOp(
                            op=ast.Or(),
                            values=[
                                ast.Attribute(
                                    value=ast.Name(id='key', ctx=ast.Load()),
                                    attr='start',
                                    ctx=ast.Load()),
                                ast.Constant(value=0)])),
                    ast.Assign(
                        targets=[
                            ast.Name(id='stop', ctx=ast.Store())],
                        value=ast.BoolOp(
                            op=ast.Or(),
                            values=[
                                ast.Attribute(
                                    value=ast.Name(id='key', ctx=ast.Load()),
                                    attr='stop',
                                    ctx=ast.Load()),
                                ast.Call(
                                    func=ast.Name(id='len', ctx=ast.Load()),
                                    args=[
                                        ast.Attribute(
                                            value=ast.Name(id='self', ctx=ast.Load()),
                                            attr='container',
                                            ctx=ast.Load())],
                                    keywords=[])])),
                    ast.Assign(
                        targets=[
                            ast.Name(id='step', ctx=ast.Store())],
                        value=ast.BoolOp(
                            op=ast.Or(),
                            values=[
                                ast.Attribute(
                                    value=ast.Name(id='key', ctx=ast.Load()),
                                    attr='step',
                                    ctx=ast.Load()),
                                ast.Constant(value=1)])),
                    ast.If(
                        test=ast.Compare(
                            left=ast.Name(id='start', ctx=ast.Load()),
                            ops=[
                                ast.Lt()],
                            comparators=[
                                ast.Constant(value=0)]),
                        body=[
                            ast.Assign(
                                targets=[
                                    ast.Name(id='start', ctx=ast.Store())],
                                value=ast.Subscript(
                                    value=ast.Attribute(
                                    value=ast.Name(id='self', ctx=ast.Load()),
                                    attr='keys',
                                    ctx=ast.Load()),
                                    slice=ast.Name(id='start', ctx=ast.Load()),
                                    ctx=ast.Load()))],
                        orelse=[]),
                    ast.If(
                        test=ast.Compare(
                            left=ast.Name(id='stop', ctx=ast.Load()),
                            ops=[
                                ast.Lt()],
                            comparators=[
                                ast.Constant(value=0)]),
                        body=[
                            ast.Assign(
                                targets=[
                                    ast.Name(id='stop', ctx=ast.Store())],
                                value=ast.Subscript(
                                    value=ast.Attribute(
                                    value=ast.Name(id='self', ctx=ast.Load()),
                                    attr='keys',
                                    ctx=ast.Load()),
                                    slice=ast.Name(id='stop', ctx=ast.Load()),
                                    ctx=ast.Load()))],
                        orelse=[]),
                    ast.For(
                        target=ast.Name(id='i', ctx=ast.Store()),
                        iter=ast.Call(
                            func=ast.Name(id='range', ctx=ast.Load()),
                            args=[
                                ast.Name(id='start', ctx=ast.Load()),
                                ast.Name(id='stop', ctx=ast.Load()),
                                ast.Name(id='step', ctx=ast.Load())],
                            keywords=[]),
                        body=[
                            ast.Expr(
                            value=ast.Call(
                                func=ast.Attribute(
                                value=ast.Name(id='list_to_return', ctx=ast.Load()),
                                attr='append',
                                ctx=ast.Load()),
                                args=[
                                    ast.Subscript(
                                        value=ast.Attribute(
                                        value=ast.Name(id='self', ctx=ast.Load()),
                                        attr='container',
                                        ctx=ast.Load()),
                                        slice=ast.Name(id='i', ctx=ast.Load()),
                                        ctx=ast.Load())],
                                keywords=[]))],
                        orelse=[]),
                    ast.Assign(
                        targets=[
                            ast.Name(id='ret_val', ctx=ast.Store())],
                        value=ast.Name(id='list_to_return', ctx=ast.Load()))],
                orelse=[
                    ast.If(
                        test=ast.Call(
                            func=ast.Name(id='isinstance', ctx=ast.Load()),
                            args=[
                                ast.Name(id='key', ctx=ast.Load()),
                                ast.Name(id='int', ctx=ast.Load())],
                            keywords=[]),
                        body=[
                            ast.If(
                                test=ast.Compare(
                                    left=ast.Name(id='key', ctx=ast.Load()),
                                    ops=[
                                        ast.Lt()],
                                    comparators=[
                                        ast.Constant(value=0)]),
                                body=[
                                    ast.Assign(
                                        targets=[
                                            ast.Name(id='key', ctx=ast.Store())],
                                        value=ast.Subscript(
                                            value=ast.Attribute(
                                            value=ast.Name(id='self', ctx=ast.Load()),
                                            attr='keys',
                                            ctx=ast.Load()),
                                            slice=ast.Name(id='key', ctx=ast.Load()),
                                            ctx=ast.Load()))],
                                orelse=[]),
                            ast.Assign(
                                targets=[
                                    ast.Name(id='ret_val', ctx=ast.Store())],
                                value=ast.Subscript(
                                    value=ast.Attribute(
                                    value=ast.Name(id='self', ctx=ast.Load()),
                                    attr='container',
                                    ctx=ast.Load()),
                                    slice=ast.Name(id='key', ctx=ast.Load()),
                                    ctx=ast.Load()))],
                        orelse=[
                            ast.If(
                                test=ast.Call(
                                    func=ast.Name(id='isinstance', ctx=ast.Load()),
                                    args=[
                                        ast.Name(id='key', ctx=ast.Load()),
                                        ast.Name(id='str', ctx=ast.Load())],
                                    keywords=[]),
                                body=[
                                    ast.Assign(
                                        targets=[
                                            ast.Name(id='ret_val', ctx=ast.Store())],
                                        value=ast.Subscript(
                                            value=ast.Attribute(
                                            value=ast.Name(id='self', ctx=ast.Load()),
                                            attr='container',
                                            ctx=ast.Load()),
                                            slice=ast.Name(id='key', ctx=ast.Load()),
                                            ctx=ast.Load()))],
                                orelse=[])])]),
            ast.Return(
                value=ast.Name(id='ret_val', ctx=ast.Load()))
        ]
        DefineFunc(snippet=self.snippet, lineno=self.lineno, **kwargs).apply_pattern()

        return

    def __define_setitem(self) -> None:
        kwargs = {}
        kwargs['func_name'] = '__setitem__'
        kwargs['class_scope'] = self.class_name
        kwargs['func_args'] = [ast.arg(arg='self'), ast.arg(arg='key'), ast.arg(arg='val')]
        kwargs['func_body'] = [
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(
                        value=ast.Name(id='self', ctx=ast.Load()),
                        attr='__refresh_keys',
                        ctx=ast.Load()),
                    args=[],
                    keywords=[])),
            ast.If(
                test=ast.Call(
                    func=ast.Name(id='isinstance', ctx=ast.Load()),
                    args=[
                        ast.Name(id='key', ctx=ast.Load()),
                        ast.Name(id='slice', ctx=ast.Load())],
                    keywords=[]),
                body=[
                    ast.Assign(
                        targets=[
                            ast.Name(id='start', ctx=ast.Store())],
                        value=ast.BoolOp(
                            op=ast.Or(),
                            values=[
                                ast.Attribute(
                                    value=ast.Name(id='key', ctx=ast.Load()),
                                    attr='start',
                                    ctx=ast.Load()),
                                ast.Constant(value=0)])),
                    ast.Assign(
                        targets=[
                            ast.Name(id='stop', ctx=ast.Store())],
                        value=ast.BoolOp(
                            op=ast.Or(),
                            values=[
                                ast.Attribute(
                                    value=ast.Name(id='key', ctx=ast.Load()),
                                    attr='stop',
                                    ctx=ast.Load()),
                                ast.Call(
                                    func=ast.Name(id='len', ctx=ast.Load()),
                                    args=[
                                        ast.Attribute(
                                            value=ast.Name(id='self', ctx=ast.Load()),
                                            attr='container',
                                            ctx=ast.Load())],
                                    keywords=[])])),
                    ast.Assign(
                        targets=[
                            ast.Name(id='step', ctx=ast.Store())],
                        value=ast.BoolOp(
                            op=ast.Or(),
                            values=[
                                ast.Attribute(
                                    value=ast.Name(id='key', ctx=ast.Load()),
                                    attr='step',
                                    ctx=ast.Load()),
                                ast.Constant(value=1)])),
                    ast.If(
                        test=ast.Compare(
                            left=ast.Name(id='start', ctx=ast.Load()),
                            ops=[
                                ast.Lt()],
                            comparators=[
                                ast.Constant(value=0)]),
                        body=[
                            ast.Assign(
                                targets=[
                                    ast.Name(id='start', ctx=ast.Store())],
                                value=ast.Subscript(
                                    value=ast.Attribute(
                                        value=ast.Name(id='self', ctx=ast.Load()),
                                        attr='keys',
                                        ctx=ast.Load()),
                                    slice=ast.Name(id='start', ctx=ast.Load()),
                                ctx=ast.Load()))],
                        orelse=[]),
                    ast.If(
                        test=ast.Compare(
                            left=ast.Name(id='stop', ctx=ast.Load()),
                            ops=[
                                ast.Lt()],
                            comparators=[
                                ast.Constant(value=0)]),
                        body=[
                            ast.Assign(
                                targets=[
                                    ast.Name(id='stop', ctx=ast.Store())],
                                value=ast.Subscript(
                                    value=ast.Attribute(
                                        value=ast.Name(id='self', ctx=ast.Load()),
                                        attr='keys',
                                        ctx=ast.Load()),
                                    slice=ast.Name(id='stop', ctx=ast.Load()),
                                    ctx=ast.Load()))],
                        orelse=[]),
                    ast.For(
                        target=ast.Name(id='i', ctx=ast.Store()),
                        iter=ast.Call(
                            func=ast.Name(id='range', ctx=ast.Load()),
                            args=[
                                ast.Constant(value=0),
                                ast.Name(id='stop', ctx=ast.Load()),
                                ast.Name(id='step', ctx=ast.Load())],
                            keywords=[]),
                        body=[
                            ast.If(
                                test=ast.Compare(
                                    left=ast.Name(id='i', ctx=ast.Load()),
                                    ops=[
                                        ast.NotIn()],
                                    comparators=[
                                        ast.Attribute(
                                            value=ast.Name(id='self', ctx=ast.Load()),
                                            attr='keys',
                                            ctx=ast.Load())]),
                                body=[
                                    ast.Assign(
                                        targets=[
                                            ast.Subscript(
                                                value=ast.Attribute(
                                                    value=ast.Name(id='self', ctx=ast.Load()),
                                                    attr='container',
                                                    ctx=ast.Load()),
                                                slice=ast.Name(id='i', ctx=ast.Load()),
                                                ctx=ast.Store())],
                                        value=ast.Constant(value=0))],
                                orelse=[])],
                        orelse=[]),
                    ast.For(
                        target=ast.Name(id='i', ctx=ast.Store()),
                        iter=ast.Call(
                            func=ast.Name(id='range', ctx=ast.Load()),
                            args=[
                                ast.Name(id='start', ctx=ast.Load()),
                                ast.Name(id='stop', ctx=ast.Load()),
                                ast.Name(id='step', ctx=ast.Load())],
                            keywords=[]),
                        body=[
                            ast.Assign(
                                targets=[
                                    ast.Subscript(
                                        value=ast.Attribute(
                                            value=ast.Name(id='self', ctx=ast.Load()),
                                            attr='container',
                                            ctx=ast.Load()),
                                        slice=ast.Name(id='i', ctx=ast.Load()),
                                        ctx=ast.Store())],
                        value=ast.Name(id='val', ctx=ast.Load()))],
                        orelse=[]),
                    ast.Return(
                        value=ast.Constant(value=True))],
                orelse=[
                    ast.If(
                        test=ast.Call(
                            func=ast.Name(id='isinstance', ctx=ast.Load()),
                            args=[
                                ast.Name(id='key', ctx=ast.Load()),
                                ast.Name(id='int', ctx=ast.Load())],
                            keywords=[]),
                        body=[
                            ast.If(
                                test=ast.Compare(
                                    left=ast.Name(id='key', ctx=ast.Load()),
                                    ops=[
                                        ast.Lt()],
                                    comparators=[
                                        ast.Constant(value=0)]),
                                body=[
                                    ast.Assign(
                                        targets=[
                                            ast.Name(id='key', ctx=ast.Store())],
                                        value=ast.Subscript(
                                            value=ast.Attribute(
                                                value=ast.Name(id='self', ctx=ast.Load()),
                                                attr='keys',
                                                ctx=ast.Load()),
                                            slice=ast.Name(id='key', ctx=ast.Load()),
                                            ctx=ast.Load()))],
                                orelse=[]),
                            ast.For(
                                target=ast.Name(id='i', ctx=ast.Store()),
                                iter=ast.Call(
                                    func=ast.Name(id='range', ctx=ast.Load()),
                                    args=[
                                        ast.Constant(value=0),
                                        ast.Name(id='key', ctx=ast.Load())],
                                    keywords=[]),
                                body=[
                                    ast.If(
                                        test=ast.Compare(
                                            left=ast.Name(id='i', ctx=ast.Load()),
                                            ops=[
                                                ast.NotIn()],
                                            comparators=[
                                                ast.Attribute(
                                                    value=ast.Name(id='self', ctx=ast.Load()),
                                                    attr='keys',
                                                    ctx=ast.Load())]),
                                        body=[
                                            ast.Assign(
                                                targets=[
                                                    ast.Subscript(
                                                        value=ast.Attribute(
                                                            value=ast.Name(id='self', ctx=ast.Load()),
                                                            attr='container',
                                                            ctx=ast.Load()),
                                                        slice=ast.Name(id='i', ctx=ast.Load()),
                                                        ctx=ast.Store())],
                                                value=ast.Constant(value=0))],
                                        orelse=[])],
                                orelse=[]),
                            ast.Assign(
                                targets=[
                                    ast.Subscript(
                                        value=ast.Attribute(
                    value=ast.Name(id='self', ctx=ast.Load()),
                                            attr='container',
                                            ctx=ast.Load()),
                                        slice=ast.Name(id='key', ctx=ast.Load()),
                                        ctx=ast.Store())],
                                value=ast.Name(id='val', ctx=ast.Load())),
                            ast.Return(
                                value=ast.Constant(value=True))],
                        orelse=[
                            ast.If(
                                test=ast.Call(
                                    func=ast.Name(id='isinstance', ctx=ast.Load()),
                                    args=[
                                        ast.Name(id='key', ctx=ast.Load()),
                                        ast.Name(id='str', ctx=ast.Load())],
                                    keywords=[]),
                                body=[
                                    ast.Assign(
                                        targets=[
                                            ast.Subscript(
                                                value=ast.Attribute(
                                                    value=ast.Name(id='self', ctx=ast.Load()),
                                                    attr='container',
                                                    ctx=ast.Load()),
                                                slice=ast.Name(id='key', ctx=ast.Load()),
                                                ctx=ast.Store())],
                                        value=ast.Name(id='val', ctx=ast.Load())),
                                    ast.Return(
                                        value=ast.Constant(value=True))],
                                orelse=[])])]),
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(
                        value=ast.Name(id='self', ctx=ast.Load()),
                        attr='__refresh_keys',
                        ctx=ast.Load()),
                    args=[],
                    keywords=[])),
            ast.Return(
                value=ast.Constant(value=False))
        ]
        DefineFunc(snippet=self.snippet, lineno=self.lineno, **kwargs).apply_pattern()

        return

    def __define_iter(self) -> None:
        kwargs = {}
        kwargs['func_name'] = '__iter__'
        kwargs['class_scope'] = self.class_name
        kwargs['func_args'] = [ast.arg(arg='self')]
        kwargs['func_body'] = [
            ast.Return(
              value=ast.Call(
                func=ast.Name(id='iter', ctx=ast.Load()),
                args=[
                  ast.Attribute(
                    value=ast.Name(id='self', ctx=ast.Load()),
                    attr='containers',
                    ctx=ast.Load())],
                keywords=[]))
        ]
        DefineFunc(snippet=self.snippet, lineno=self.lineno, **kwargs).apply_pattern()

        return None

    def __define_len(self) -> None:
        kwargs = {}
        kwargs['func_name'] = '__len__'
        kwargs['class_scope'] = self.class_name
        kwargs['func_args'] = [ast.arg(arg='self')]
        kwargs['func_body'] = [
            ast.Return(
                value=ast.Call(
                    func=ast.Name(id='len', ctx=ast.Load()),
                    args=[
                        ast.Attribute(
                            value=ast.Name(id='self', ctx=ast.Load()),
                            attr='keys',
                            ctx=ast.Load())],
                    keywords=[]))
        ]
        DefineFunc(snippet=self.snippet, lineno=self.lineno, **kwargs).apply_pattern()

        return