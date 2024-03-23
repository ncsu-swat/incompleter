# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(51989)

except ImportError:
    pass
arr1 = _c_(51992, _a_(51991, _n_(51990, "np", lambda: np), "array"), [1, 2, 3, 2, 4, 6, 1, 2, 12, 0, -12, 6])
_l_(51993)
_c_(51995, _n_(51994, "print", lambda: print), 'Original array:')
_l_(51996)
_c_(51999, _n_(51997, "print", lambda: print), _n_(51998, "arr1", lambda: arr1))
_l_(52000)
_c_(52002, _n_(52001, "print", lambda: print), 'Average of every consecutive triplet of elements of the said array:')
_l_(52003)
_c_(52006, _n_(52004, "print", lambda: print), _n_(52005, "result", lambda: result))
_l_(52007)