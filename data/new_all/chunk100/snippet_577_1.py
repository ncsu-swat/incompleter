# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(59824)

except ImportError:
    pass
data1 = _c_(59827, _a_(59826, _n_(59825, "pd", lambda: pd), "DataFrame"), {'key1': ['K0', 'K0', 'K1', 'K2'], 'key2': ['K0', 'K1', 'K0', 'K1'], 'P': ['P0', 'P1', 'P2', 'P3'], 'Q': ['Q0', 'Q1', 'Q2', 'Q3']})
_l_(59828)
_c_(59830, _n_(59829, "print", lambda: print), 'Original DataFrames:')
_l_(59831)
_c_(59834, _n_(59832, "print", lambda: print), _n_(59833, "data1", lambda: data1))
_l_(59835)
_c_(59837, _n_(59836, "print", lambda: print), '--------------------')
_l_(59838)
_c_(59841, _n_(59839, "print", lambda: print), _n_(59840, "data2", lambda: data2))
_l_(59842)
_c_(59844, _n_(59843, "print", lambda: print), '\nMerged Data:')
_l_(59845)
merged_data = _c_(59850, _a_(59847, _n_(59846, "pd", lambda: pd), "merge"), _n_(59848, "data1", lambda: data1), _n_(59849, "data2", lambda: data2), on=['key1', 'key2'])
_l_(59851)
_c_(59854, _n_(59852, "print", lambda: print), _n_(59853, "merged_data", lambda: merged_data))
_l_(59855)