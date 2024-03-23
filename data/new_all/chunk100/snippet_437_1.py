# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(44494)

except ImportError:
    pass
arr1 = _c_(44498, _a_(44496, _n_(44495, "np", lambda: np), "reshape"), _n_(44497, "num", lambda: num), [4, 5])
_l_(44499)
_c_(44501, _n_(44500, "print", lambda: print), 'Original array:')
_l_(44502)
_c_(44505, _n_(44503, "print", lambda: print), _n_(44504, "arr1", lambda: arr1))
_l_(44506)
_c_(44511, _n_(44507, "print", lambda: print), [0, 1, 2, 3, 4] in _c_(44510, _a_(44509, _n_(44508, "arr1", lambda: arr1), "tolist")))
_l_(44512)
_c_(44517, _n_(44513, "print", lambda: print), [0, 1, 2, 3, 5] in _c_(44516, _a_(44515, _n_(44514, "arr1", lambda: arr1), "tolist")))
_l_(44518)
_c_(44523, _n_(44519, "print", lambda: print), [15, 16, 17, 18, 19] in _c_(44522, _a_(44521, _n_(44520, "arr1", lambda: arr1), "tolist")))
_l_(44524)