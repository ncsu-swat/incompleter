# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(68608)

except ImportError:
    pass
b = _c_(68611, _a_(68610, _n_(68609, "np", lambda: np), "array"), ['a', 'e', 'i', 'o', 'u'])
_l_(68612)
_c_(68614, _n_(68613, "print", lambda: print), 'Original arrays')
_l_(68615)
_c_(68618, _n_(68616, "print", lambda: print), _n_(68617, "a", lambda: a))
_l_(68619)
_c_(68622, _n_(68620, "print", lambda: print), _n_(68621, "b", lambda: b))
_l_(68623)
_c_(68625, _n_(68624, "print", lambda: print), 'Elements from the second array  corresponding to elements in the first array  that are greater than 100 and less than 110:')
_l_(68626)
_c_(68631, _n_(68627, "print", lambda: print), _n_(68628, "b", lambda: b)[(100 < _n_(68629, "a", lambda: a)) & (_n_(68630, "a", lambda: a) < 110)])
_l_(68632)