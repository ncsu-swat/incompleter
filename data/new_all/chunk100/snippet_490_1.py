# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(51367)

except ImportError:
    pass
try:
    import os
    _l_(51369)

except ImportError:
    pass
x = _c_(51372, _a_(51371, _n_(51370, "np", lambda: np), "arange"), 10)
_l_(51373)
y = _c_(51376, _a_(51375, _n_(51374, "np", lambda: np), "arange"), 11, 20)
_l_(51377)
_c_(51379, _n_(51378, "print", lambda: print), 'Original arrays:')
_l_(51380)
_c_(51383, _n_(51381, "print", lambda: print), _n_(51382, "x", lambda: x))
_l_(51384)
_c_(51387, _n_(51385, "print", lambda: print), _n_(51386, "y", lambda: y))
_l_(51388)
_c_(51393, _a_(51390, _n_(51389, "np", lambda: np), "savez"), 'temp_arra.npz', x=_n_(51391, "x", lambda: x), y=_n_(51392, "y", lambda: y))
_l_(51394)
_c_(51396, _n_(51395, "print", lambda: print), "Load arrays from the 'temp_arra.npz' file:")
_l_(51397)
with _c_(51400, _a_(51399, _n_(51398, "np", lambda: np), "load"), 'temp_arra.npz') as data:
    _l_(51411)

    y2 = _n_(51401, "data", lambda: data)['y']
    _l_(51402)
    _c_(51405, _n_(51403, "print", lambda: print), _n_(51404, "x2", lambda: x2))
    _l_(51406)
    _c_(51409, _n_(51407, "print", lambda: print), _n_(51408, "y2", lambda: y2))
    _l_(51410)