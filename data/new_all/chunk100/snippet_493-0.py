# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(118640)

except ImportError:
    pass
_c_(118642, _n_(118641, "print", lambda: print), '\nOriginal arrays:')
_l_(118643)
x = _c_(118646, _a_(118645, _n_(118644, "np", lambda: np), "array"), (1, 2, 3))
_l_(118647)
y = _c_(118650, _a_(118649, _n_(118648, "np", lambda: np), "array"), (2, 3, 4))
_l_(118651)
_c_(118653, _n_(118652, "print", lambda: print), 'Array-1')
_l_(118654)
_c_(118657, _n_(118655, "print", lambda: print), _n_(118656, "x", lambda: x))
_l_(118658)
_c_(118660, _n_(118659, "print", lambda: print), 'Array-2')
_l_(118661)
_c_(118664, _n_(118662, "print", lambda: print), _n_(118663, "y", lambda: y))
_l_(118665)
_c_(118667, _n_(118666, "print", lambda: print), '\nStack 1-D arrays as columns wise:')
_l_(118668)
_c_(118671, _n_(118669, "print", lambda: print), _n_(118670, "new_array", lambda: new_array))
_l_(118672)