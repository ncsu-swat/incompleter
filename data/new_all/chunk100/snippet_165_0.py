# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def perfect_number(n):
    _l_(11403)

    for x in _c_(11393, _n_(11391, "range", lambda: range), 1, _n_(11392, "n", lambda: n)):
        _l_(11399)

        if _n_(11394, "n", lambda: n) % _n_(11395, "x", lambda: x) == 0:
            _l_(11398)

            sum += _n_(11396, "x", lambda: x)
            _l_(11397)
    aux = _n_(11400, "sum", lambda: sum) == _n_(11401, "n", lambda: n)
    _l_(11402)
    return aux
_c_(11407, _n_(11404, "print", lambda: print), _c_(11406, _n_(11405, "perfect_number", lambda: perfect_number), 6))
_l_(11408)