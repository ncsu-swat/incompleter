# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import time
    _l_(54812)

except ImportError:
    pass
try:
    import numpy as np
    _l_(54814)

except ImportError:
    pass
list1 = _c_(54817, _n_(54815, "range", lambda: range), _n_(54816, "SIZE", lambda: SIZE))
_l_(54818)
list2 = _c_(54821, _n_(54819, "range", lambda: range), _n_(54820, "SIZE", lambda: SIZE))
_l_(54822)
arra1 = _c_(54826, _a_(54824, _n_(54823, "np", lambda: np), "arange"), _n_(54825, "SIZE", lambda: SIZE))
_l_(54827)
arra2 = _c_(54831, _a_(54829, _n_(54828, "np", lambda: np), "arange"), _n_(54830, "SIZE", lambda: SIZE))
_l_(54832)
start_list = _c_(54835, _a_(54834, _n_(54833, "time", lambda: time), "time"))
_l_(54836)
result = [(_n_(54837, "x", lambda: x), _n_(54838, "y", lambda: y)) for (x, y) in _c_(54842, _n_(54839, "zip", lambda: zip), _n_(54840, "list1", lambda: list1), _n_(54841, "list2", lambda: list2))]
_l_(54843)
_c_(54845, _n_(54844, "print", lambda: print), 'Time to aggregates elements from each of the iterables:')
_l_(54846)
_c_(54848, _n_(54847, "print", lambda: print), 'List:')
_l_(54849)
_c_(54855, _n_(54850, "print", lambda: print), (_c_(54853, _a_(54852, _n_(54851, "time", lambda: time), "time")) - _n_(54854, "start_list", lambda: start_list)) * 1000)
_l_(54856)
start_array = _c_(54859, _a_(54858, _n_(54857, "time", lambda: time), "time"))
_l_(54860)
result = _n_(54861, "arra1", lambda: arra1) + _n_(54862, "arra2", lambda: arra2)
_l_(54863)
_c_(54865, _n_(54864, "print", lambda: print), 'NumPy array:')
_l_(54866)
_c_(54872, _n_(54867, "print", lambda: print), (_c_(54870, _a_(54869, _n_(54868, "time", lambda: time), "time")) - _n_(54871, "start_array", lambda: start_array)) * 1000)
_l_(54873)