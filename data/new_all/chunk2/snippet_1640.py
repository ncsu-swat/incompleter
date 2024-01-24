# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67554168/python-decorator-on-class-typeerror-super-argument-1-must-be-type-not-funct
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import functools
    _l_(422210)

except ImportError:
    pass
registry = {}
_l_(422211)

def register(name=None):
    _l_(422233)

    """A decorator for registering modules
    :param name: (optional) name for component
    """
    def _wrap_func(func):
        _l_(422230)

        _n_(422212, "registry", lambda: registry)[_n_(422213, "name", lambda: name) or _a_(422215, _n_(422214, "func", lambda: func), "__name__")] = _n_(422216, "func", lambda: func)
        _l_(422217)

        @_c_(422221, _a_(422219, _n_(422218, "functools", lambda: functools), "wraps"), _n_(422220, "func", lambda: func))
        def _wrap_args(*args, **kwargs):
            _l_(422227)

            aux = _c_(422225, _n_(422222, "func", lambda: func), *_n_(422223, "args", lambda: args), **_n_(422224, "kwargs", lambda: kwargs))
            _l_(422226)
            return aux
        aux = _n_(422228, "_wrap_args", lambda: _wrap_args)
        _l_(422229)

        return aux
    aux = _n_(422231, "_wrap_func", lambda: _wrap_func)
    _l_(422232)
    return aux

class Base:
    _l_(422238)


    def __init__(self, arg):
        _l_(422237)

        _n_(422234, "self", lambda: self).arg = _n_(422235, "arg", lambda: arg)
        _l_(422236)

@_c_(422240, _n_(422239, "register", lambda: register), name="module1")
class Module1(_n_(422241, "Base", lambda: Base)):
    _l_(422250)


    def __init__(self, arg):
        _l_(422249)

        _c_(422247, _a_(422245, _n_(422242, "super", lambda: super)(_n_(422243, "Module1", lambda: Module1), _n_(422244, "self", lambda: self)), "__init__"), arg=_n_(422246, "arg", lambda: arg))
        _l_(422248)

@_c_(422252, _n_(422251, "register", lambda: register), name="module2")
class Module2(_n_(422253, "Base", lambda: Base)):
    _l_(422262)


    def __init__(self, arg):
        _l_(422261)

        _c_(422259, _a_(422257, _n_(422254, "super", lambda: super)(_n_(422255, "Module2", lambda: Module2), _n_(422256, "self", lambda: self)), "__init__"), arg=_n_(422258, "arg", lambda: arg))
        _l_(422260)