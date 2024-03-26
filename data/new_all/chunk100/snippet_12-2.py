# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(101428)

except ImportError:
    pass
_c_(101430, _n_(101429, "print", lambda: print), 'Original array:')
_l_(101431)
_c_(101434, _n_(101432, "print", lambda: print), _n_(101433, "nums", lambda: nums))
_l_(101435)
p = 2
_l_(101436)
new_nums = _c_(101446, _a_(101438, _n_(101437, "np", lambda: np), "zeros"), _c_(101441, _n_(101439, "len", lambda: len), _n_(101440, "nums", lambda: nums)) + (_c_(101444, _n_(101442, "len", lambda: len), _n_(101443, "nums", lambda: nums)) - 1) * _n_(101445, "p", lambda: p))
_l_(101447)
_n_(101448, "new_nums", lambda: new_nums)[::_n_(101449, "p", lambda: p) + 1] = _n_(101450, "nums", lambda: nums)
_l_(101451)
_c_(101453, _n_(101452, "print", lambda: print), '\nNew array:')
_l_(101454)
_c_(101457, _n_(101455, "print", lambda: print), _n_(101456, "new_nums", lambda: new_nums))
_l_(101458)