# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(107224)

except ImportError:
    pass
data1 = _c_(107227, _a_(107226, _n_(107225, "pd", lambda: pd), "DataFrame"), {'A': ['A0', 'A1', 'A2'], 'B': ['B0', 'B1', 'B2']}, index=['K0', 'K1', 'K2'])
_l_(107228)
data2 = _c_(107231, _a_(107230, _n_(107229, "pd", lambda: pd), "DataFrame"), {'C': ['C0', 'C2', 'C3'], 'D': ['D0', 'D2', 'D3']}, index=['K0', 'K2', 'K3'])
_l_(107232)
_c_(107234, _n_(107233, "print", lambda: print), 'Original DataFrames:')
_l_(107235)
_c_(107238, _n_(107236, "print", lambda: print), _n_(107237, "data1", lambda: data1))
_l_(107239)
_c_(107241, _n_(107240, "print", lambda: print), '--------------------')
_l_(107242)
_c_(107245, _n_(107243, "print", lambda: print), _n_(107244, "data2", lambda: data2))
_l_(107246)
_c_(107248, _n_(107247, "print", lambda: print), '\nMerged Data (Joining on index):')
_l_(107249)
_c_(107252, _n_(107250, "print", lambda: print), _n_(107251, "result", lambda: result))
_l_(107253)