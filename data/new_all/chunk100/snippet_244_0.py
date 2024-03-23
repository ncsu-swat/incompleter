# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(19362)

except ImportError:
    pass
_c_(19364, _n_(19363, "print", lambda: print), 'Original array:')
_l_(19365)
_c_(19368, _n_(19366, "print", lambda: print), _n_(19367, "x", lambda: x))
_l_(19369)
_c_(19371, _n_(19370, "print", lambda: print), '1 on the border and 0 inside in the array')
_l_(19372)
_n_(19373, "x", lambda: x)[1:-1, 1:-1] = 0
_l_(19374)
_c_(19377, _n_(19375, "print", lambda: print), _n_(19376, "x", lambda: x))
_l_(19378)