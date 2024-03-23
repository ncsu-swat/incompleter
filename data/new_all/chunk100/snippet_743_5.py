# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import itertools
    _l_(75139)

except ImportError:
    pass
try:
    from functools import partial
    _l_(75141)

except ImportError:
    pass
X = [10, 20, 20, 20]
_l_(75142)
Y = [10, 20, 30, 40]
_l_(75143)
Z = [10, 30, 40, 20]
_l_(75144)
T = 70
_l_(75145)

def check_sum_array(N, *nums):
    _l_(75156)

    if _c_(75149, _n_(75146, "sum", lambda: sum), (_n_(75147, "x", lambda: x) for x in _n_(75148, "nums", lambda: nums))) == _n_(75150, "N", lambda: N):
        _l_(75155)

        aux = (True, _n_(75151, "nums", lambda: nums))
        _l_(75152)
        return aux
    else:
        aux = (False, _n_(75153, "nums", lambda: nums))
        _l_(75154)
        return aux
func = _c_(75160, _n_(75157, "partial", lambda: partial), _n_(75158, "check_sum_array", lambda: check_sum_array), _n_(75159, "T", lambda: T))
_l_(75161)
sums = _c_(75168, _n_(75162, "list", lambda: list), _c_(75167, _a_(75164, _n_(75163, "itertools", lambda: itertools), "starmap"), _n_(75165, "func", lambda: func), _n_(75166, "pro", lambda: pro)))
_l_(75169)
result = _c_(75171, _n_(75170, "set", lambda: set))
_l_(75172)
for s in _n_(75173, "sums", lambda: sums):
    _l_(75187)

    if _n_(75174, "s", lambda: s)[0] == True and _n_(75175, "s", lambda: s)[1] not in _n_(75176, "result", lambda: result):
        _l_(75186)

        _c_(75180, _a_(75178, _n_(75177, "result", lambda: result), "add"), _n_(75179, "s", lambda: s)[1])
        _l_(75181)
        _c_(75184, _n_(75182, "print", lambda: print), _n_(75183, "result", lambda: result))
        _l_(75185)