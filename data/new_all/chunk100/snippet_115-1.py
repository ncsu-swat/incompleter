# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(100956)

except ImportError:
    pass
array_nums = _c_(100959, _a_(100958, _n_(100957, "np", lambda: np), "arange"), 0, 40, 2)
_l_(100960)
_c_(100962, _n_(100961, "print", lambda: print), 'Original array:')
_l_(100963)
_c_(100966, _n_(100964, "print", lambda: print), _n_(100965, "array_nums", lambda: array_nums))
_l_(100967)
_c_(100969, _n_(100968, "print", lambda: print), '\nNew array of shape(5, 4):')
_l_(100970)
_c_(100973, _n_(100971, "print", lambda: print), _n_(100972, "new_array", lambda: new_array))
_l_(100974)
_c_(100976, _n_(100975, "print", lambda: print), '\nRestore the reshaped array into a 1-D array:')
_l_(100977)
_c_(100982, _n_(100978, "print", lambda: print), _c_(100981, _a_(100980, _n_(100979, "new_array", lambda: new_array), "flatten")))
_l_(100983)