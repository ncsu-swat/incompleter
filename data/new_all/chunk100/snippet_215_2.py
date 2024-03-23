# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(17070)

except ImportError:
    pass
nums = _c_(17074, _a_(17073, _a_(17072, _n_(17071, "np", lambda: np), "random"), "randint"), 0, 4, (6, 3))
_l_(17075)
_c_(17077, _n_(17076, "print", lambda: print), 'Original vector:')
_l_(17078)
_c_(17081, _n_(17079, "print", lambda: print), _n_(17080, "nums", lambda: nums))
_l_(17082)
result = _n_(17083, "nums", lambda: nums)[~_n_(17084, "new_nums", lambda: new_nums)]
_l_(17085)
_c_(17087, _n_(17086, "print", lambda: print), '\nRows with unequal values:')
_l_(17088)
_c_(17091, _n_(17089, "print", lambda: print), _n_(17090, "result", lambda: result))
_l_(17092)