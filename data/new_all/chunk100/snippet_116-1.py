# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(101024)

except ImportError:
    pass
y = _c_(101027, _a_(101026, _n_(101025, "np", lambda: np), "array"), [72, 79, 85, 90, 150, -135, 120, -10, 60, 100.000001])
_l_(101028)
_c_(101030, _n_(101029, "print", lambda: print), 'Original numbers:')
_l_(101031)
_c_(101034, _n_(101032, "print", lambda: print), _n_(101033, "x", lambda: x))
_l_(101035)
_c_(101038, _n_(101036, "print", lambda: print), _n_(101037, "y", lambda: y))
_l_(101039)
_c_(101041, _n_(101040, "print", lambda: print), 'Comparison - equal:')
_l_(101042)
_c_(101049, _n_(101043, "print", lambda: print), _c_(101048, _a_(101045, _n_(101044, "np", lambda: np), "equal"), _n_(101046, "x", lambda: x), _n_(101047, "y", lambda: y)))
_l_(101050)
_c_(101052, _n_(101051, "print", lambda: print), 'Comparison - equal within a tolerance:')
_l_(101053)
_c_(101060, _n_(101054, "print", lambda: print), _c_(101059, _a_(101056, _n_(101055, "np", lambda: np), "allclose"), _n_(101057, "x", lambda: x), _n_(101058, "y", lambda: y)))
_l_(101061)