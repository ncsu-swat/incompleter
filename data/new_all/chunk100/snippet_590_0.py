# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(62734)

except ImportError:
    pass
_c_(62736, _n_(62735, "print", lambda: print), 'Original dictionary:')
_l_(62737)
_c_(62740, _n_(62738, "print", lambda: print), _n_(62739, "d1", lambda: d1))
_l_(62741)
new_series = _c_(62745, _a_(62743, _n_(62742, "pd", lambda: pd), "Series"), _n_(62744, "d1", lambda: d1))
_l_(62746)
_c_(62748, _n_(62747, "print", lambda: print), 'Converted series:')
_l_(62749)
_c_(62752, _n_(62750, "print", lambda: print), _n_(62751, "new_series", lambda: new_series))
_l_(62753)