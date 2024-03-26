# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(107862)

except ImportError:
    pass
s = _c_(107865, _a_(107864, _n_(107863, "pd", lambda: pd), "Series"), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
_l_(107866)
_c_(107868, _n_(107867, "print", lambda: print), 'Original Data Series:')
_l_(107869)
_c_(107872, _n_(107870, "print", lambda: print), _n_(107871, "s", lambda: s))
_l_(107873)
_c_(107875, _n_(107874, "print", lambda: print), '\nSubset of the above Data Series:')
_l_(107876)
new_s = _n_(107877, "s", lambda: s)[_n_(107878, "s", lambda: s) < _n_(107879, "n", lambda: n)]
_l_(107880)
_c_(107883, _n_(107881, "print", lambda: print), _n_(107882, "new_s", lambda: new_s))
_l_(107884)