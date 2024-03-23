# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def max_min(data):
    _l_(4821)

    l = _n_(4804, "data", lambda: data)[0]
    _l_(4805)
    for num in _n_(4806, "data", lambda: data):
        _l_(4817)

        if _n_(4807, "num", lambda: num) > _n_(4808, "l", lambda: l):
            _l_(4816)

            l = _n_(4809, "num", lambda: num)
            _l_(4810)
        elif _n_(4811, "num", lambda: num) < _n_(4812, "s", lambda: s):
            _l_(4815)

            s = _n_(4813, "num", lambda: num)
            _l_(4814)
    aux = (_n_(4818, "l", lambda: l), _n_(4819, "s", lambda: s))
    _l_(4820)
    return aux
_c_(4825, _n_(4822, "print", lambda: print), _c_(4824, _n_(4823, "max_min", lambda: max_min), [0, 10, 15, 40, -5, 42, 17, 28, 75]))
_l_(4826)