# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(112139)

except ImportError:
    pass
try:
    import os
    _l_(112141)

except ImportError:
    pass
_c_(112143, _n_(112142, "print", lambda: print), 'Original array:')
_l_(112144)
_c_(112147, _n_(112145, "print", lambda: print), _n_(112146, "a", lambda: a))
_l_(112148)
a_bytes = _c_(112151, _a_(112150, _n_(112149, "a", lambda: a), "tostring"))
_l_(112152)
a2 = _c_(112158, _a_(112154, _n_(112153, "np", lambda: np), "fromstring"), _n_(112155, "a_bytes", lambda: a_bytes), dtype=_a_(112157, _n_(112156, "a", lambda: a), "dtype"))
_l_(112159)
_c_(112161, _n_(112160, "print", lambda: print), 'After loading, content of the text file:')
_l_(112162)
_c_(112165, _n_(112163, "print", lambda: print), _n_(112164, "a2", lambda: a2))
_l_(112166)
_c_(112173, _n_(112167, "print", lambda: print), _c_(112172, _a_(112169, _n_(112168, "np", lambda: np), "array_equal"), _n_(112170, "a", lambda: a), _n_(112171, "a2", lambda: a2)))
_l_(112174)