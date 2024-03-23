# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(82386)

except ImportError:
    pass
data1 = _c_(82389, _a_(82388, _n_(82387, "pd", lambda: pd), "DataFrame"), {'key1': ['K0', 'K0', 'K1', 'K2'], 'key2': ['K0', 'K1', 'K0', 'K1'], 'P': ['P0', 'P1', 'P2', 'P3'], 'Q': ['Q0', 'Q1', 'Q2', 'Q3']})
_l_(82390)
data2 = _c_(82393, _a_(82392, _n_(82391, "pd", lambda: pd), "DataFrame"), {'key1': ['K0', 'K1', 'K1', 'K2'], 'key2': ['K0', 'K0', 'K0', 'K0'], 'R': ['R0', 'R1', 'R2', 'R3'], 'S': ['S0', 'S1', 'S2', 'S3']})
_l_(82394)
_c_(82396, _n_(82395, "print", lambda: print), 'Original DataFrames:')
_l_(82397)
_c_(82400, _n_(82398, "print", lambda: print), _n_(82399, "data1", lambda: data1))
_l_(82401)
_c_(82403, _n_(82402, "print", lambda: print), '--------------------')
_l_(82404)
_c_(82407, _n_(82405, "print", lambda: print), _n_(82406, "data2", lambda: data2))
_l_(82408)
_c_(82410, _n_(82409, "print", lambda: print), '\nMerged Data (keys from data2):')
_l_(82411)
_c_(82414, _n_(82412, "print", lambda: print), _n_(82413, "merged_data", lambda: merged_data))
_l_(82415)
_c_(82417, _n_(82416, "print", lambda: print), '\nMerged Data (keys from data1):')
_l_(82418)
merged_data = _c_(82423, _a_(82420, _n_(82419, "pd", lambda: pd), "merge"), _n_(82421, "data2", lambda: data2), _n_(82422, "data1", lambda: data1), how='right', on=['key1', 'key2'])
_l_(82424)
_c_(82427, _n_(82425, "print", lambda: print), _n_(82426, "merged_data", lambda: merged_data))
_l_(82428)