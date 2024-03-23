# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(5881)

except ImportError:
    pass
array_nums = _c_(5884, _a_(5883, _n_(5882, "np", lambda: np), "arange"), 0, 40, 2)
_l_(5885)
_c_(5887, _n_(5886, "print", lambda: print), 'Original array:')
_l_(5888)
_c_(5891, _n_(5889, "print", lambda: print), _n_(5890, "array_nums", lambda: array_nums))
_l_(5892)
_c_(5894, _n_(5893, "print", lambda: print), '\nNew array of shape(5, 4):')
_l_(5895)
_c_(5898, _n_(5896, "print", lambda: print), _n_(5897, "new_array", lambda: new_array))
_l_(5899)
_c_(5901, _n_(5900, "print", lambda: print), '\nRestore the reshaped array into a 1-D array:')
_l_(5902)
_c_(5907, _n_(5903, "print", lambda: print), _c_(5906, _a_(5905, _n_(5904, "new_array", lambda: new_array), "flatten")))
_l_(5908)