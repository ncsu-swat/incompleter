# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def add_without_plus_operator(a, b):
    _l_(53490)

    while _n_(53481, "b", lambda: b) != 0:
        _l_(53487)

        data = _n_(53482, "a", lambda: a) & _n_(53483, "b", lambda: b)
        _l_(53484)
        b = _n_(53485, "data", lambda: data) << 1
        _l_(53486)
    aux = _n_(53488, "a", lambda: a)
    _l_(53489)
    return aux
_c_(53494, _n_(53491, "print", lambda: print), _c_(53493, _n_(53492, "add_without_plus_operator", lambda: add_without_plus_operator), 2, 10))
_l_(53495)
_c_(53499, _n_(53496, "print", lambda: print), _c_(53498, _n_(53497, "add_without_plus_operator", lambda: add_without_plus_operator), -20, 10))
_l_(53500)
_c_(53504, _n_(53501, "print", lambda: print), _c_(53503, _n_(53502, "add_without_plus_operator", lambda: add_without_plus_operator), -10, -20))
_l_(53505)