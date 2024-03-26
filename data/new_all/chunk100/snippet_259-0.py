# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(107160)

except ImportError:
    pass
data1 = _c_(107163, _a_(107162, _n_(107161, "pd", lambda: pd), "DataFrame"), {'A': ['A0', 'A1', 'A2'], 'B': ['B0', 'B1', 'B2']}, index=['K0', 'K1', 'K2'])
_l_(107164)
_c_(107166, _n_(107165, "print", lambda: print), 'Original DataFrames:')
_l_(107167)
_c_(107170, _n_(107168, "print", lambda: print), _n_(107169, "data1", lambda: data1))
_l_(107171)
_c_(107173, _n_(107172, "print", lambda: print), '--------------------')
_l_(107174)
_c_(107177, _n_(107175, "print", lambda: print), _n_(107176, "data2", lambda: data2))
_l_(107178)
_c_(107180, _n_(107179, "print", lambda: print), '\nMerged Data (Joining on index):')
_l_(107181)
result = _c_(107185, _a_(107183, _n_(107182, "data1", lambda: data1), "join"), _n_(107184, "data2", lambda: data2))
_l_(107186)
_c_(107189, _n_(107187, "print", lambda: print), _n_(107188, "result", lambda: result))
_l_(107190)