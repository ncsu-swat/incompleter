# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import time
    _l_(54934)

except ImportError:
    pass
try:
    import numpy as np
    _l_(54936)

except ImportError:
    pass
SIZE = 200000
_l_(54937)
list1 = _c_(54940, _n_(54938, "range", lambda: range), _n_(54939, "SIZE", lambda: SIZE))
_l_(54941)
list2 = _c_(54944, _n_(54942, "range", lambda: range), _n_(54943, "SIZE", lambda: SIZE))
_l_(54945)
arra1 = _c_(54949, _a_(54947, _n_(54946, "np", lambda: np), "arange"), _n_(54948, "SIZE", lambda: SIZE))
_l_(54950)
start_list = _c_(54953, _a_(54952, _n_(54951, "time", lambda: time), "time"))
_l_(54954)
result = [(_n_(54955, "x", lambda: x), _n_(54956, "y", lambda: y)) for (x, y) in _c_(54960, _n_(54957, "zip", lambda: zip), _n_(54958, "list1", lambda: list1), _n_(54959, "list2", lambda: list2))]
_l_(54961)
_c_(54963, _n_(54962, "print", lambda: print), 'Time to aggregates elements from each of the iterables:')
_l_(54964)
_c_(54966, _n_(54965, "print", lambda: print), 'List:')
_l_(54967)
_c_(54973, _n_(54968, "print", lambda: print), (_c_(54971, _a_(54970, _n_(54969, "time", lambda: time), "time")) - _n_(54972, "start_list", lambda: start_list)) * 1000)
_l_(54974)
start_array = _c_(54977, _a_(54976, _n_(54975, "time", lambda: time), "time"))
_l_(54978)
result = _n_(54979, "arra1", lambda: arra1) + _n_(54980, "arra2", lambda: arra2)
_l_(54981)
_c_(54983, _n_(54982, "print", lambda: print), 'NumPy array:')
_l_(54984)
_c_(54990, _n_(54985, "print", lambda: print), (_c_(54988, _a_(54987, _n_(54986, "time", lambda: time), "time")) - _n_(54989, "start_array", lambda: start_array)) * 1000)
_l_(54991)