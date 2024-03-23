# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(17106)

except ImportError:
    pass
arr = _c_(17110, _a_(17108, _n_(17107, "np", lambda: np), "empty"), (0, 3), _n_(17109, "int", lambda: int))
_l_(17111)
_c_(17113, _n_(17112, "print", lambda: print), 'Empty array:')
_l_(17114)
_c_(17117, _n_(17115, "print", lambda: print), _n_(17116, "arr", lambda: arr))
_l_(17118)
arr = _c_(17125, _a_(17120, _n_(17119, "np", lambda: np), "append"), _n_(17121, "arr", lambda: arr), _c_(17124, _a_(17123, _n_(17122, "np", lambda: np), "array"), [[10, 20, 30]]), axis=0)
_l_(17126)
_c_(17128, _n_(17127, "print", lambda: print), 'After adding two new arrays:')
_l_(17129)
_c_(17132, _n_(17130, "print", lambda: print), _n_(17131, "arr", lambda: arr))
_l_(17133)