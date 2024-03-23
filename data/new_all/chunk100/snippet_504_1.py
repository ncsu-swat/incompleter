# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(52295)

except ImportError:
    pass
_c_(52297, _n_(52296, "print", lambda: print), 'Original Array:')
_l_(52298)
_c_(52301, _n_(52299, "print", lambda: print), _n_(52300, "x", lambda: x))
_l_(52302)
(xmax, xmin) = (_c_(52305, _a_(52304, _n_(52303, "x", lambda: x), "max")), _c_(52308, _a_(52307, _n_(52306, "x", lambda: x), "min")))
_l_(52309)
x = (_n_(52310, "x", lambda: x) - _n_(52311, "xmin", lambda: xmin)) / (_n_(52312, "xmax", lambda: xmax) - _n_(52313, "xmin", lambda: xmin))
_l_(52314)
_c_(52316, _n_(52315, "print", lambda: print), 'After normalization:')
_l_(52317)
_c_(52320, _n_(52318, "print", lambda: print), _n_(52319, "x", lambda: x))
_l_(52321)