# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import itertools
    _l_(74917)

except ImportError:
    pass
try:
    from functools import partial
    _l_(74919)

except ImportError:
    pass
X = [10, 20, 20, 20]
_l_(74920)
Y = [10, 20, 30, 40]
_l_(74921)
Z = [10, 30, 40, 20]
_l_(74922)
T = 70
_l_(74923)

def check_sum_array(N, *nums):
    _l_(74934)

    if _c_(74927, _n_(74924, "sum", lambda: sum), (_n_(74925, "x", lambda: x) for x in _n_(74926, "nums", lambda: nums))) == _n_(74928, "N", lambda: N):
        _l_(74933)

        aux = (True, _n_(74929, "nums", lambda: nums))
        _l_(74930)
        return aux
    else:
        aux = (False, _n_(74931, "nums", lambda: nums))
        _l_(74932)
        return aux
pro = _c_(74940, _a_(74936, _n_(74935, "itertools", lambda: itertools), "product"), _n_(74937, "X", lambda: X), _n_(74938, "Y", lambda: Y), _n_(74939, "Z", lambda: Z))
_l_(74941)
func = _c_(74945, _n_(74942, "partial", lambda: partial), _n_(74943, "check_sum_array", lambda: check_sum_array), _n_(74944, "T", lambda: T))
_l_(74946)
sums = _c_(74953, _n_(74947, "list", lambda: list), _c_(74952, _a_(74949, _n_(74948, "itertools", lambda: itertools), "starmap"), _n_(74950, "func", lambda: func), _n_(74951, "pro", lambda: pro)))
_l_(74954)
for s in _n_(74955, "sums", lambda: sums):
    _l_(74969)

    if _n_(74956, "s", lambda: s)[0] == True and _n_(74957, "s", lambda: s)[1] not in _n_(74958, "result", lambda: result):
        _l_(74968)

        _c_(74962, _a_(74960, _n_(74959, "result", lambda: result), "add"), _n_(74961, "s", lambda: s)[1])
        _l_(74963)
        _c_(74966, _n_(74964, "print", lambda: print), _n_(74965, "result", lambda: result))
        _l_(74967)