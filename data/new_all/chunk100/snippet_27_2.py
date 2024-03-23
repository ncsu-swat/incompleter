# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(22741)

except ImportError:
    pass
s = _c_(22744, _a_(22743, _n_(22742, "pd", lambda: pd), "Series"), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
_l_(22745)
_c_(22747, _n_(22746, "print", lambda: print), 'Original Data Series:')
_l_(22748)
_c_(22751, _n_(22749, "print", lambda: print), _n_(22750, "s", lambda: s))
_l_(22752)
_c_(22754, _n_(22753, "print", lambda: print), '\nSubset of the above Data Series:')
_l_(22755)
n = 6
_l_(22756)
_c_(22759, _n_(22757, "print", lambda: print), _n_(22758, "new_s", lambda: new_s))
_l_(22760)