# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def add_without_plus_operator(a, b):
    _l_(53516)

    while _n_(53506, "b", lambda: b) != 0:
        _l_(53513)

        data = _n_(53507, "a", lambda: a) & _n_(53508, "b", lambda: b)
        _l_(53509)
        a = _n_(53510, "a", lambda: a) ^ _n_(53511, "b", lambda: b)
        _l_(53512)
    aux = _n_(53514, "a", lambda: a)
    _l_(53515)
    return aux
_c_(53520, _n_(53517, "print", lambda: print), _c_(53519, _n_(53518, "add_without_plus_operator", lambda: add_without_plus_operator), 2, 10))
_l_(53521)
_c_(53525, _n_(53522, "print", lambda: print), _c_(53524, _n_(53523, "add_without_plus_operator", lambda: add_without_plus_operator), -20, 10))
_l_(53526)
_c_(53530, _n_(53527, "print", lambda: print), _c_(53529, _n_(53528, "add_without_plus_operator", lambda: add_without_plus_operator), -10, -20))
_l_(53531)