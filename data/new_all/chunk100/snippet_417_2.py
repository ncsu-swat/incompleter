# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(41068)

except ImportError:
    pass
num_series = _c_(41073, _a_(41070, _n_(41069, "pd", lambda: pd), "Series"), _c_(41072, _n_(41071, "list", lambda: list), '2390238923902390239023'))
_l_(41074)
_c_(41076, _n_(41075, "print", lambda: print), 'Original Series:')
_l_(41077)
_c_(41080, _n_(41078, "print", lambda: print), _n_(41079, "num_series", lambda: num_series))
_l_(41081)
result = _c_(41085, _a_(41083, _n_(41082, "num_series", lambda: num_series), "take"), _n_(41084, "element_pos", lambda: element_pos))
_l_(41086)
_c_(41088, _n_(41087, "print", lambda: print), '\nExtract items at given positions of the said series:')
_l_(41089)
_c_(41092, _n_(41090, "print", lambda: print), _n_(41091, "result", lambda: result))
_l_(41093)