# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(18624)

except ImportError:
    pass
_c_(18626, _n_(18625, "print", lambda: print), '\nOriginal arrays:')
_l_(18627)
y = _c_(18630, _a_(18629, _n_(18628, "np", lambda: np), "array"), (2, 3, 4))
_l_(18631)
_c_(18633, _n_(18632, "print", lambda: print), 'Array-1')
_l_(18634)
_c_(18637, _n_(18635, "print", lambda: print), _n_(18636, "x", lambda: x))
_l_(18638)
_c_(18640, _n_(18639, "print", lambda: print), 'Array-2')
_l_(18641)
_c_(18644, _n_(18642, "print", lambda: print), _n_(18643, "y", lambda: y))
_l_(18645)
new_array = _c_(18650, _a_(18647, _n_(18646, "np", lambda: np), "row_stack"), (_n_(18648, "x", lambda: x), _n_(18649, "y", lambda: y)))
_l_(18651)
_c_(18653, _n_(18652, "print", lambda: print), '\nStack 1-D arrays as rows wise:')
_l_(18654)
_c_(18657, _n_(18655, "print", lambda: print), _n_(18656, "new_array", lambda: new_array))
_l_(18658)