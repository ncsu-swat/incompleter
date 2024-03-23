# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(87573)

except ImportError:
    pass
x = _c_(87576, _a_(87575, _n_(87574, "np", lambda: np), "array"), [1.0, 2.0, 0.2, 0.3])
_l_(87577)
_c_(87579, _n_(87578, "print", lambda: print), 'Original array: ')
_l_(87580)
_c_(87583, _n_(87581, "print", lambda: print), _n_(87582, "x", lambda: x))
_l_(87584)
r1 = _c_(87588, _a_(87586, _n_(87585, "np", lambda: np), "reciprocal"), _n_(87587, "x", lambda: x))
_l_(87589)
assert _c_(87594, _a_(87591, _n_(87590, "np", lambda: np), "array_equal"), _n_(87592, "r1", lambda: r1), _n_(87593, "r2", lambda: r2))
_l_(87595)
_c_(87597, _n_(87596, "print", lambda: print), 'Reciprocal for all elements of the said array:')
_l_(87598)
_c_(87601, _n_(87599, "print", lambda: print), _n_(87600, "r1", lambda: r1))
_l_(87602)