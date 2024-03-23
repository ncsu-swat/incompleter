# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(82340)

except ImportError:
    pass
data1 = _c_(82343, _a_(82342, _n_(82341, "pd", lambda: pd), "DataFrame"), {'key1': ['K0', 'K0', 'K1', 'K2'], 'key2': ['K0', 'K1', 'K0', 'K1'], 'P': ['P0', 'P1', 'P2', 'P3'], 'Q': ['Q0', 'Q1', 'Q2', 'Q3']})
_l_(82344)
_c_(82346, _n_(82345, "print", lambda: print), 'Original DataFrames:')
_l_(82347)
_c_(82350, _n_(82348, "print", lambda: print), _n_(82349, "data1", lambda: data1))
_l_(82351)
_c_(82353, _n_(82352, "print", lambda: print), '--------------------')
_l_(82354)
_c_(82357, _n_(82355, "print", lambda: print), _n_(82356, "data2", lambda: data2))
_l_(82358)
_c_(82360, _n_(82359, "print", lambda: print), '\nMerged Data (keys from data2):')
_l_(82361)
merged_data = _c_(82366, _a_(82363, _n_(82362, "pd", lambda: pd), "merge"), _n_(82364, "data1", lambda: data1), _n_(82365, "data2", lambda: data2), how='right', on=['key1', 'key2'])
_l_(82367)
_c_(82370, _n_(82368, "print", lambda: print), _n_(82369, "merged_data", lambda: merged_data))
_l_(82371)
_c_(82373, _n_(82372, "print", lambda: print), '\nMerged Data (keys from data1):')
_l_(82374)
merged_data = _c_(82379, _a_(82376, _n_(82375, "pd", lambda: pd), "merge"), _n_(82377, "data2", lambda: data2), _n_(82378, "data1", lambda: data1), how='right', on=['key1', 'key2'])
_l_(82380)
_c_(82383, _n_(82381, "print", lambda: print), _n_(82382, "merged_data", lambda: merged_data))
_l_(82384)