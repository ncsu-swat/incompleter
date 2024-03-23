# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import time
    _l_(54634)

except ImportError:
    pass
try:
    import numpy as np
    _l_(54636)

except ImportError:
    pass
SIZE = 200000
_l_(54637)
list1 = _c_(54640, _n_(54638, "range", lambda: range), _n_(54639, "SIZE", lambda: SIZE))
_l_(54641)
list2 = _c_(54644, _n_(54642, "range", lambda: range), _n_(54643, "SIZE", lambda: SIZE))
_l_(54645)
arra1 = _c_(54649, _a_(54647, _n_(54646, "np", lambda: np), "arange"), _n_(54648, "SIZE", lambda: SIZE))
_l_(54650)
arra2 = _c_(54654, _a_(54652, _n_(54651, "np", lambda: np), "arange"), _n_(54653, "SIZE", lambda: SIZE))
_l_(54655)
start_list = _c_(54658, _a_(54657, _n_(54656, "time", lambda: time), "time"))
_l_(54659)
_c_(54661, _n_(54660, "print", lambda: print), 'Time to aggregates elements from each of the iterables:')
_l_(54662)
_c_(54664, _n_(54663, "print", lambda: print), 'List:')
_l_(54665)
_c_(54671, _n_(54666, "print", lambda: print), (_c_(54669, _a_(54668, _n_(54667, "time", lambda: time), "time")) - _n_(54670, "start_list", lambda: start_list)) * 1000)
_l_(54672)
start_array = _c_(54675, _a_(54674, _n_(54673, "time", lambda: time), "time"))
_l_(54676)
result = _n_(54677, "arra1", lambda: arra1) + _n_(54678, "arra2", lambda: arra2)
_l_(54679)
_c_(54681, _n_(54680, "print", lambda: print), 'NumPy array:')
_l_(54682)
_c_(54688, _n_(54683, "print", lambda: print), (_c_(54686, _a_(54685, _n_(54684, "time", lambda: time), "time")) - _n_(54687, "start_array", lambda: start_array)) * 1000)
_l_(54689)