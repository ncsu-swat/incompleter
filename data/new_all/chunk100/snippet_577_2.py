# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(59857)

except ImportError:
    pass
data1 = _c_(59860, _a_(59859, _n_(59858, "pd", lambda: pd), "DataFrame"), {'key1': ['K0', 'K0', 'K1', 'K2'], 'key2': ['K0', 'K1', 'K0', 'K1'], 'P': ['P0', 'P1', 'P2', 'P3'], 'Q': ['Q0', 'Q1', 'Q2', 'Q3']})
_l_(59861)
data2 = _c_(59864, _a_(59863, _n_(59862, "pd", lambda: pd), "DataFrame"), {'key1': ['K0', 'K1', 'K1', 'K2'], 'key2': ['K0', 'K0', 'K0', 'K0'], 'R': ['R0', 'R1', 'R2', 'R3'], 'S': ['S0', 'S1', 'S2', 'S3']})
_l_(59865)
_c_(59867, _n_(59866, "print", lambda: print), 'Original DataFrames:')
_l_(59868)
_c_(59871, _n_(59869, "print", lambda: print), _n_(59870, "data1", lambda: data1))
_l_(59872)
_c_(59874, _n_(59873, "print", lambda: print), '--------------------')
_l_(59875)
_c_(59878, _n_(59876, "print", lambda: print), _n_(59877, "data2", lambda: data2))
_l_(59879)
_c_(59881, _n_(59880, "print", lambda: print), '\nMerged Data:')
_l_(59882)
_c_(59885, _n_(59883, "print", lambda: print), _n_(59884, "merged_data", lambda: merged_data))
_l_(59886)