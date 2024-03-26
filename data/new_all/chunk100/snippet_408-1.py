# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(114797)

except ImportError:
    pass
_c_(114799, _n_(114798, "print", lambda: print), 'Original array:')
_l_(114800)
_c_(114803, _n_(114801, "print", lambda: print), _n_(114802, "nums", lambda: nums))
_l_(114804)
_c_(114806, _n_(114805, "print", lambda: print), '\nExtract array of shape (6,6,3) from the said array:')
_l_(114807)
new_nums = _n_(114808, "nums", lambda: nums)[:6, :6, :]
_l_(114809)
_c_(114812, _n_(114810, "print", lambda: print), _n_(114811, "new_nums", lambda: new_nums))
_l_(114813)