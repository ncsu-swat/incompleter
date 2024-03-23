# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(21120)

except ImportError:
    pass
data1 = _c_(21123, _a_(21122, _n_(21121, "pd", lambda: pd), "DataFrame"), {'A': ['A0', 'A1', 'A2'], 'B': ['B0', 'B1', 'B2']}, index=['K0', 'K1', 'K2'])
_l_(21124)
_c_(21126, _n_(21125, "print", lambda: print), 'Original DataFrames:')
_l_(21127)
_c_(21130, _n_(21128, "print", lambda: print), _n_(21129, "data1", lambda: data1))
_l_(21131)
_c_(21133, _n_(21132, "print", lambda: print), '--------------------')
_l_(21134)
_c_(21137, _n_(21135, "print", lambda: print), _n_(21136, "data2", lambda: data2))
_l_(21138)
_c_(21140, _n_(21139, "print", lambda: print), '\nMerged Data (Joining on index):')
_l_(21141)
result = _c_(21145, _a_(21143, _n_(21142, "data1", lambda: data1), "join"), _n_(21144, "data2", lambda: data2))
_l_(21146)
_c_(21149, _n_(21147, "print", lambda: print), _n_(21148, "result", lambda: result))
_l_(21150)