# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(106770)

except ImportError:
    pass
_c_(106772, _n_(106771, "print", lambda: print), 'Original array:')
_l_(106773)
_c_(106776, _n_(106774, "print", lambda: print), _n_(106775, "x", lambda: x))
_l_(106777)
_c_(106779, _n_(106778, "print", lambda: print), '1 on the border and 0 inside in the array')
_l_(106780)
_n_(106781, "x", lambda: x)[1:-1, 1:-1] = 0
_l_(106782)
_c_(106785, _n_(106783, "print", lambda: print), _n_(106784, "x", lambda: x))
_l_(106786)