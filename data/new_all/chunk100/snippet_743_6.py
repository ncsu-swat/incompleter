# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import itertools
    _l_(75189)

except ImportError:
    pass
try:
    from functools import partial
    _l_(75191)

except ImportError:
    pass
X = [10, 20, 20, 20]
_l_(75192)
Y = [10, 20, 30, 40]
_l_(75193)
T = 70
_l_(75194)

def check_sum_array(N, *nums):
    _l_(75205)

    if _c_(75198, _n_(75195, "sum", lambda: sum), (_n_(75196, "x", lambda: x) for x in _n_(75197, "nums", lambda: nums))) == _n_(75199, "N", lambda: N):
        _l_(75204)

        aux = (True, _n_(75200, "nums", lambda: nums))
        _l_(75201)
        return aux
    else:
        aux = (False, _n_(75202, "nums", lambda: nums))
        _l_(75203)
        return aux
pro = _c_(75211, _a_(75207, _n_(75206, "itertools", lambda: itertools), "product"), _n_(75208, "X", lambda: X), _n_(75209, "Y", lambda: Y), _n_(75210, "Z", lambda: Z))
_l_(75212)
func = _c_(75216, _n_(75213, "partial", lambda: partial), _n_(75214, "check_sum_array", lambda: check_sum_array), _n_(75215, "T", lambda: T))
_l_(75217)
sums = _c_(75224, _n_(75218, "list", lambda: list), _c_(75223, _a_(75220, _n_(75219, "itertools", lambda: itertools), "starmap"), _n_(75221, "func", lambda: func), _n_(75222, "pro", lambda: pro)))
_l_(75225)
result = _c_(75227, _n_(75226, "set", lambda: set))
_l_(75228)
for s in _n_(75229, "sums", lambda: sums):
    _l_(75243)

    if _n_(75230, "s", lambda: s)[0] == True and _n_(75231, "s", lambda: s)[1] not in _n_(75232, "result", lambda: result):
        _l_(75242)

        _c_(75236, _a_(75234, _n_(75233, "result", lambda: result), "add"), _n_(75235, "s", lambda: s)[1])
        _l_(75237)
        _c_(75240, _n_(75238, "print", lambda: print), _n_(75239, "result", lambda: result))
        _l_(75241)