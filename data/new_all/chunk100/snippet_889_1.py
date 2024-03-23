# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(87452)

except ImportError:
    pass
data1 = _c_(87455, _a_(87454, _n_(87453, "pd", lambda: pd), "DataFrame"), {'key1': ['K0', 'K0', 'K1', 'K2'], 'key2': ['K0', 'K1', 'K0', 'K1'], 'P': ['P0', 'P1', 'P2', 'P3'], 'Q': ['Q0', 'Q1', 'Q2', 'Q3']})
_l_(87456)
data2 = _c_(87459, _a_(87458, _n_(87457, "pd", lambda: pd), "DataFrame"), {'key1': ['K0', 'K1', 'K1', 'K2'], 'key2': ['K0', 'K0', 'K0', 'K0'], 'R': ['R0', 'R1', 'R2', 'R3'], 'S': ['S0', 'S1', 'S2', 'S3']})
_l_(87460)
_c_(87462, _n_(87461, "print", lambda: print), 'Original DataFrames:')
_l_(87463)
_c_(87466, _n_(87464, "print", lambda: print), _n_(87465, "data1", lambda: data1))
_l_(87467)
_c_(87469, _n_(87468, "print", lambda: print), '--------------------')
_l_(87470)
_c_(87473, _n_(87471, "print", lambda: print), _n_(87472, "data2", lambda: data2))
_l_(87474)
_c_(87476, _n_(87475, "print", lambda: print), '\nMerge two dataframes with different columns:')
_l_(87477)
_c_(87480, _n_(87478, "print", lambda: print), _n_(87479, "result", lambda: result))
_l_(87481)