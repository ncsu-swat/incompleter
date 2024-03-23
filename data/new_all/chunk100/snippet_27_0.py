# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(22696)

except ImportError:
    pass
s = _c_(22699, _a_(22698, _n_(22697, "pd", lambda: pd), "Series"), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
_l_(22700)
_c_(22702, _n_(22701, "print", lambda: print), 'Original Data Series:')
_l_(22703)
_c_(22706, _n_(22704, "print", lambda: print), _n_(22705, "s", lambda: s))
_l_(22707)
_c_(22709, _n_(22708, "print", lambda: print), '\nSubset of the above Data Series:')
_l_(22710)
new_s = _n_(22711, "s", lambda: s)[_n_(22712, "s", lambda: s) < _n_(22713, "n", lambda: n)]
_l_(22714)
_c_(22717, _n_(22715, "print", lambda: print), _n_(22716, "new_s", lambda: new_s))
_l_(22718)