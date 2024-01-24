# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60322770/typeerror-with-validation-decorator-in-class-method
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(555205)

except ImportError:
    pass

def validate_decorator(func):
    _l_(555218)

    def func_wrapper(value):
        _l_(555215)

        if _n_(555206, "value", lambda: value) < 0:
            _l_(555210)

            raise _c_(555208, _n_(555207, "Exception", lambda: Exception), "Not valid!")
            _l_(555209)
        aux = _c_(555213, _n_(555211, "func", lambda: func), _n_(555212, "value", lambda: value))
        _l_(555214)
        return aux
    aux = _n_(555216, "func_wrapper", lambda: func_wrapper)
    _l_(555217)
    return aux


class MyClass:
    _l_(555243)

    def __init__(self):
        _l_(555226)

        _n_(555219, "self", lambda: self).my_array = _c_(555222, _a_(555221, _n_(555220, "np", lambda: np), "zeros"), shape=(10,))
        _l_(555223)
        _n_(555224, "self", lambda: self).idx = 0
        _l_(555225)

    @_n_(555227, "validate_decorator", lambda: validate_decorator)
    def insert_value(self, value):
        _l_(555236)

        _a_(555229, _n_(555228, "self", lambda: self), "my_array")[_a_(555231, _n_(555230, "self", lambda: self), "idx")] = _n_(555232, "value", lambda: value)
        _l_(555233)
        _n_(555234, "self", lambda: self).idx += 1
        _l_(555235)

    def __str__(self):
        _l_(555242)

        aux = f"{_a_(555238, _n_(555237, 'self', lambda: self), 'my_array')[:_a_(555240, _n_(555239, 'self', lambda: self), 'idx')]}"
        _l_(555241)
        return aux


a = _c_(555245, _n_(555244, "MyClass", lambda: MyClass))
_l_(555246)
_c_(555249, _a_(555248, _n_(555247, "a", lambda: a), "insert_value"), 3.14)
_l_(555250)