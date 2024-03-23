# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(94988)

except ImportError:
    pass
arr1 = _c_(95003, _a_(94990, _n_(94989, "np", lambda: np), "array"), [[10, 20, 30], [40, 50, _a_(94992, _n_(94991, "np", lambda: np), "nan")], [_a_(94994, _n_(94993, "np", lambda: np), "nan"), 6, _a_(94996, _n_(94995, "np", lambda: np), "nan")], [_a_(94998, _n_(94997, "np", lambda: np), "nan"), _a_(95000, _n_(94999, "np", lambda: np), "nan"), _a_(95002, _n_(95001, "np", lambda: np), "nan")]])
_l_(95004)
_c_(95006, _n_(95005, "print", lambda: print), 'Original array:')
_l_(95007)
_c_(95010, _n_(95008, "print", lambda: print), _n_(95009, "arr1", lambda: arr1))
_l_(95011)
temp = _c_(95020, _a_(95014, _a_(95013, _n_(95012, "np", lambda: np), "ma"), "masked_array"), _n_(95015, "arr1", lambda: arr1), _c_(95019, _a_(95017, _n_(95016, "np", lambda: np), "isnan"), _n_(95018, "arr1", lambda: arr1)))
_l_(95021)
_c_(95023, _n_(95022, "print", lambda: print), 'Averages without NaNs along the said array:')
_l_(95024)
_c_(95031, _n_(95025, "print", lambda: print), _c_(95030, _a_(95027, _n_(95026, "result", lambda: result), "filled"), _a_(95029, _n_(95028, "np", lambda: np), "nan")))
_l_(95032)