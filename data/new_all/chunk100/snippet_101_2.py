# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def max_min(data):
    _l_(4844)

    s = _n_(4827, "data", lambda: data)[0]
    _l_(4828)
    for num in _n_(4829, "data", lambda: data):
        _l_(4840)

        if _n_(4830, "num", lambda: num) > _n_(4831, "l", lambda: l):
            _l_(4839)

            l = _n_(4832, "num", lambda: num)
            _l_(4833)
        elif _n_(4834, "num", lambda: num) < _n_(4835, "s", lambda: s):
            _l_(4838)

            s = _n_(4836, "num", lambda: num)
            _l_(4837)
    aux = (_n_(4841, "l", lambda: l), _n_(4842, "s", lambda: s))
    _l_(4843)
    return aux
_c_(4848, _n_(4845, "print", lambda: print), _c_(4847, _n_(4846, "max_min", lambda: max_min), [0, 10, 15, 40, -5, 42, 17, 28, 75]))
_l_(4849)