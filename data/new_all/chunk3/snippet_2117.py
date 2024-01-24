# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60073168/nameerror-while-using-functools-partial-inside-a-loop
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from functools import partial
    _l_(573450)

except ImportError:
    pass

def glob_func(a, b, c, x):
    _l_(573456)

    aux = 1000 * _n_(573451, "a", lambda: a) + 100 * _n_(573452, "b", lambda: b) + 10 * _n_(573453, "c", lambda: c) + _n_(573454, "x", lambda: x)
    _l_(573455)
    return aux

class MyClass:
    _l_(573465)


    local_func = _c_(573459, _n_(573457, "partial", lambda: partial), _n_(573458, "glob_func", lambda: glob_func), 3, 1, 4)
    _l_(573460)

    my_list = [_c_(573463, _n_(573461, "local_func", lambda: local_func), _n_(573462, "num", lambda: num))
        for num in (
            40,
            70,
            90
        )]
    _l_(573464)