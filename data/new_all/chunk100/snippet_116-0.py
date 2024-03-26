# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(100985)

except ImportError:
    pass
x = _c_(100988, _a_(100987, _n_(100986, "np", lambda: np), "array"), [72, 79, 85, 90, 150, -135, 120, -10, 60, 100])
_l_(100989)
_c_(100991, _n_(100990, "print", lambda: print), 'Original numbers:')
_l_(100992)
_c_(100995, _n_(100993, "print", lambda: print), _n_(100994, "x", lambda: x))
_l_(100996)
_c_(100999, _n_(100997, "print", lambda: print), _n_(100998, "y", lambda: y))
_l_(101000)
_c_(101002, _n_(101001, "print", lambda: print), 'Comparison - equal:')
_l_(101003)
_c_(101010, _n_(101004, "print", lambda: print), _c_(101009, _a_(101006, _n_(101005, "np", lambda: np), "equal"), _n_(101007, "x", lambda: x), _n_(101008, "y", lambda: y)))
_l_(101011)
_c_(101013, _n_(101012, "print", lambda: print), 'Comparison - equal within a tolerance:')
_l_(101014)
_c_(101021, _n_(101015, "print", lambda: print), _c_(101020, _a_(101017, _n_(101016, "np", lambda: np), "allclose"), _n_(101018, "x", lambda: x), _n_(101019, "y", lambda: y)))
_l_(101022)