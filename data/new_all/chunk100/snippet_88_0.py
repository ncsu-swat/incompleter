# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(87516)

except ImportError:
    pass
x = _c_(87519, _a_(87518, _n_(87517, "np", lambda: np), "array"), [1.0, 2.0, 0.2, 0.3])
_l_(87520)
_c_(87522, _n_(87521, "print", lambda: print), 'Original array: ')
_l_(87523)
_c_(87526, _n_(87524, "print", lambda: print), _n_(87525, "x", lambda: x))
_l_(87527)
r2 = 1 / _n_(87528, "x", lambda: x)
_l_(87529)
assert _c_(87534, _a_(87531, _n_(87530, "np", lambda: np), "array_equal"), _n_(87532, "r1", lambda: r1), _n_(87533, "r2", lambda: r2))
_l_(87535)
_c_(87537, _n_(87536, "print", lambda: print), 'Reciprocal for all elements of the said array:')
_l_(87538)
_c_(87541, _n_(87539, "print", lambda: print), _n_(87540, "r1", lambda: r1))
_l_(87542)