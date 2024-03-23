# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(8622)

except ImportError:
    pass
_c_(8624, _n_(8623, "print", lambda: print), 'Original array:')
_l_(8625)
_c_(8628, _n_(8626, "print", lambda: print), _n_(8627, "nums", lambda: nums))
_l_(8629)
p = 2
_l_(8630)
new_nums = _c_(8640, _a_(8632, _n_(8631, "np", lambda: np), "zeros"), _c_(8635, _n_(8633, "len", lambda: len), _n_(8634, "nums", lambda: nums)) + (_c_(8638, _n_(8636, "len", lambda: len), _n_(8637, "nums", lambda: nums)) - 1) * _n_(8639, "p", lambda: p))
_l_(8641)
_n_(8642, "new_nums", lambda: new_nums)[::_n_(8643, "p", lambda: p) + 1] = _n_(8644, "nums", lambda: nums)
_l_(8645)
_c_(8647, _n_(8646, "print", lambda: print), '\nNew array:')
_l_(8648)
_c_(8651, _n_(8649, "print", lambda: print), _n_(8650, "new_nums", lambda: new_nums))
_l_(8652)