# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(15204)

except ImportError:
    pass
array1 = _c_(15207, _a_(15206, _n_(15205, "np", lambda: np), "array"), [1, 7, 8, 2, 0.1, 3, 15, 2.5])
_l_(15208)
_c_(15210, _n_(15209, "print", lambda: print), 'Original arrays:')
_l_(15211)
_c_(15214, _n_(15212, "print", lambda: print), _n_(15213, "array1", lambda: array1))
_l_(15215)
result = _c_(15220, _a_(15217, _n_(15216, "np", lambda: np), "argpartition"), _n_(15218, "array1", lambda: array1), _n_(15219, "k", lambda: k))
_l_(15221)
_c_(15223, _n_(15222, "print", lambda: print), '\nk smallest values:')
_l_(15224)
_c_(15229, _n_(15225, "print", lambda: print), _n_(15226, "array1", lambda: array1)[_n_(15227, "result", lambda: result)[:_n_(15228, "k", lambda: k)]])
_l_(15230)