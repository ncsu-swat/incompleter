# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(14554)

except ImportError:
    pass
_c_(14556, _n_(14555, "print", lambda: print), '\nOriginal arrays:')
_l_(14557)
x = _c_(14562, _a_(14561, _c_(14560, _a_(14559, _n_(14558, "np", lambda: np), "arange"), 9), "reshape"), 3, 3)
_l_(14563)
_c_(14565, _n_(14564, "print", lambda: print), 'Array-1')
_l_(14566)
_c_(14569, _n_(14567, "print", lambda: print), _n_(14568, "x", lambda: x))
_l_(14570)
_c_(14572, _n_(14571, "print", lambda: print), 'Array-2')
_l_(14573)
_c_(14576, _n_(14574, "print", lambda: print), _n_(14575, "y", lambda: y))
_l_(14577)
new_array = _c_(14582, _a_(14579, _n_(14578, "np", lambda: np), "hstack"), (_n_(14580, "x", lambda: x), _n_(14581, "y", lambda: y)))
_l_(14583)
_c_(14585, _n_(14584, "print", lambda: print), '\nStack arrays in sequence horizontally:')
_l_(14586)
_c_(14589, _n_(14587, "print", lambda: print), _n_(14588, "new_array", lambda: new_array))
_l_(14590)