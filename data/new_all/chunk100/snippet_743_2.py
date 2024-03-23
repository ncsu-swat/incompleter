# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import itertools
    _l_(74971)

except ImportError:
    pass
try:
    from functools import partial
    _l_(74973)

except ImportError:
    pass
X = [10, 20, 20, 20]
_l_(74974)
Z = [10, 30, 40, 20]
_l_(74975)
T = 70
_l_(74976)

def check_sum_array(N, *nums):
    _l_(74987)

    if _c_(74980, _n_(74977, "sum", lambda: sum), (_n_(74978, "x", lambda: x) for x in _n_(74979, "nums", lambda: nums))) == _n_(74981, "N", lambda: N):
        _l_(74986)

        aux = (True, _n_(74982, "nums", lambda: nums))
        _l_(74983)
        return aux
    else:
        aux = (False, _n_(74984, "nums", lambda: nums))
        _l_(74985)
        return aux
pro = _c_(74993, _a_(74989, _n_(74988, "itertools", lambda: itertools), "product"), _n_(74990, "X", lambda: X), _n_(74991, "Y", lambda: Y), _n_(74992, "Z", lambda: Z))
_l_(74994)
func = _c_(74998, _n_(74995, "partial", lambda: partial), _n_(74996, "check_sum_array", lambda: check_sum_array), _n_(74997, "T", lambda: T))
_l_(74999)
sums = _c_(75006, _n_(75000, "list", lambda: list), _c_(75005, _a_(75002, _n_(75001, "itertools", lambda: itertools), "starmap"), _n_(75003, "func", lambda: func), _n_(75004, "pro", lambda: pro)))
_l_(75007)
result = _c_(75009, _n_(75008, "set", lambda: set))
_l_(75010)
for s in _n_(75011, "sums", lambda: sums):
    _l_(75025)

    if _n_(75012, "s", lambda: s)[0] == True and _n_(75013, "s", lambda: s)[1] not in _n_(75014, "result", lambda: result):
        _l_(75024)

        _c_(75018, _a_(75016, _n_(75015, "result", lambda: result), "add"), _n_(75017, "s", lambda: s)[1])
        _l_(75019)
        _c_(75022, _n_(75020, "print", lambda: print), _n_(75021, "result", lambda: result))
        _l_(75023)