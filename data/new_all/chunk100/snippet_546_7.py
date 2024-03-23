# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import time
    _l_(55053)

except ImportError:
    pass
try:
    import numpy as np
    _l_(55055)

except ImportError:
    pass
SIZE = 200000
_l_(55056)
list1 = _c_(55059, _n_(55057, "range", lambda: range), _n_(55058, "SIZE", lambda: SIZE))
_l_(55060)
list2 = _c_(55063, _n_(55061, "range", lambda: range), _n_(55062, "SIZE", lambda: SIZE))
_l_(55064)
arra1 = _c_(55068, _a_(55066, _n_(55065, "np", lambda: np), "arange"), _n_(55067, "SIZE", lambda: SIZE))
_l_(55069)
arra2 = _c_(55073, _a_(55071, _n_(55070, "np", lambda: np), "arange"), _n_(55072, "SIZE", lambda: SIZE))
_l_(55074)
result = [(_n_(55075, "x", lambda: x), _n_(55076, "y", lambda: y)) for (x, y) in _c_(55080, _n_(55077, "zip", lambda: zip), _n_(55078, "list1", lambda: list1), _n_(55079, "list2", lambda: list2))]
_l_(55081)
_c_(55083, _n_(55082, "print", lambda: print), 'Time to aggregates elements from each of the iterables:')
_l_(55084)
_c_(55086, _n_(55085, "print", lambda: print), 'List:')
_l_(55087)
_c_(55093, _n_(55088, "print", lambda: print), (_c_(55091, _a_(55090, _n_(55089, "time", lambda: time), "time")) - _n_(55092, "start_list", lambda: start_list)) * 1000)
_l_(55094)
start_array = _c_(55097, _a_(55096, _n_(55095, "time", lambda: time), "time"))
_l_(55098)
result = _n_(55099, "arra1", lambda: arra1) + _n_(55100, "arra2", lambda: arra2)
_l_(55101)
_c_(55103, _n_(55102, "print", lambda: print), 'NumPy array:')
_l_(55104)
_c_(55110, _n_(55105, "print", lambda: print), (_c_(55108, _a_(55107, _n_(55106, "time", lambda: time), "time")) - _n_(55109, "start_array", lambda: start_array)) * 1000)
_l_(55111)