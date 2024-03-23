# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from itertools import accumulate
    _l_(57374)

except ImportError:
    pass

def running_max_product(iters):
    _l_(57380)

    aux = _c_(57378, _n_(57375, "accumulate", lambda: accumulate), _n_(57376, "iters", lambda: iters), _n_(57377, "max", lambda: max))
    _l_(57379)
    return aux
result = _c_(57382, _n_(57381, "running_max_product", lambda: running_max_product), [1, 3, 2, 7, 9, 8, 10, 11, 12, 14, 11, 12, 7])
_l_(57383)
_c_(57385, _n_(57384, "print", lambda: print), 'Running maximum value of a list:')
_l_(57386)
for i in _n_(57387, "result", lambda: result):
    _l_(57392)

    _c_(57390, _n_(57388, "print", lambda: print), _n_(57389, "i", lambda: i))
    _l_(57391)
result = _c_(57394, _n_(57393, "running_max_product", lambda: running_max_product), (1, 3, 3, 7, 9, 8, 10, 9, 8, 14, 11, 15, 7))
_l_(57395)
_c_(57397, _n_(57396, "print", lambda: print), 'Running maximum value of a Tuple:')
_l_(57398)
for i in _n_(57399, "result", lambda: result):
    _l_(57404)

    _c_(57402, _n_(57400, "print", lambda: print), _n_(57401, "i", lambda: i))
    _l_(57403)

def running_min_product(iters):
    _l_(57410)

    aux = _c_(57408, _n_(57405, "accumulate", lambda: accumulate), _n_(57406, "iters", lambda: iters), _n_(57407, "min", lambda: min))
    _l_(57409)
    return aux
_c_(57412, _n_(57411, "print", lambda: print), 'Running minimum value of a list:')
_l_(57413)
for i in _n_(57414, "result", lambda: result):
    _l_(57419)

    _c_(57417, _n_(57415, "print", lambda: print), _n_(57416, "i", lambda: i))
    _l_(57418)
result = _c_(57421, _n_(57420, "running_min_product", lambda: running_min_product), (1, 3, 3, 7, 9, 8, 10, 9, 8, 0, 11, 15, 7))
_l_(57422)
_c_(57424, _n_(57423, "print", lambda: print), 'Running minimum value of a Tuple:')
_l_(57425)
for i in _n_(57426, "result", lambda: result):
    _l_(57431)

    _c_(57429, _n_(57427, "print", lambda: print), _n_(57428, "i", lambda: i))
    _l_(57430)