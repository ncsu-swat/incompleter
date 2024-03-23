# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from itertools import accumulate
    _l_(57433)

except ImportError:
    pass

def running_max_product(iters):
    _l_(57439)

    aux = _c_(57437, _n_(57434, "accumulate", lambda: accumulate), _n_(57435, "iters", lambda: iters), _n_(57436, "max", lambda: max))
    _l_(57438)
    return aux
result = _c_(57441, _n_(57440, "running_max_product", lambda: running_max_product), [1, 3, 2, 7, 9, 8, 10, 11, 12, 14, 11, 12, 7])
_l_(57442)
_c_(57444, _n_(57443, "print", lambda: print), 'Running maximum value of a list:')
_l_(57445)
for i in _n_(57446, "result", lambda: result):
    _l_(57451)

    _c_(57449, _n_(57447, "print", lambda: print), _n_(57448, "i", lambda: i))
    _l_(57450)
_c_(57453, _n_(57452, "print", lambda: print), 'Running maximum value of a Tuple:')
_l_(57454)
for i in _n_(57455, "result", lambda: result):
    _l_(57460)

    _c_(57458, _n_(57456, "print", lambda: print), _n_(57457, "i", lambda: i))
    _l_(57459)

def running_min_product(iters):
    _l_(57466)

    aux = _c_(57464, _n_(57461, "accumulate", lambda: accumulate), _n_(57462, "iters", lambda: iters), _n_(57463, "min", lambda: min))
    _l_(57465)
    return aux
result = _c_(57468, _n_(57467, "running_min_product", lambda: running_min_product), [3, 2, 7, 9, 8, 10, 11, 12, 1, 14, 11, 12, 7])
_l_(57469)
_c_(57471, _n_(57470, "print", lambda: print), 'Running minimum value of a list:')
_l_(57472)
for i in _n_(57473, "result", lambda: result):
    _l_(57478)

    _c_(57476, _n_(57474, "print", lambda: print), _n_(57475, "i", lambda: i))
    _l_(57477)
result = _c_(57480, _n_(57479, "running_min_product", lambda: running_min_product), (1, 3, 3, 7, 9, 8, 10, 9, 8, 0, 11, 15, 7))
_l_(57481)
_c_(57483, _n_(57482, "print", lambda: print), 'Running minimum value of a Tuple:')
_l_(57484)
for i in _n_(57485, "result", lambda: result):
    _l_(57490)

    _c_(57488, _n_(57486, "print", lambda: print), _n_(57487, "i", lambda: i))
    _l_(57489)