# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import time
    _l_(55113)

except ImportError:
    pass
try:
    import numpy as np
    _l_(55115)

except ImportError:
    pass
SIZE = 200000
_l_(55116)
list1 = _c_(55119, _n_(55117, "range", lambda: range), _n_(55118, "SIZE", lambda: SIZE))
_l_(55120)
arra1 = _c_(55124, _a_(55122, _n_(55121, "np", lambda: np), "arange"), _n_(55123, "SIZE", lambda: SIZE))
_l_(55125)
arra2 = _c_(55129, _a_(55127, _n_(55126, "np", lambda: np), "arange"), _n_(55128, "SIZE", lambda: SIZE))
_l_(55130)
start_list = _c_(55133, _a_(55132, _n_(55131, "time", lambda: time), "time"))
_l_(55134)
result = [(_n_(55135, "x", lambda: x), _n_(55136, "y", lambda: y)) for (x, y) in _c_(55140, _n_(55137, "zip", lambda: zip), _n_(55138, "list1", lambda: list1), _n_(55139, "list2", lambda: list2))]
_l_(55141)
_c_(55143, _n_(55142, "print", lambda: print), 'Time to aggregates elements from each of the iterables:')
_l_(55144)
_c_(55146, _n_(55145, "print", lambda: print), 'List:')
_l_(55147)
_c_(55153, _n_(55148, "print", lambda: print), (_c_(55151, _a_(55150, _n_(55149, "time", lambda: time), "time")) - _n_(55152, "start_list", lambda: start_list)) * 1000)
_l_(55154)
start_array = _c_(55157, _a_(55156, _n_(55155, "time", lambda: time), "time"))
_l_(55158)
result = _n_(55159, "arra1", lambda: arra1) + _n_(55160, "arra2", lambda: arra2)
_l_(55161)
_c_(55163, _n_(55162, "print", lambda: print), 'NumPy array:')
_l_(55164)
_c_(55170, _n_(55165, "print", lambda: print), (_c_(55168, _a_(55167, _n_(55166, "time", lambda: time), "time")) - _n_(55169, "start_array", lambda: start_array)) * 1000)
_l_(55171)