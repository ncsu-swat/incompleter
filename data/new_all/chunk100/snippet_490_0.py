# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(51323)

except ImportError:
    pass
try:
    import os
    _l_(51325)

except ImportError:
    pass
y = _c_(51328, _a_(51327, _n_(51326, "np", lambda: np), "arange"), 11, 20)
_l_(51329)
_c_(51331, _n_(51330, "print", lambda: print), 'Original arrays:')
_l_(51332)
_c_(51335, _n_(51333, "print", lambda: print), _n_(51334, "x", lambda: x))
_l_(51336)
_c_(51339, _n_(51337, "print", lambda: print), _n_(51338, "y", lambda: y))
_l_(51340)
_c_(51345, _a_(51342, _n_(51341, "np", lambda: np), "savez"), 'temp_arra.npz', x=_n_(51343, "x", lambda: x), y=_n_(51344, "y", lambda: y))
_l_(51346)
_c_(51348, _n_(51347, "print", lambda: print), "Load arrays from the 'temp_arra.npz' file:")
_l_(51349)
with _c_(51352, _a_(51351, _n_(51350, "np", lambda: np), "load"), 'temp_arra.npz') as data:
    _l_(51365)

    x2 = _n_(51353, "data", lambda: data)['x']
    _l_(51354)
    y2 = _n_(51355, "data", lambda: data)['y']
    _l_(51356)
    _c_(51359, _n_(51357, "print", lambda: print), _n_(51358, "x2", lambda: x2))
    _l_(51360)
    _c_(51363, _n_(51361, "print", lambda: print), _n_(51362, "y2", lambda: y2))
    _l_(51364)