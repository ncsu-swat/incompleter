# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(77680)

except ImportError:
    pass
ds = _c_(77683, _a_(77682, _n_(77681, "pd", lambda: pd), "Series"), [1, 3, 5, 7, 9, 11, 13, 15], index=[0, 1, 2, 3, 4, 5, 7, 8])
_l_(77684)
_c_(77686, _n_(77685, "print", lambda: print), 'Original Series:')
_l_(77687)
_c_(77690, _n_(77688, "print", lambda: print), _n_(77689, "ds", lambda: ds))
_l_(77691)
_c_(77693, _n_(77692, "print", lambda: print), '\nIndex of 11 in the said series:')
_l_(77694)
_c_(77697, _n_(77695, "print", lambda: print), _n_(77696, "x", lambda: x))
_l_(77698)