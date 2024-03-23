# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(8654)

except ImportError:
    pass
nums = _c_(8657, _a_(8656, _n_(8655, "np", lambda: np), "array"), [1, 2, 3, 4, 5, 6, 7, 8])
_l_(8658)
_c_(8660, _n_(8659, "print", lambda: print), 'Original array:')
_l_(8661)
_c_(8664, _n_(8662, "print", lambda: print), _n_(8663, "nums", lambda: nums))
_l_(8665)
new_nums = _c_(8675, _a_(8667, _n_(8666, "np", lambda: np), "zeros"), _c_(8670, _n_(8668, "len", lambda: len), _n_(8669, "nums", lambda: nums)) + (_c_(8673, _n_(8671, "len", lambda: len), _n_(8672, "nums", lambda: nums)) - 1) * _n_(8674, "p", lambda: p))
_l_(8676)
_n_(8677, "new_nums", lambda: new_nums)[::_n_(8678, "p", lambda: p) + 1] = _n_(8679, "nums", lambda: nums)
_l_(8680)
_c_(8682, _n_(8681, "print", lambda: print), '\nNew array:')
_l_(8683)
_c_(8686, _n_(8684, "print", lambda: print), _n_(8685, "new_nums", lambda: new_nums))
_l_(8687)