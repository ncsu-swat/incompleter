# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import time
    _l_(54993)

except ImportError:
    pass
try:
    import numpy as np
    _l_(54995)

except ImportError:
    pass
SIZE = 200000
_l_(54996)
list2 = _c_(54999, _n_(54997, "range", lambda: range), _n_(54998, "SIZE", lambda: SIZE))
_l_(55000)
arra1 = _c_(55004, _a_(55002, _n_(55001, "np", lambda: np), "arange"), _n_(55003, "SIZE", lambda: SIZE))
_l_(55005)
arra2 = _c_(55009, _a_(55007, _n_(55006, "np", lambda: np), "arange"), _n_(55008, "SIZE", lambda: SIZE))
_l_(55010)
start_list = _c_(55013, _a_(55012, _n_(55011, "time", lambda: time), "time"))
_l_(55014)
result = [(_n_(55015, "x", lambda: x), _n_(55016, "y", lambda: y)) for (x, y) in _c_(55020, _n_(55017, "zip", lambda: zip), _n_(55018, "list1", lambda: list1), _n_(55019, "list2", lambda: list2))]
_l_(55021)
_c_(55023, _n_(55022, "print", lambda: print), 'Time to aggregates elements from each of the iterables:')
_l_(55024)
_c_(55026, _n_(55025, "print", lambda: print), 'List:')
_l_(55027)
_c_(55033, _n_(55028, "print", lambda: print), (_c_(55031, _a_(55030, _n_(55029, "time", lambda: time), "time")) - _n_(55032, "start_list", lambda: start_list)) * 1000)
_l_(55034)
start_array = _c_(55037, _a_(55036, _n_(55035, "time", lambda: time), "time"))
_l_(55038)
result = _n_(55039, "arra1", lambda: arra1) + _n_(55040, "arra2", lambda: arra2)
_l_(55041)
_c_(55043, _n_(55042, "print", lambda: print), 'NumPy array:')
_l_(55044)
_c_(55050, _n_(55045, "print", lambda: print), (_c_(55048, _a_(55047, _n_(55046, "time", lambda: time), "time")) - _n_(55049, "start_array", lambda: start_array)) * 1000)
_l_(55051)