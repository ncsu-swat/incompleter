# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from itertools import accumulate
    _l_(57492)

except ImportError:
    pass

def running_max_product(iters):
    _l_(57498)

    aux = _c_(57496, _n_(57493, "accumulate", lambda: accumulate), _n_(57494, "iters", lambda: iters), _n_(57495, "max", lambda: max))
    _l_(57497)
    return aux
_c_(57500, _n_(57499, "print", lambda: print), 'Running maximum value of a list:')
_l_(57501)
for i in _n_(57502, "result", lambda: result):
    _l_(57507)

    _c_(57505, _n_(57503, "print", lambda: print), _n_(57504, "i", lambda: i))
    _l_(57506)
result = _c_(57509, _n_(57508, "running_max_product", lambda: running_max_product), (1, 3, 3, 7, 9, 8, 10, 9, 8, 14, 11, 15, 7))
_l_(57510)
_c_(57512, _n_(57511, "print", lambda: print), 'Running maximum value of a Tuple:')
_l_(57513)
for i in _n_(57514, "result", lambda: result):
    _l_(57519)

    _c_(57517, _n_(57515, "print", lambda: print), _n_(57516, "i", lambda: i))
    _l_(57518)

def running_min_product(iters):
    _l_(57525)

    aux = _c_(57523, _n_(57520, "accumulate", lambda: accumulate), _n_(57521, "iters", lambda: iters), _n_(57522, "min", lambda: min))
    _l_(57524)
    return aux
result = _c_(57527, _n_(57526, "running_min_product", lambda: running_min_product), [3, 2, 7, 9, 8, 10, 11, 12, 1, 14, 11, 12, 7])
_l_(57528)
_c_(57530, _n_(57529, "print", lambda: print), 'Running minimum value of a list:')
_l_(57531)
for i in _n_(57532, "result", lambda: result):
    _l_(57537)

    _c_(57535, _n_(57533, "print", lambda: print), _n_(57534, "i", lambda: i))
    _l_(57536)
result = _c_(57539, _n_(57538, "running_min_product", lambda: running_min_product), (1, 3, 3, 7, 9, 8, 10, 9, 8, 0, 11, 15, 7))
_l_(57540)
_c_(57542, _n_(57541, "print", lambda: print), 'Running minimum value of a Tuple:')
_l_(57543)
for i in _n_(57544, "result", lambda: result):
    _l_(57549)

    _c_(57547, _n_(57545, "print", lambda: print), _n_(57546, "i", lambda: i))
    _l_(57548)