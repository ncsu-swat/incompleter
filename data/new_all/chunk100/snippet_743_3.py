# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import itertools
    _l_(75027)

except ImportError:
    pass
try:
    from functools import partial
    _l_(75029)

except ImportError:
    pass
X = [10, 20, 20, 20]
_l_(75030)
Y = [10, 20, 30, 40]
_l_(75031)
Z = [10, 30, 40, 20]
_l_(75032)

def check_sum_array(N, *nums):
    _l_(75043)

    if _c_(75036, _n_(75033, "sum", lambda: sum), (_n_(75034, "x", lambda: x) for x in _n_(75035, "nums", lambda: nums))) == _n_(75037, "N", lambda: N):
        _l_(75042)

        aux = (True, _n_(75038, "nums", lambda: nums))
        _l_(75039)
        return aux
    else:
        aux = (False, _n_(75040, "nums", lambda: nums))
        _l_(75041)
        return aux
pro = _c_(75049, _a_(75045, _n_(75044, "itertools", lambda: itertools), "product"), _n_(75046, "X", lambda: X), _n_(75047, "Y", lambda: Y), _n_(75048, "Z", lambda: Z))
_l_(75050)
func = _c_(75054, _n_(75051, "partial", lambda: partial), _n_(75052, "check_sum_array", lambda: check_sum_array), _n_(75053, "T", lambda: T))
_l_(75055)
sums = _c_(75062, _n_(75056, "list", lambda: list), _c_(75061, _a_(75058, _n_(75057, "itertools", lambda: itertools), "starmap"), _n_(75059, "func", lambda: func), _n_(75060, "pro", lambda: pro)))
_l_(75063)
result = _c_(75065, _n_(75064, "set", lambda: set))
_l_(75066)
for s in _n_(75067, "sums", lambda: sums):
    _l_(75081)

    if _n_(75068, "s", lambda: s)[0] == True and _n_(75069, "s", lambda: s)[1] not in _n_(75070, "result", lambda: result):
        _l_(75080)

        _c_(75074, _a_(75072, _n_(75071, "result", lambda: result), "add"), _n_(75073, "s", lambda: s)[1])
        _l_(75075)
        _c_(75078, _n_(75076, "print", lambda: print), _n_(75077, "result", lambda: result))
        _l_(75079)