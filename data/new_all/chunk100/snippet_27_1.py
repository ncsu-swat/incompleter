# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(22720)

except ImportError:
    pass
_c_(22722, _n_(22721, "print", lambda: print), 'Original Data Series:')
_l_(22723)
_c_(22726, _n_(22724, "print", lambda: print), _n_(22725, "s", lambda: s))
_l_(22727)
_c_(22729, _n_(22728, "print", lambda: print), '\nSubset of the above Data Series:')
_l_(22730)
n = 6
_l_(22731)
new_s = _n_(22732, "s", lambda: s)[_n_(22733, "s", lambda: s) < _n_(22734, "n", lambda: n)]
_l_(22735)
_c_(22738, _n_(22736, "print", lambda: print), _n_(22737, "new_s", lambda: new_s))
_l_(22739)