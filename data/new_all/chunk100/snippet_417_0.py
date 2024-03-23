# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(41023)

except ImportError:
    pass
num_series = _c_(41028, _a_(41025, _n_(41024, "pd", lambda: pd), "Series"), _c_(41027, _n_(41026, "list", lambda: list), '2390238923902390239023'))
_l_(41029)
element_pos = [0, 2, 6, 11, 21]
_l_(41030)
_c_(41032, _n_(41031, "print", lambda: print), 'Original Series:')
_l_(41033)
_c_(41036, _n_(41034, "print", lambda: print), _n_(41035, "num_series", lambda: num_series))
_l_(41037)
_c_(41039, _n_(41038, "print", lambda: print), '\nExtract items at given positions of the said series:')
_l_(41040)
_c_(41043, _n_(41041, "print", lambda: print), _n_(41042, "result", lambda: result))
_l_(41044)