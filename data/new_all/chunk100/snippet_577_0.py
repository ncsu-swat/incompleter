# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(59791)

except ImportError:
    pass
data2 = _c_(59794, _a_(59793, _n_(59792, "pd", lambda: pd), "DataFrame"), {'key1': ['K0', 'K1', 'K1', 'K2'], 'key2': ['K0', 'K0', 'K0', 'K0'], 'R': ['R0', 'R1', 'R2', 'R3'], 'S': ['S0', 'S1', 'S2', 'S3']})
_l_(59795)
_c_(59797, _n_(59796, "print", lambda: print), 'Original DataFrames:')
_l_(59798)
_c_(59801, _n_(59799, "print", lambda: print), _n_(59800, "data1", lambda: data1))
_l_(59802)
_c_(59804, _n_(59803, "print", lambda: print), '--------------------')
_l_(59805)
_c_(59808, _n_(59806, "print", lambda: print), _n_(59807, "data2", lambda: data2))
_l_(59809)
_c_(59811, _n_(59810, "print", lambda: print), '\nMerged Data:')
_l_(59812)
merged_data = _c_(59817, _a_(59814, _n_(59813, "pd", lambda: pd), "merge"), _n_(59815, "data1", lambda: data1), _n_(59816, "data2", lambda: data2), on=['key1', 'key2'])
_l_(59818)
_c_(59821, _n_(59819, "print", lambda: print), _n_(59820, "merged_data", lambda: merged_data))
_l_(59822)