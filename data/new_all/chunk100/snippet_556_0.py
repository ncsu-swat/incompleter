# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from itertools import accumulate
    _l_(57315)

except ImportError:
    pass

def running_max_product(iters):
    _l_(57321)

    aux = _c_(57319, _n_(57316, "accumulate", lambda: accumulate), _n_(57317, "iters", lambda: iters), _n_(57318, "max", lambda: max))
    _l_(57320)
    return aux
result = _c_(57323, _n_(57322, "running_max_product", lambda: running_max_product), [1, 3, 2, 7, 9, 8, 10, 11, 12, 14, 11, 12, 7])
_l_(57324)
_c_(57326, _n_(57325, "print", lambda: print), 'Running maximum value of a list:')
_l_(57327)
for i in _n_(57328, "result", lambda: result):
    _l_(57333)

    _c_(57331, _n_(57329, "print", lambda: print), _n_(57330, "i", lambda: i))
    _l_(57332)
result = _c_(57335, _n_(57334, "running_max_product", lambda: running_max_product), (1, 3, 3, 7, 9, 8, 10, 9, 8, 14, 11, 15, 7))
_l_(57336)
_c_(57338, _n_(57337, "print", lambda: print), 'Running maximum value of a Tuple:')
_l_(57339)
for i in _n_(57340, "result", lambda: result):
    _l_(57345)

    _c_(57343, _n_(57341, "print", lambda: print), _n_(57342, "i", lambda: i))
    _l_(57344)

def running_min_product(iters):
    _l_(57351)

    aux = _c_(57349, _n_(57346, "accumulate", lambda: accumulate), _n_(57347, "iters", lambda: iters), _n_(57348, "min", lambda: min))
    _l_(57350)
    return aux
result = _c_(57353, _n_(57352, "running_min_product", lambda: running_min_product), [3, 2, 7, 9, 8, 10, 11, 12, 1, 14, 11, 12, 7])
_l_(57354)
_c_(57356, _n_(57355, "print", lambda: print), 'Running minimum value of a list:')
_l_(57357)
for i in _n_(57358, "result", lambda: result):
    _l_(57363)

    _c_(57361, _n_(57359, "print", lambda: print), _n_(57360, "i", lambda: i))
    _l_(57362)
_c_(57365, _n_(57364, "print", lambda: print), 'Running minimum value of a Tuple:')
_l_(57366)
for i in _n_(57367, "result", lambda: result):
    _l_(57372)

    _c_(57370, _n_(57368, "print", lambda: print), _n_(57369, "i", lambda: i))
    _l_(57371)