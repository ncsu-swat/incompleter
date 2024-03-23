# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(84349)

except ImportError:
    pass
arr1 = _c_(84353, _a_(84352, _a_(84351, _n_(84350, "np", lambda: np), "random"), "random"), size=(25, 25, 1))
_l_(84354)
arr2 = _c_(84358, _a_(84357, _a_(84356, _n_(84355, "np", lambda: np), "random"), "random"), size=(25, 25, 1))
_l_(84359)
arr3 = _c_(84363, _a_(84362, _a_(84361, _n_(84360, "np", lambda: np), "random"), "random"), size=(25, 25, 1))
_l_(84364)
_c_(84366, _n_(84365, "print", lambda: print), 'Original arrays:')
_l_(84367)
_c_(84370, _n_(84368, "print", lambda: print), _n_(84369, "arr1", lambda: arr1))
_l_(84371)
_c_(84374, _n_(84372, "print", lambda: print), _n_(84373, "arr2", lambda: arr2))
_l_(84375)
_c_(84378, _n_(84376, "print", lambda: print), _n_(84377, "arr3", lambda: arr3))
_l_(84379)
_c_(84381, _n_(84380, "print", lambda: print), '\nAfter concatenate:')
_l_(84382)
_c_(84385, _n_(84383, "print", lambda: print), _n_(84384, "result", lambda: result))
_l_(84386)