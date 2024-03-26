# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(116278)

except ImportError:
    pass
arr1 = _c_(116282, _a_(116280, _n_(116279, "np", lambda: np), "reshape"), _n_(116281, "num", lambda: num), [4, 5])
_l_(116283)
_c_(116285, _n_(116284, "print", lambda: print), 'Original array:')
_l_(116286)
_c_(116289, _n_(116287, "print", lambda: print), _n_(116288, "arr1", lambda: arr1))
_l_(116290)
_c_(116295, _n_(116291, "print", lambda: print), [0, 1, 2, 3, 4] in _c_(116294, _a_(116293, _n_(116292, "arr1", lambda: arr1), "tolist")))
_l_(116296)
_c_(116301, _n_(116297, "print", lambda: print), [0, 1, 2, 3, 5] in _c_(116300, _a_(116299, _n_(116298, "arr1", lambda: arr1), "tolist")))
_l_(116302)
_c_(116307, _n_(116303, "print", lambda: print), [15, 16, 17, 18, 19] in _c_(116306, _a_(116305, _n_(116304, "arr1", lambda: arr1), "tolist")))
_l_(116308)