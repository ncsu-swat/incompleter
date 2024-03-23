# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(70336)

except ImportError:
    pass
a = _c_(70339, _a_(70338, _n_(70337, "np", lambda: np), "array"), [1, 2, 5])
_l_(70340)
_c_(70342, _n_(70341, "print", lambda: print), 'Original 1-d arrays:')
_l_(70343)
_c_(70346, _n_(70344, "print", lambda: print), _n_(70345, "a", lambda: a))
_l_(70347)
_c_(70350, _n_(70348, "print", lambda: print), _n_(70349, "b", lambda: b))
_l_(70351)
_n_(70352, "print", lambda: print)
_l_(70353)
result = _c_(70358, _a_(70355, _n_(70354, "np", lambda: np), "inner"), _n_(70356, "a", lambda: a), _n_(70357, "b", lambda: b))
_l_(70359)
_c_(70361, _n_(70360, "print", lambda: print), 'Inner product of the said vectors:')
_l_(70362)
x = _c_(70367, _a_(70366, _c_(70365, _a_(70364, _n_(70363, "np", lambda: np), "arange"), 9), "reshape"), 3, 3)
_l_(70368)
y = _c_(70373, _a_(70372, _c_(70371, _a_(70370, _n_(70369, "np", lambda: np), "arange"), 3, 12), "reshape"), 3, 3)
_l_(70374)
_c_(70376, _n_(70375, "print", lambda: print), 'Higher dimension arrays:')
_l_(70377)
_c_(70380, _n_(70378, "print", lambda: print), _n_(70379, "x", lambda: x))
_l_(70381)
_c_(70384, _n_(70382, "print", lambda: print), _n_(70383, "y", lambda: y))
_l_(70385)
result = _c_(70390, _a_(70387, _n_(70386, "np", lambda: np), "inner"), _n_(70388, "x", lambda: x), _n_(70389, "y", lambda: y))
_l_(70391)
_c_(70393, _n_(70392, "print", lambda: print), 'Inner product of the said vectors:')
_l_(70394)
_c_(70397, _n_(70395, "print", lambda: print), _n_(70396, "result", lambda: result))
_l_(70398)