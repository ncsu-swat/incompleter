# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(84226)

except ImportError:
    pass
arr2 = _c_(84230, _a_(84229, _a_(84228, _n_(84227, "np", lambda: np), "random"), "random"), size=(25, 25, 1))
_l_(84231)
arr3 = _c_(84235, _a_(84234, _a_(84233, _n_(84232, "np", lambda: np), "random"), "random"), size=(25, 25, 1))
_l_(84236)
_c_(84238, _n_(84237, "print", lambda: print), 'Original arrays:')
_l_(84239)
_c_(84242, _n_(84240, "print", lambda: print), _n_(84241, "arr1", lambda: arr1))
_l_(84243)
_c_(84246, _n_(84244, "print", lambda: print), _n_(84245, "arr2", lambda: arr2))
_l_(84247)
_c_(84250, _n_(84248, "print", lambda: print), _n_(84249, "arr3", lambda: arr3))
_l_(84251)
result = _c_(84257, _a_(84253, _n_(84252, "np", lambda: np), "concatenate"), (_n_(84254, "arr1", lambda: arr1), _n_(84255, "arr2", lambda: arr2), _n_(84256, "arr3", lambda: arr3)), axis=-1)
_l_(84258)
_c_(84260, _n_(84259, "print", lambda: print), '\nAfter concatenate:')
_l_(84261)
_c_(84264, _n_(84262, "print", lambda: print), _n_(84263, "result", lambda: result))
_l_(84265)