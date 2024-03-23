# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(68634)

except ImportError:
    pass
a = _c_(68637, _a_(68636, _n_(68635, "np", lambda: np), "array"), [97, 101, 105, 111, 117])
_l_(68638)
_c_(68640, _n_(68639, "print", lambda: print), 'Original arrays')
_l_(68641)
_c_(68644, _n_(68642, "print", lambda: print), _n_(68643, "a", lambda: a))
_l_(68645)
_c_(68648, _n_(68646, "print", lambda: print), _n_(68647, "b", lambda: b))
_l_(68649)
_c_(68651, _n_(68650, "print", lambda: print), 'Elements from the second array  corresponding to elements in the first array  that are greater than 100 and less than 110:')
_l_(68652)
_c_(68657, _n_(68653, "print", lambda: print), _n_(68654, "b", lambda: b)[(100 < _n_(68655, "a", lambda: a)) & (_n_(68656, "a", lambda: a) < 110)])
_l_(68658)