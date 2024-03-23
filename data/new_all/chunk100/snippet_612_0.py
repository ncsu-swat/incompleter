# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(64580)

except ImportError:
    pass
try:
    import numpy as np
    _l_(64582)

except ImportError:
    pass
_c_(64585, _a_(64584, _n_(64583, "pd", lambda: pd), "set_option"), 'display.max_rows', None)
_l_(64586)
_c_(64588, _n_(64587, "print", lambda: print), 'Original Orders DataFrame:')
_l_(64589)
_c_(64592, _n_(64590, "print", lambda: print), _n_(64591, "df", lambda: df))
_l_(64593)
_c_(64595, _n_(64594, "print", lambda: print), '\nMissing values in purch_amt column:')
_l_(64596)
result = _c_(64603, _a_(64602, _c_(64601, _a_(64600, _c_(64599, _a_(64598, _n_(64597, "df", lambda: df)['ord_no'], "isnull")), "to_numpy")), "nonzero"))
_l_(64604)
_c_(64607, _n_(64605, "print", lambda: print), _n_(64606, "result", lambda: result))
_l_(64608)