# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54602828/typeerror-unsupported-operand-types-for-tuple-and-int-why-i-can-not-s
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from numba import jit
    _l_(572775)

except ImportError:
    pass
try:
    import numpy as np
    _l_(572777)

except ImportError:
    pass
try:
    import time
    _l_(572779)

except ImportError:
    pass


@_n_(572780, "jit", lambda: jit)
def foo(x: _n_(572781, "int", lambda: int), y: _n_(572782, "int", lambda: int)) ->_n_(572783, "float", lambda: float):
    _l_(572807)

    tt = _c_(572786, _a_(572785, _n_(572784, "time", lambda: time), "time"))
    _l_(572787)
    s = 0
    _l_(572788)
    for i in _c_(572792, _n_(572789, "range", lambda: range), _n_(572790, "x", lambda: x),_n_(572791, "y", lambda: y)):
        _l_(572795)

        s += _n_(572793, "i", lambda: i)
        _l_(572794)
    _c_(572803, _n_(572796, "print", lambda: print), _c_(572802, _a_(572797, "Time used: {} sec", "format"), _c_(572800, _a_(572799, _n_(572798, "time", lambda: time), "time")) - _n_(572801, "tt", lambda: tt)))
    _l_(572804)
    aux = _n_(572805, "s", lambda: s)
    _l_(572806)
    return aux


_c_(572811, _n_(572808, "print", lambda: print), "value of foo", _c_(572810, _n_(572809, "foo", lambda: foo), 1, 1000))
_l_(572812)


def foo2(x, y)->_n_(572813, "float", lambda: float):
    _l_(572837)

    tt = _c_(572816, _a_(572815, _n_(572814, "time", lambda: time), "time"))
    _l_(572817)
    s = 0
    _l_(572818)
    for i in _c_(572822, _n_(572819, "range", lambda: range), _n_(572820, "x", lambda: x), _n_(572821, "y", lambda: y)):
        _l_(572825)

        s += _n_(572823, "i", lambda: i)
        _l_(572824)
    _c_(572833, _n_(572826, "print", lambda: print), _c_(572832, _a_(572827, "Time used for foo2: {} sec", "format"), _c_(572830, _a_(572829, _n_(572828, "time", lambda: time), "time")) - _n_(572831, "tt", lambda: tt)))
    _l_(572834)
    aux = _n_(572835, "s", lambda: s)
    _l_(572836)
    return aux


_c_(572841, _n_(572838, "print", lambda: print), "value of foo2", _c_(572840, _n_(572839, "foo2", lambda: foo2), 1, 1000))
_l_(572842)

a= _c_(572844, _n_(572843, "foo", lambda: foo), 1, 1000)
_l_(572845)
b= _c_(572847, _n_(572846, "foo2", lambda: foo2), 1, 1000)
_l_(572848)
_c_(572852, _n_(572849, "print", lambda: print), _n_(572850, "a", lambda: a)-_n_(572851, "b", lambda: b))
_l_(572853)
_c_(572858, _n_(572854, "print", lambda: print), _c_(572857, _n_(572855, "type", lambda: type), _n_(572856, "a", lambda: a)))
_l_(572859)
_c_(572864, _n_(572860, "print", lambda: print), _c_(572863, _n_(572861, "type", lambda: type), _n_(572862, "b", lambda: b)))
_l_(572865)
_c_(572873, _n_(572866, "print", lambda: print), _c_(572872, _n_(572867, "type", lambda: type), _c_(572871, _n_(572868, "foo2", lambda: foo2), (1, 1000)-_c_(572870, _n_(572869, "foo", lambda: foo), 1, 1000))))
_l_(572874)