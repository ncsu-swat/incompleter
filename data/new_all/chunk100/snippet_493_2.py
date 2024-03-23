# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(51698)

except ImportError:
    pass
_c_(51700, _n_(51699, "print", lambda: print), '\nOriginal arrays:')
_l_(51701)
x = _c_(51704, _a_(51703, _n_(51702, "np", lambda: np), "array"), (1, 2, 3))
_l_(51705)
_c_(51707, _n_(51706, "print", lambda: print), 'Array-1')
_l_(51708)
_c_(51711, _n_(51709, "print", lambda: print), _n_(51710, "x", lambda: x))
_l_(51712)
_c_(51714, _n_(51713, "print", lambda: print), 'Array-2')
_l_(51715)
_c_(51718, _n_(51716, "print", lambda: print), _n_(51717, "y", lambda: y))
_l_(51719)
new_array = _c_(51724, _a_(51721, _n_(51720, "np", lambda: np), "column_stack"), (_n_(51722, "x", lambda: x), _n_(51723, "y", lambda: y)))
_l_(51725)
_c_(51727, _n_(51726, "print", lambda: print), '\nStack 1-D arrays as columns wise:')
_l_(51728)
_c_(51731, _n_(51729, "print", lambda: print), _n_(51730, "new_array", lambda: new_array))
_l_(51732)