# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(106332)

except ImportError:
    pass
x = _c_(106335, _a_(106334, _n_(106333, "np", lambda: np), "array"), [0, 1, -1])
_l_(106336)
_c_(106338, _n_(106337, "print", lambda: print), 'Original array: ')
_l_(106339)
_c_(106342, _n_(106340, "print", lambda: print), _n_(106341, "x", lambda: x))
_l_(106343)
r1 = _c_(106347, _a_(106345, _n_(106344, "np", lambda: np), "negative"), _n_(106346, "x", lambda: x))
_l_(106348)
assert _c_(106353, _a_(106350, _n_(106349, "np", lambda: np), "array_equal"), _n_(106351, "r1", lambda: r1), _n_(106352, "r2", lambda: r2))
_l_(106354)
_c_(106356, _n_(106355, "print", lambda: print), 'Numerical negative value for all elements of the said array:')
_l_(106357)
_c_(106360, _n_(106358, "print", lambda: print), _n_(106359, "r1", lambda: r1))
_l_(106361)