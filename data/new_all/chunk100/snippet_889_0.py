# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(87419)

except ImportError:
    pass
data2 = _c_(87422, _a_(87421, _n_(87420, "pd", lambda: pd), "DataFrame"), {'key1': ['K0', 'K1', 'K1', 'K2'], 'key2': ['K0', 'K0', 'K0', 'K0'], 'R': ['R0', 'R1', 'R2', 'R3'], 'S': ['S0', 'S1', 'S2', 'S3']})
_l_(87423)
_c_(87425, _n_(87424, "print", lambda: print), 'Original DataFrames:')
_l_(87426)
_c_(87429, _n_(87427, "print", lambda: print), _n_(87428, "data1", lambda: data1))
_l_(87430)
_c_(87432, _n_(87431, "print", lambda: print), '--------------------')
_l_(87433)
_c_(87436, _n_(87434, "print", lambda: print), _n_(87435, "data2", lambda: data2))
_l_(87437)
_c_(87439, _n_(87438, "print", lambda: print), '\nMerge two dataframes with different columns:')
_l_(87440)
result = _c_(87445, _a_(87442, _n_(87441, "pd", lambda: pd), "concat"), [_n_(87443, "data1", lambda: data1), _n_(87444, "data2", lambda: data2)], axis=0, ignore_index=True)
_l_(87446)
_c_(87449, _n_(87447, "print", lambda: print), _n_(87448, "result", lambda: result))
_l_(87450)