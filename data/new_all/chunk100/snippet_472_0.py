# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def test(a):
    _l_(49615)


    def add(b):
        _l_(49612)

        nonlocal a
        _l_(49607)
        a += 1
        _l_(49608)
        aux = _n_(49609, "a", lambda: a) + _n_(49610, "b", lambda: b)
        _l_(49611)
        return aux
    aux = _n_(49613, "add", lambda: add)
    _l_(49614)
    return aux
_c_(49619, _n_(49616, "print", lambda: print), _c_(49618, _n_(49617, "func", lambda: func), 4))
_l_(49620)