# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(112938)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(112940)

except ImportError:
    pass
np_array = _c_(112944, _a_(112943, _a_(112942, _n_(112941, "np", lambda: np), "random"), "rand"), 12, 3)
_l_(112945)
_c_(112947, _n_(112946, "print", lambda: print), 'Original Numpy array:')
_l_(112948)
_c_(112951, _n_(112949, "print", lambda: print), _n_(112950, "np_array", lambda: np_array))
_l_(112952)
_c_(112957, _n_(112953, "print", lambda: print), 'Type: ', _c_(112956, _n_(112954, "type", lambda: type), _n_(112955, "np_array", lambda: np_array)))
_l_(112958)
_c_(112960, _n_(112959, "print", lambda: print), "\nPanda's DataFrame: ")
_l_(112961)
_c_(112964, _n_(112962, "print", lambda: print), _n_(112963, "df", lambda: df))
_l_(112965)
_c_(112970, _n_(112966, "print", lambda: print), 'Type: ', _c_(112969, _n_(112967, "type", lambda: type), _n_(112968, "df", lambda: df)))
_l_(112971)