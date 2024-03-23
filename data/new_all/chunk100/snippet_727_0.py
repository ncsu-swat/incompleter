# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(73684)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(73686)

except ImportError:
    pass
_c_(73688, _n_(73687, "print", lambda: print), 'NumPy array:')
_l_(73689)
_c_(73692, _n_(73690, "print", lambda: print), _n_(73691, "np_array", lambda: np_array))
_l_(73693)
new_series = _c_(73697, _a_(73695, _n_(73694, "pd", lambda: pd), "Series"), _n_(73696, "np_array", lambda: np_array))
_l_(73698)
_c_(73700, _n_(73699, "print", lambda: print), 'Converted Pandas series:')
_l_(73701)
_c_(73704, _n_(73702, "print", lambda: print), _n_(73703, "new_series", lambda: new_series))
_l_(73705)