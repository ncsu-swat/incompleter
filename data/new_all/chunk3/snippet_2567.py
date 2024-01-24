# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69520437/typeerror-float-object-is-not-subscriptable-when-accessing-the-float-elements
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(539085)

except ImportError:
    pass
try:
    from math import sqrt
    _l_(539087)

except ImportError:
    pass
try:
    import itertools
    _l_(539089)

except ImportError:
    pass

class MyClass():
    _l_(539142)

    id = _c_(539092, _a_(539091, _n_(539090, "itertools", lambda: itertools), "count"), start=1)
    _l_(539093)

    def __init__(self, location = None):
        _l_(539108)

        _n_(539094, "self", lambda: self).id = _c_(539098, _n_(539095, "next", lambda: next), _a_(539097, _n_(539096, "MyClass", lambda: MyClass), "id"))
        _l_(539099)
        _n_(539100, "self", lambda: self).location = _c_(539106, _a_(539105, _c_(539104, _a_(539103, _a_(539102, _n_(539101, "np", lambda: np), "random"), "uniform"), 0, 1, size=(1, 2)), "tolist"))[0]
        _l_(539107)


    def __iter__(self):
        _l_(539116)

        for _ in _c_(539112, _a_(539111, _a_(539110, _n_(539109, "self", lambda: self), "__dict__"), "values")):
            _l_(539115)

            yield _n_(539113, "_", lambda: _)
            _l_(539114)

    def f(self, obj):
        _l_(539128)

        aux = _c_(539126, _n_(539117, "sqrt", lambda: sqrt), (_a_(539119, _n_(539118, "self", lambda: self), "location")[0][0] - _a_(539121, _n_(539120, "obj", lambda: obj), "location")[0][0]) ** 2 + (_a_(539123, _n_(539122, "self", lambda: self), "location")[0][1] - _a_(539125, _n_(539124, "obj", lambda: obj), "location")[0][1]) ** 2)
        _l_(539127)
        return aux

    def g(self, objs):
        _l_(539141)

        flag = True
        _l_(539129)
        for obj in _n_(539130, "objs", lambda: objs):
            _l_(539138)

            if _c_(539134, _a_(539132, _n_(539131, "self", lambda: self), "f"), _n_(539133, "obj", lambda: obj)) > 0.8:
                _l_(539137)

                flag = False
                _l_(539135)
                break
                _l_(539136)
        aux = _n_(539139, "flag", lambda: flag)
        _l_(539140)
        return aux

def do():
    _l_(539172)

    objs = []
    _l_(539143)
    first_obj = _c_(539145, _n_(539144, "MyClass", lambda: MyClass))
    _l_(539146)
    _c_(539150, _a_(539148, _n_(539147, "objs", lambda: objs), "append"), _n_(539149, "first_obj", lambda: first_obj))
    _l_(539151)
    counter = 1
    _l_(539152)
    while _n_(539153, "counter", lambda: counter) != 10:
        _l_(539169)

        next_obj = _c_(539155, _n_(539154, "MyClass", lambda: MyClass))
        _l_(539156)
        if _c_(539160, _a_(539158, _n_(539157, "next_obj", lambda: next_obj), "g"), _n_(539159, "objs", lambda: objs)):
            _l_(539168)

            _c_(539164, _a_(539162, _n_(539161, "objs", lambda: objs), "append"), _n_(539163, "next_obj", lambda: next_obj))
            _l_(539165)
            counter = _n_(539166, "counter", lambda: counter) + 1
            _l_(539167)
    aux = _n_(539170, "objs", lambda: objs)
    _l_(539171)
    return aux

objs = _c_(539174, _n_(539173, "do", lambda: do))
_l_(539175)