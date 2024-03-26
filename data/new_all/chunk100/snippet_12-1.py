# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(101393)

except ImportError:
    pass
nums = _c_(101396, _a_(101395, _n_(101394, "np", lambda: np), "array"), [1, 2, 3, 4, 5, 6, 7, 8])
_l_(101397)
_c_(101399, _n_(101398, "print", lambda: print), 'Original array:')
_l_(101400)
_c_(101403, _n_(101401, "print", lambda: print), _n_(101402, "nums", lambda: nums))
_l_(101404)
new_nums = _c_(101414, _a_(101406, _n_(101405, "np", lambda: np), "zeros"), _c_(101409, _n_(101407, "len", lambda: len), _n_(101408, "nums", lambda: nums)) + (_c_(101412, _n_(101410, "len", lambda: len), _n_(101411, "nums", lambda: nums)) - 1) * _n_(101413, "p", lambda: p))
_l_(101415)
_n_(101416, "new_nums", lambda: new_nums)[::_n_(101417, "p", lambda: p) + 1] = _n_(101418, "nums", lambda: nums)
_l_(101419)
_c_(101421, _n_(101420, "print", lambda: print), '\nNew array:')
_l_(101422)
_c_(101425, _n_(101423, "print", lambda: print), _n_(101424, "new_nums", lambda: new_nums))
_l_(101426)