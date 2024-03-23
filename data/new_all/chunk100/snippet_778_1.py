# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(78596)

except ImportError:
    pass
array1 = _c_(78599, _a_(78598, _n_(78597, "np", lambda: np), "array"), [[11, 22, 33, 44, 55], [66, 77, 88, 99, 100]])
_l_(78600)
_c_(78602, _n_(78601, "print", lambda: print), 'Original arrays:')
_l_(78603)
_c_(78606, _n_(78604, "print", lambda: print), _n_(78605, "array1", lambda: array1))
_l_(78607)
result = _n_(78608, "array1", lambda: array1)[:, _n_(78609, "i", lambda: i)]
_l_(78610)
_c_(78612, _n_(78611, "print", lambda: print), 'New array:')
_l_(78613)
_c_(78616, _n_(78614, "print", lambda: print), _n_(78615, "result", lambda: result))
_l_(78617)