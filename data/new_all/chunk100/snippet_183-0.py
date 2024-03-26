# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(103897)

except ImportError:
    pass
_c_(103899, _n_(103898, "print", lambda: print), '\nOriginal arrays:')
_l_(103900)
x = _c_(103905, _a_(103904, _c_(103903, _a_(103902, _n_(103901, "np", lambda: np), "arange"), 9), "reshape"), 3, 3)
_l_(103906)
y = _n_(103907, "x", lambda: x) * 3
_l_(103908)
_c_(103910, _n_(103909, "print", lambda: print), 'Array-1')
_l_(103911)
_c_(103914, _n_(103912, "print", lambda: print), _n_(103913, "x", lambda: x))
_l_(103915)
_c_(103917, _n_(103916, "print", lambda: print), 'Array-2')
_l_(103918)
_c_(103921, _n_(103919, "print", lambda: print), _n_(103920, "y", lambda: y))
_l_(103922)
_c_(103924, _n_(103923, "print", lambda: print), '\nStack arrays in sequence horizontally:')
_l_(103925)
_c_(103928, _n_(103926, "print", lambda: print), _n_(103927, "new_array", lambda: new_array))
_l_(103929)