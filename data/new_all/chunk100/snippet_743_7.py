# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import itertools
    _l_(75245)

except ImportError:
    pass
try:
    from functools import partial
    _l_(75247)

except ImportError:
    pass
X = [10, 20, 20, 20]
_l_(75248)
Y = [10, 20, 30, 40]
_l_(75249)
Z = [10, 30, 40, 20]
_l_(75250)
T = 70
_l_(75251)

def check_sum_array(N, *nums):
    _l_(75262)

    if _c_(75255, _n_(75252, "sum", lambda: sum), (_n_(75253, "x", lambda: x) for x in _n_(75254, "nums", lambda: nums))) == _n_(75256, "N", lambda: N):
        _l_(75261)

        aux = (True, _n_(75257, "nums", lambda: nums))
        _l_(75258)
        return aux
    else:
        aux = (False, _n_(75259, "nums", lambda: nums))
        _l_(75260)
        return aux
pro = _c_(75268, _a_(75264, _n_(75263, "itertools", lambda: itertools), "product"), _n_(75265, "X", lambda: X), _n_(75266, "Y", lambda: Y), _n_(75267, "Z", lambda: Z))
_l_(75269)
func = _c_(75273, _n_(75270, "partial", lambda: partial), _n_(75271, "check_sum_array", lambda: check_sum_array), _n_(75272, "T", lambda: T))
_l_(75274)
result = _c_(75276, _n_(75275, "set", lambda: set))
_l_(75277)
for s in _n_(75278, "sums", lambda: sums):
    _l_(75292)

    if _n_(75279, "s", lambda: s)[0] == True and _n_(75280, "s", lambda: s)[1] not in _n_(75281, "result", lambda: result):
        _l_(75291)

        _c_(75285, _a_(75283, _n_(75282, "result", lambda: result), "add"), _n_(75284, "s", lambda: s)[1])
        _l_(75286)
        _c_(75289, _n_(75287, "print", lambda: print), _n_(75288, "result", lambda: result))
        _l_(75290)