# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(98370)

except ImportError:
    pass
_c_(98372, _n_(98371, "print", lambda: print), 'Original arrays:')
_l_(98373)
_c_(98376, _n_(98374, "print", lambda: print), _n_(98375, "x", lambda: x))
_l_(98377)
_c_(98379, _n_(98378, "print", lambda: print), '\nArray with size 2x2 from the said array:')
_l_(98380)
new_array1 = _c_(98384, _a_(98382, _n_(98381, "np", lambda: np), "resize"), _n_(98383, "x", lambda: x), (2, 2))
_l_(98385)
_c_(98388, _n_(98386, "print", lambda: print), _n_(98387, "new_array1", lambda: new_array1))
_l_(98389)
_c_(98391, _n_(98390, "print", lambda: print), '\nArray with size 6x6 from the said array:')
_l_(98392)
new_array2 = _c_(98396, _a_(98394, _n_(98393, "np", lambda: np), "resize"), _n_(98395, "x", lambda: x), (6, 6))
_l_(98397)
_c_(98400, _n_(98398, "print", lambda: print), _n_(98399, "new_array2", lambda: new_array2))
_l_(98401)