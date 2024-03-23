# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import time
    _l_(54875)

except ImportError:
    pass
try:
    import numpy as np
    _l_(54877)

except ImportError:
    pass
SIZE = 200000
_l_(54878)
list1 = _c_(54881, _n_(54879, "range", lambda: range), _n_(54880, "SIZE", lambda: SIZE))
_l_(54882)
list2 = _c_(54885, _n_(54883, "range", lambda: range), _n_(54884, "SIZE", lambda: SIZE))
_l_(54886)
arra2 = _c_(54890, _a_(54888, _n_(54887, "np", lambda: np), "arange"), _n_(54889, "SIZE", lambda: SIZE))
_l_(54891)
start_list = _c_(54894, _a_(54893, _n_(54892, "time", lambda: time), "time"))
_l_(54895)
result = [(_n_(54896, "x", lambda: x), _n_(54897, "y", lambda: y)) for (x, y) in _c_(54901, _n_(54898, "zip", lambda: zip), _n_(54899, "list1", lambda: list1), _n_(54900, "list2", lambda: list2))]
_l_(54902)
_c_(54904, _n_(54903, "print", lambda: print), 'Time to aggregates elements from each of the iterables:')
_l_(54905)
_c_(54907, _n_(54906, "print", lambda: print), 'List:')
_l_(54908)
_c_(54914, _n_(54909, "print", lambda: print), (_c_(54912, _a_(54911, _n_(54910, "time", lambda: time), "time")) - _n_(54913, "start_list", lambda: start_list)) * 1000)
_l_(54915)
start_array = _c_(54918, _a_(54917, _n_(54916, "time", lambda: time), "time"))
_l_(54919)
result = _n_(54920, "arra1", lambda: arra1) + _n_(54921, "arra2", lambda: arra2)
_l_(54922)
_c_(54924, _n_(54923, "print", lambda: print), 'NumPy array:')
_l_(54925)
_c_(54931, _n_(54926, "print", lambda: print), (_c_(54929, _a_(54928, _n_(54927, "time", lambda: time), "time")) - _n_(54930, "start_array", lambda: start_array)) * 1000)
_l_(54932)