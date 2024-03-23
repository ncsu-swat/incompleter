# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(72773)

except ImportError:
    pass
_c_(72775, _n_(72774, "print", lambda: print), 'Original array:')
_l_(72776)
_c_(72779, _n_(72777, "print", lambda: print), _n_(72778, "x", lambda: x))
_l_(72780)
_c_(72782, _n_(72781, "print", lambda: print), 'Replace all elements of the said array with .5 which are greater than .5')
_l_(72783)
_n_(72784, "x", lambda: x)[_n_(72785, "x", lambda: x) > 0.5] = 0.5
_l_(72786)
_c_(72789, _n_(72787, "print", lambda: print), _n_(72788, "x", lambda: x))
_l_(72790)