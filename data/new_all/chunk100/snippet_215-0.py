# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(105470)

except ImportError:
    pass
nums = _c_(105474, _a_(105473, _a_(105472, _n_(105471, "np", lambda: np), "random"), "randint"), 0, 4, (6, 3))
_l_(105475)
_c_(105477, _n_(105476, "print", lambda: print), 'Original vector:')
_l_(105478)
_c_(105481, _n_(105479, "print", lambda: print), _n_(105480, "nums", lambda: nums))
_l_(105482)
new_nums = _c_(105488, _a_(105485, _a_(105484, _n_(105483, "np", lambda: np), "logical_and"), "reduce"), _n_(105486, "nums", lambda: nums)[:, 1:] == _n_(105487, "nums", lambda: nums)[:, :-1], axis=1)
_l_(105489)
_c_(105491, _n_(105490, "print", lambda: print), '\nRows with unequal values:')
_l_(105492)
_c_(105495, _n_(105493, "print", lambda: print), _n_(105494, "result", lambda: result))
_l_(105496)