# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(5852)

except ImportError:
    pass
_c_(5854, _n_(5853, "print", lambda: print), 'Original array:')
_l_(5855)
_c_(5858, _n_(5856, "print", lambda: print), _n_(5857, "array_nums", lambda: array_nums))
_l_(5859)
_c_(5861, _n_(5860, "print", lambda: print), '\nNew array of shape(5, 4):')
_l_(5862)
new_array = _c_(5865, _a_(5864, _n_(5863, "array_nums", lambda: array_nums), "reshape"), 5, 4)
_l_(5866)
_c_(5869, _n_(5867, "print", lambda: print), _n_(5868, "new_array", lambda: new_array))
_l_(5870)
_c_(5872, _n_(5871, "print", lambda: print), '\nRestore the reshaped array into a 1-D array:')
_l_(5873)
_c_(5878, _n_(5874, "print", lambda: print), _c_(5877, _a_(5876, _n_(5875, "new_array", lambda: new_array), "flatten")))
_l_(5879)