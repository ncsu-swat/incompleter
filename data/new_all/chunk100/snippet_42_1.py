# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(42043)

except ImportError:
    pass
p = _c_(42046, _a_(42045, _n_(42044, "np", lambda: np), "array"), [[0, 0, 0], [1, 2, 3], [4, 5, 6]])
_l_(42047)
_c_(42049, _n_(42048, "print", lambda: print), 'Original arrays:')
_l_(42050)
_c_(42052, _n_(42051, "print", lambda: print), 'Array-1')
_l_(42053)
_c_(42056, _n_(42054, "print", lambda: print), _n_(42055, "p", lambda: p))
_l_(42057)
_c_(42059, _n_(42058, "print", lambda: print), 'Array-2')
_l_(42060)
_c_(42063, _n_(42061, "print", lambda: print), _n_(42062, "q", lambda: q))
_l_(42064)
_c_(42066, _n_(42065, "print", lambda: print), '\nNew Array:')
_l_(42067)
new_array1 = _n_(42068, "p", lambda: p) + _n_(42069, "q", lambda: q)
_l_(42070)
_c_(42073, _n_(42071, "print", lambda: print), _n_(42072, "new_array1", lambda: new_array1))
_l_(42074)