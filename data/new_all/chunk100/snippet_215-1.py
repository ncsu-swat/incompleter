# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(105498)

except ImportError:
    pass
_c_(105500, _n_(105499, "print", lambda: print), 'Original vector:')
_l_(105501)
_c_(105504, _n_(105502, "print", lambda: print), _n_(105503, "nums", lambda: nums))
_l_(105505)
new_nums = _c_(105511, _a_(105508, _a_(105507, _n_(105506, "np", lambda: np), "logical_and"), "reduce"), _n_(105509, "nums", lambda: nums)[:, 1:] == _n_(105510, "nums", lambda: nums)[:, :-1], axis=1)
_l_(105512)
result = _n_(105513, "nums", lambda: nums)[~_n_(105514, "new_nums", lambda: new_nums)]
_l_(105515)
_c_(105517, _n_(105516, "print", lambda: print), '\nRows with unequal values:')
_l_(105518)
_c_(105521, _n_(105519, "print", lambda: print), _n_(105520, "result", lambda: result))
_l_(105522)