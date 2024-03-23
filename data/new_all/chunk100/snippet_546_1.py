# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import time
    _l_(54691)

except ImportError:
    pass
try:
    import numpy as np
    _l_(54693)

except ImportError:
    pass
SIZE = 200000
_l_(54694)
list1 = _c_(54697, _n_(54695, "range", lambda: range), _n_(54696, "SIZE", lambda: SIZE))
_l_(54698)
list2 = _c_(54701, _n_(54699, "range", lambda: range), _n_(54700, "SIZE", lambda: SIZE))
_l_(54702)
arra1 = _c_(54706, _a_(54704, _n_(54703, "np", lambda: np), "arange"), _n_(54705, "SIZE", lambda: SIZE))
_l_(54707)
arra2 = _c_(54711, _a_(54709, _n_(54708, "np", lambda: np), "arange"), _n_(54710, "SIZE", lambda: SIZE))
_l_(54712)
start_list = _c_(54715, _a_(54714, _n_(54713, "time", lambda: time), "time"))
_l_(54716)
result = [(_n_(54717, "x", lambda: x), _n_(54718, "y", lambda: y)) for (x, y) in _c_(54722, _n_(54719, "zip", lambda: zip), _n_(54720, "list1", lambda: list1), _n_(54721, "list2", lambda: list2))]
_l_(54723)
_c_(54725, _n_(54724, "print", lambda: print), 'Time to aggregates elements from each of the iterables:')
_l_(54726)
_c_(54728, _n_(54727, "print", lambda: print), 'List:')
_l_(54729)
_c_(54735, _n_(54730, "print", lambda: print), (_c_(54733, _a_(54732, _n_(54731, "time", lambda: time), "time")) - _n_(54734, "start_list", lambda: start_list)) * 1000)
_l_(54736)
result = _n_(54737, "arra1", lambda: arra1) + _n_(54738, "arra2", lambda: arra2)
_l_(54739)
_c_(54741, _n_(54740, "print", lambda: print), 'NumPy array:')
_l_(54742)
_c_(54748, _n_(54743, "print", lambda: print), (_c_(54746, _a_(54745, _n_(54744, "time", lambda: time), "time")) - _n_(54747, "start_array", lambda: start_array)) * 1000)
_l_(54749)