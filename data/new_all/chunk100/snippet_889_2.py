# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(87483)

except ImportError:
    pass
data1 = _c_(87486, _a_(87485, _n_(87484, "pd", lambda: pd), "DataFrame"), {'key1': ['K0', 'K0', 'K1', 'K2'], 'key2': ['K0', 'K1', 'K0', 'K1'], 'P': ['P0', 'P1', 'P2', 'P3'], 'Q': ['Q0', 'Q1', 'Q2', 'Q3']})
_l_(87487)
_c_(87489, _n_(87488, "print", lambda: print), 'Original DataFrames:')
_l_(87490)
_c_(87493, _n_(87491, "print", lambda: print), _n_(87492, "data1", lambda: data1))
_l_(87494)
_c_(87496, _n_(87495, "print", lambda: print), '--------------------')
_l_(87497)
_c_(87500, _n_(87498, "print", lambda: print), _n_(87499, "data2", lambda: data2))
_l_(87501)
_c_(87503, _n_(87502, "print", lambda: print), '\nMerge two dataframes with different columns:')
_l_(87504)
result = _c_(87509, _a_(87506, _n_(87505, "pd", lambda: pd), "concat"), [_n_(87507, "data1", lambda: data1), _n_(87508, "data2", lambda: data2)], axis=0, ignore_index=True)
_l_(87510)
_c_(87513, _n_(87511, "print", lambda: print), _n_(87512, "result", lambda: result))
_l_(87514)