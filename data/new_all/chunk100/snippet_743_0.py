# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import itertools
    _l_(74865)

except ImportError:
    pass
try:
    from functools import partial
    _l_(74867)

except ImportError:
    pass
X = [10, 20, 20, 20]
_l_(74868)
Y = [10, 20, 30, 40]
_l_(74869)
Z = [10, 30, 40, 20]
_l_(74870)
T = 70
_l_(74871)

def check_sum_array(N, *nums):
    _l_(74882)

    if _c_(74875, _n_(74872, "sum", lambda: sum), (_n_(74873, "x", lambda: x) for x in _n_(74874, "nums", lambda: nums))) == _n_(74876, "N", lambda: N):
        _l_(74881)

        aux = (True, _n_(74877, "nums", lambda: nums))
        _l_(74878)
        return aux
    else:
        aux = (False, _n_(74879, "nums", lambda: nums))
        _l_(74880)
        return aux
pro = _c_(74888, _a_(74884, _n_(74883, "itertools", lambda: itertools), "product"), _n_(74885, "X", lambda: X), _n_(74886, "Y", lambda: Y), _n_(74887, "Z", lambda: Z))
_l_(74889)
sums = _c_(74896, _n_(74890, "list", lambda: list), _c_(74895, _a_(74892, _n_(74891, "itertools", lambda: itertools), "starmap"), _n_(74893, "func", lambda: func), _n_(74894, "pro", lambda: pro)))
_l_(74897)
result = _c_(74899, _n_(74898, "set", lambda: set))
_l_(74900)
for s in _n_(74901, "sums", lambda: sums):
    _l_(74915)

    if _n_(74902, "s", lambda: s)[0] == True and _n_(74903, "s", lambda: s)[1] not in _n_(74904, "result", lambda: result):
        _l_(74914)

        _c_(74908, _a_(74906, _n_(74905, "result", lambda: result), "add"), _n_(74907, "s", lambda: s)[1])
        _l_(74909)
        _c_(74912, _n_(74910, "print", lambda: print), _n_(74911, "result", lambda: result))
        _l_(74913)