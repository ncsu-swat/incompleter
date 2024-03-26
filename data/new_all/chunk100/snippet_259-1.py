# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(107192)

except ImportError:
    pass
data2 = _c_(107195, _a_(107194, _n_(107193, "pd", lambda: pd), "DataFrame"), {'C': ['C0', 'C2', 'C3'], 'D': ['D0', 'D2', 'D3']}, index=['K0', 'K2', 'K3'])
_l_(107196)
_c_(107198, _n_(107197, "print", lambda: print), 'Original DataFrames:')
_l_(107199)
_c_(107202, _n_(107200, "print", lambda: print), _n_(107201, "data1", lambda: data1))
_l_(107203)
_c_(107205, _n_(107204, "print", lambda: print), '--------------------')
_l_(107206)
_c_(107209, _n_(107207, "print", lambda: print), _n_(107208, "data2", lambda: data2))
_l_(107210)
_c_(107212, _n_(107211, "print", lambda: print), '\nMerged Data (Joining on index):')
_l_(107213)
result = _c_(107217, _a_(107215, _n_(107214, "data1", lambda: data1), "join"), _n_(107216, "data2", lambda: data2))
_l_(107218)
_c_(107221, _n_(107219, "print", lambda: print), _n_(107220, "result", lambda: result))
_l_(107222)