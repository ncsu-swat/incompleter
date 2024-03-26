# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(112068)

except ImportError:
    pass
try:
    import os
    _l_(112070)

except ImportError:
    pass
a = _c_(112073, _a_(112072, _n_(112071, "np", lambda: np), "array"), [1, 2, 3, 4, 5, 6])
_l_(112074)
_c_(112076, _n_(112075, "print", lambda: print), 'Original array:')
_l_(112077)
_c_(112080, _n_(112078, "print", lambda: print), _n_(112079, "a", lambda: a))
_l_(112081)
a_bytes = _c_(112084, _a_(112083, _n_(112082, "a", lambda: a), "tostring"))
_l_(112085)
_c_(112087, _n_(112086, "print", lambda: print), 'After loading, content of the text file:')
_l_(112088)
_c_(112091, _n_(112089, "print", lambda: print), _n_(112090, "a2", lambda: a2))
_l_(112092)
_c_(112099, _n_(112093, "print", lambda: print), _c_(112098, _a_(112095, _n_(112094, "np", lambda: np), "array_equal"), _n_(112096, "a", lambda: a), _n_(112097, "a2", lambda: a2)))
_l_(112100)