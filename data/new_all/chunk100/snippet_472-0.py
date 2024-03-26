# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def test(a):
    _l_(117692)


    def add(b):
        _l_(117689)

        nonlocal a
        _l_(117684)
        a += 1
        _l_(117685)
        aux = _n_(117686, "a", lambda: a) + _n_(117687, "b", lambda: b)
        _l_(117688)
        return aux
    aux = _n_(117690, "add", lambda: add)
    _l_(117691)
    return aux
_c_(117696, _n_(117693, "print", lambda: print), _c_(117695, _n_(117694, "func", lambda: func), 4))
_l_(117697)