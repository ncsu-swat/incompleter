# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(21089)

except ImportError:
    pass
data1 = _c_(21092, _a_(21091, _n_(21090, "pd", lambda: pd), "DataFrame"), {'A': ['A0', 'A1', 'A2'], 'B': ['B0', 'B1', 'B2']}, index=['K0', 'K1', 'K2'])
_l_(21093)
data2 = _c_(21096, _a_(21095, _n_(21094, "pd", lambda: pd), "DataFrame"), {'C': ['C0', 'C2', 'C3'], 'D': ['D0', 'D2', 'D3']}, index=['K0', 'K2', 'K3'])
_l_(21097)
_c_(21099, _n_(21098, "print", lambda: print), 'Original DataFrames:')
_l_(21100)
_c_(21103, _n_(21101, "print", lambda: print), _n_(21102, "data1", lambda: data1))
_l_(21104)
_c_(21106, _n_(21105, "print", lambda: print), '--------------------')
_l_(21107)
_c_(21110, _n_(21108, "print", lambda: print), _n_(21109, "data2", lambda: data2))
_l_(21111)
_c_(21113, _n_(21112, "print", lambda: print), '\nMerged Data (Joining on index):')
_l_(21114)
_c_(21117, _n_(21115, "print", lambda: print), _n_(21116, "result", lambda: result))
_l_(21118)