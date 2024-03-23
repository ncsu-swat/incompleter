# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(50701)

except ImportError:
    pass
_c_(50703, _n_(50702, "print", lambda: print), 'Original arrays:')
_l_(50704)
_c_(50707, _n_(50705, "print", lambda: print), _n_(50706, "array_nums1", lambda: array_nums1))
_l_(50708)
result = _n_(50709, "array_nums1", lambda: array_nums1)[(_n_(50710, "array_nums1", lambda: array_nums1) > 6) & (_n_(50711, "array_nums1", lambda: array_nums1) % 3 == 0)]
_l_(50712)
_c_(50714, _n_(50713, "print", lambda: print), '\nItems greater than 6 and a multiple of 3 of the said array:')
_l_(50715)
_c_(50718, _n_(50716, "print", lambda: print), _n_(50717, "result", lambda: result))
_l_(50719)