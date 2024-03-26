# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(103739)

except ImportError:
    pass
_c_(103741, _n_(103740, "print", lambda: print), 'Original arrays:')
_l_(103742)
_c_(103745, _n_(103743, "print", lambda: print), _n_(103744, "x", lambda: x))
_l_(103746)
new_array = _c_(103750, _a_(103748, _n_(103747, "np", lambda: np), "transpose"), _n_(103749, "x", lambda: x))
_l_(103751)
_c_(103753, _n_(103752, "print", lambda: print), 'After reverse the dimensions:')
_l_(103754)
_c_(103757, _n_(103755, "print", lambda: print), _n_(103756, "new_array", lambda: new_array))
_l_(103758)