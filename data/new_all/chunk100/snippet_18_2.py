# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(15232)

except ImportError:
    pass
_c_(15234, _n_(15233, "print", lambda: print), 'Original arrays:')
_l_(15235)
_c_(15238, _n_(15236, "print", lambda: print), _n_(15237, "array1", lambda: array1))
_l_(15239)
k = 4
_l_(15240)
result = _c_(15245, _a_(15242, _n_(15241, "np", lambda: np), "argpartition"), _n_(15243, "array1", lambda: array1), _n_(15244, "k", lambda: k))
_l_(15246)
_c_(15248, _n_(15247, "print", lambda: print), '\nk smallest values:')
_l_(15249)
_c_(15254, _n_(15250, "print", lambda: print), _n_(15251, "array1", lambda: array1)[_n_(15252, "result", lambda: result)[:_n_(15253, "k", lambda: k)]])
_l_(15255)