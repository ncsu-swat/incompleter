# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(94947)

except ImportError:
    pass
arr1 = _c_(94962, _a_(94949, _n_(94948, "np", lambda: np), "array"), [[10, 20, 30], [40, 50, _a_(94951, _n_(94950, "np", lambda: np), "nan")], [_a_(94953, _n_(94952, "np", lambda: np), "nan"), 6, _a_(94955, _n_(94954, "np", lambda: np), "nan")], [_a_(94957, _n_(94956, "np", lambda: np), "nan"), _a_(94959, _n_(94958, "np", lambda: np), "nan"), _a_(94961, _n_(94960, "np", lambda: np), "nan")]])
_l_(94963)
_c_(94965, _n_(94964, "print", lambda: print), 'Original array:')
_l_(94966)
_c_(94969, _n_(94967, "print", lambda: print), _n_(94968, "arr1", lambda: arr1))
_l_(94970)
result = _c_(94974, _a_(94972, _n_(94971, "np", lambda: np), "mean"), _n_(94973, "temp", lambda: temp), axis=1)
_l_(94975)
_c_(94977, _n_(94976, "print", lambda: print), 'Averages without NaNs along the said array:')
_l_(94978)
_c_(94985, _n_(94979, "print", lambda: print), _c_(94984, _a_(94981, _n_(94980, "result", lambda: result), "filled"), _a_(94983, _n_(94982, "np", lambda: np), "nan")))
_l_(94986)