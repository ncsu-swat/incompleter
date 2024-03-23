# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(82294)

except ImportError:
    pass
data2 = _c_(82297, _a_(82296, _n_(82295, "pd", lambda: pd), "DataFrame"), {'key1': ['K0', 'K1', 'K1', 'K2'], 'key2': ['K0', 'K0', 'K0', 'K0'], 'R': ['R0', 'R1', 'R2', 'R3'], 'S': ['S0', 'S1', 'S2', 'S3']})
_l_(82298)
_c_(82300, _n_(82299, "print", lambda: print), 'Original DataFrames:')
_l_(82301)
_c_(82304, _n_(82302, "print", lambda: print), _n_(82303, "data1", lambda: data1))
_l_(82305)
_c_(82307, _n_(82306, "print", lambda: print), '--------------------')
_l_(82308)
_c_(82311, _n_(82309, "print", lambda: print), _n_(82310, "data2", lambda: data2))
_l_(82312)
_c_(82314, _n_(82313, "print", lambda: print), '\nMerged Data (keys from data2):')
_l_(82315)
merged_data = _c_(82320, _a_(82317, _n_(82316, "pd", lambda: pd), "merge"), _n_(82318, "data1", lambda: data1), _n_(82319, "data2", lambda: data2), how='right', on=['key1', 'key2'])
_l_(82321)
_c_(82324, _n_(82322, "print", lambda: print), _n_(82323, "merged_data", lambda: merged_data))
_l_(82325)
_c_(82327, _n_(82326, "print", lambda: print), '\nMerged Data (keys from data1):')
_l_(82328)
merged_data = _c_(82333, _a_(82330, _n_(82329, "pd", lambda: pd), "merge"), _n_(82331, "data2", lambda: data2), _n_(82332, "data1", lambda: data1), how='right', on=['key1', 'key2'])
_l_(82334)
_c_(82337, _n_(82335, "print", lambda: print), _n_(82336, "merged_data", lambda: merged_data))
_l_(82338)