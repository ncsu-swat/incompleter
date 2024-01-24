# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/52285972/unexpected-typeerror-nonetype-object-is-not-callable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_n_(523971, "gettime", lambda: gettime)
def contrast(a, b):
    _l_(523986)

    res = _c_(523979, _a_(523973, _n_(523972, "np", lambda: np), "sum"), _c_(523978, _a_(523975, _n_(523974, "np", lambda: np), "equal"), _n_(523976, "a", lambda: a), _n_(523977, "b", lambda: b)))/_c_(523982, _n_(523980, "len", lambda: len), _n_(523981, "a", lambda: a))
    _l_(523983)
    aux = _n_(523984, "res", lambda: res)
    _l_(523985)
    return aux

res = _c_(523990, _n_(523987, "contrast", lambda: contrast), _n_(523988, "A", lambda: A), _n_(523989, "B", lambda: B))
_l_(523991)
_c_(523994, _n_(523992, "print", lambda: print), "The correct rate is: %f"%_n_(523993, "res", lambda: res))
_l_(523995)