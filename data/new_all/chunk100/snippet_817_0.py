# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(82250)

except ImportError:
    pass
data1 = _c_(82253, _a_(82252, _n_(82251, "pd", lambda: pd), "DataFrame"), {'key1': ['K0', 'K0', 'K1', 'K2'], 'key2': ['K0', 'K1', 'K0', 'K1'], 'P': ['P0', 'P1', 'P2', 'P3'], 'Q': ['Q0', 'Q1', 'Q2', 'Q3']})
_l_(82254)
data2 = _c_(82257, _a_(82256, _n_(82255, "pd", lambda: pd), "DataFrame"), {'key1': ['K0', 'K1', 'K1', 'K2'], 'key2': ['K0', 'K0', 'K0', 'K0'], 'R': ['R0', 'R1', 'R2', 'R3'], 'S': ['S0', 'S1', 'S2', 'S3']})
_l_(82258)
_c_(82260, _n_(82259, "print", lambda: print), 'Original DataFrames:')
_l_(82261)
_c_(82264, _n_(82262, "print", lambda: print), _n_(82263, "data1", lambda: data1))
_l_(82265)
_c_(82267, _n_(82266, "print", lambda: print), '--------------------')
_l_(82268)
_c_(82271, _n_(82269, "print", lambda: print), _n_(82270, "data2", lambda: data2))
_l_(82272)
_c_(82274, _n_(82273, "print", lambda: print), '\nMerged Data (keys from data2):')
_l_(82275)
merged_data = _c_(82280, _a_(82277, _n_(82276, "pd", lambda: pd), "merge"), _n_(82278, "data1", lambda: data1), _n_(82279, "data2", lambda: data2), how='right', on=['key1', 'key2'])
_l_(82281)
_c_(82284, _n_(82282, "print", lambda: print), _n_(82283, "merged_data", lambda: merged_data))
_l_(82285)
_c_(82287, _n_(82286, "print", lambda: print), '\nMerged Data (keys from data1):')
_l_(82288)
_c_(82291, _n_(82289, "print", lambda: print), _n_(82290, "merged_data", lambda: merged_data))
_l_(82292)