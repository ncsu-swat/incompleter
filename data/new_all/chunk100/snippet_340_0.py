# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(33550)

except ImportError:
    pass
_c_(33552, _n_(33551, "print", lambda: print), 'Original array:')
_l_(33553)
_c_(33556, _n_(33554, "print", lambda: print), _n_(33555, "array_nums", lambda: array_nums))
_l_(33557)
_c_(33559, _n_(33558, "print", lambda: print), '\nAfter reversing:')
_l_(33560)
_n_(33561, "array_nums", lambda: array_nums)[:] = _n_(33562, "array_nums", lambda: array_nums)[3::-1]
_l_(33563)
_c_(33566, _n_(33564, "print", lambda: print), _n_(33565, "array_nums", lambda: array_nums))
_l_(33567)