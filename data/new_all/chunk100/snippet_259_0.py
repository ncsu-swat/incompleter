# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(21057)

except ImportError:
    pass
data2 = _c_(21060, _a_(21059, _n_(21058, "pd", lambda: pd), "DataFrame"), {'C': ['C0', 'C2', 'C3'], 'D': ['D0', 'D2', 'D3']}, index=['K0', 'K2', 'K3'])
_l_(21061)
_c_(21063, _n_(21062, "print", lambda: print), 'Original DataFrames:')
_l_(21064)
_c_(21067, _n_(21065, "print", lambda: print), _n_(21066, "data1", lambda: data1))
_l_(21068)
_c_(21070, _n_(21069, "print", lambda: print), '--------------------')
_l_(21071)
_c_(21074, _n_(21072, "print", lambda: print), _n_(21073, "data2", lambda: data2))
_l_(21075)
_c_(21077, _n_(21076, "print", lambda: print), '\nMerged Data (Joining on index):')
_l_(21078)
result = _c_(21082, _a_(21080, _n_(21079, "data1", lambda: data1), "join"), _n_(21081, "data2", lambda: data2))
_l_(21083)
_c_(21086, _n_(21084, "print", lambda: print), _n_(21085, "result", lambda: result))
_l_(21087)