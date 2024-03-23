# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(62786)

except ImportError:
    pass
_c_(62789, _n_(62787, "print", lambda: print), 'Original array: ', _n_(62788, "x", lambda: x))
_l_(62790)
_c_(62796, _n_(62791, "print", lambda: print), 'Maximum Values: ', _c_(62795, _a_(62793, _n_(62792, "np", lambda: np), "argmax"), _n_(62794, "x", lambda: x)))
_l_(62797)
_c_(62803, _n_(62798, "print", lambda: print), 'Minimum Values: ', _c_(62802, _a_(62800, _n_(62799, "np", lambda: np), "argmin"), _n_(62801, "x", lambda: x)))
_l_(62804)