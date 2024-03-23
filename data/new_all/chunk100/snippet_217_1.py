# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(17135)

except ImportError:
    pass
_c_(17137, _n_(17136, "print", lambda: print), 'Empty array:')
_l_(17138)
_c_(17141, _n_(17139, "print", lambda: print), _n_(17140, "arr", lambda: arr))
_l_(17142)
arr = _c_(17149, _a_(17144, _n_(17143, "np", lambda: np), "append"), _n_(17145, "arr", lambda: arr), _c_(17148, _a_(17147, _n_(17146, "np", lambda: np), "array"), [[10, 20, 30]]), axis=0)
_l_(17150)
arr = _c_(17157, _a_(17152, _n_(17151, "np", lambda: np), "append"), _n_(17153, "arr", lambda: arr), _c_(17156, _a_(17155, _n_(17154, "np", lambda: np), "array"), [[40, 50, 60]]), axis=0)
_l_(17158)
_c_(17160, _n_(17159, "print", lambda: print), 'After adding two new arrays:')
_l_(17161)
_c_(17164, _n_(17162, "print", lambda: print), _n_(17163, "arr", lambda: arr))
_l_(17165)