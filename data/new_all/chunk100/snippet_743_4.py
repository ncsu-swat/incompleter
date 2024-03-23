# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import itertools
    _l_(75083)

except ImportError:
    pass
try:
    from functools import partial
    _l_(75085)

except ImportError:
    pass
Y = [10, 20, 30, 40]
_l_(75086)
Z = [10, 30, 40, 20]
_l_(75087)
T = 70
_l_(75088)

def check_sum_array(N, *nums):
    _l_(75099)

    if _c_(75092, _n_(75089, "sum", lambda: sum), (_n_(75090, "x", lambda: x) for x in _n_(75091, "nums", lambda: nums))) == _n_(75093, "N", lambda: N):
        _l_(75098)

        aux = (True, _n_(75094, "nums", lambda: nums))
        _l_(75095)
        return aux
    else:
        aux = (False, _n_(75096, "nums", lambda: nums))
        _l_(75097)
        return aux
pro = _c_(75105, _a_(75101, _n_(75100, "itertools", lambda: itertools), "product"), _n_(75102, "X", lambda: X), _n_(75103, "Y", lambda: Y), _n_(75104, "Z", lambda: Z))
_l_(75106)
func = _c_(75110, _n_(75107, "partial", lambda: partial), _n_(75108, "check_sum_array", lambda: check_sum_array), _n_(75109, "T", lambda: T))
_l_(75111)
sums = _c_(75118, _n_(75112, "list", lambda: list), _c_(75117, _a_(75114, _n_(75113, "itertools", lambda: itertools), "starmap"), _n_(75115, "func", lambda: func), _n_(75116, "pro", lambda: pro)))
_l_(75119)
result = _c_(75121, _n_(75120, "set", lambda: set))
_l_(75122)
for s in _n_(75123, "sums", lambda: sums):
    _l_(75137)

    if _n_(75124, "s", lambda: s)[0] == True and _n_(75125, "s", lambda: s)[1] not in _n_(75126, "result", lambda: result):
        _l_(75136)

        _c_(75130, _a_(75128, _n_(75127, "result", lambda: result), "add"), _n_(75129, "s", lambda: s)[1])
        _l_(75131)
        _c_(75134, _n_(75132, "print", lambda: print), _n_(75133, "result", lambda: result))
        _l_(75135)