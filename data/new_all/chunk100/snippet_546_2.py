# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import time
    _l_(54751)

except ImportError:
    pass
try:
    import numpy as np
    _l_(54753)

except ImportError:
    pass
SIZE = 200000
_l_(54754)
list1 = _c_(54757, _n_(54755, "range", lambda: range), _n_(54756, "SIZE", lambda: SIZE))
_l_(54758)
list2 = _c_(54761, _n_(54759, "range", lambda: range), _n_(54760, "SIZE", lambda: SIZE))
_l_(54762)
arra1 = _c_(54766, _a_(54764, _n_(54763, "np", lambda: np), "arange"), _n_(54765, "SIZE", lambda: SIZE))
_l_(54767)
arra2 = _c_(54771, _a_(54769, _n_(54768, "np", lambda: np), "arange"), _n_(54770, "SIZE", lambda: SIZE))
_l_(54772)
start_list = _c_(54775, _a_(54774, _n_(54773, "time", lambda: time), "time"))
_l_(54776)
result = [(_n_(54777, "x", lambda: x), _n_(54778, "y", lambda: y)) for (x, y) in _c_(54782, _n_(54779, "zip", lambda: zip), _n_(54780, "list1", lambda: list1), _n_(54781, "list2", lambda: list2))]
_l_(54783)
_c_(54785, _n_(54784, "print", lambda: print), 'Time to aggregates elements from each of the iterables:')
_l_(54786)
_c_(54788, _n_(54787, "print", lambda: print), 'List:')
_l_(54789)
_c_(54795, _n_(54790, "print", lambda: print), (_c_(54793, _a_(54792, _n_(54791, "time", lambda: time), "time")) - _n_(54794, "start_list", lambda: start_list)) * 1000)
_l_(54796)
start_array = _c_(54799, _a_(54798, _n_(54797, "time", lambda: time), "time"))
_l_(54800)
_c_(54802, _n_(54801, "print", lambda: print), 'NumPy array:')
_l_(54803)
_c_(54809, _n_(54804, "print", lambda: print), (_c_(54807, _a_(54806, _n_(54805, "time", lambda: time), "time")) - _n_(54808, "start_array", lambda: start_array)) * 1000)
_l_(54810)