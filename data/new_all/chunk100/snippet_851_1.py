# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(84487)

except ImportError:
    pass
_c_(84489, _n_(84488, "print", lambda: print), 'Original array: ')
_l_(84490)
_c_(84493, _n_(84491, "print", lambda: print), _n_(84492, "x", lambda: x))
_l_(84494)
_c_(84496, _n_(84495, "print", lambda: print), '\ne^x, element-wise of the said:')
_l_(84497)
r = _c_(84501, _a_(84499, _n_(84498, "np", lambda: np), "exp"), _n_(84500, "x", lambda: x))
_l_(84502)
_c_(84505, _n_(84503, "print", lambda: print), _n_(84504, "r", lambda: r))
_l_(84506)