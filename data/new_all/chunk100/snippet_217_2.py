# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(17167)

except ImportError:
    pass
arr = _c_(17171, _a_(17169, _n_(17168, "np", lambda: np), "empty"), (0, 3), _n_(17170, "int", lambda: int))
_l_(17172)
_c_(17174, _n_(17173, "print", lambda: print), 'Empty array:')
_l_(17175)
_c_(17178, _n_(17176, "print", lambda: print), _n_(17177, "arr", lambda: arr))
_l_(17179)
arr = _c_(17186, _a_(17181, _n_(17180, "np", lambda: np), "append"), _n_(17182, "arr", lambda: arr), _c_(17185, _a_(17184, _n_(17183, "np", lambda: np), "array"), [[40, 50, 60]]), axis=0)
_l_(17187)
_c_(17189, _n_(17188, "print", lambda: print), 'After adding two new arrays:')
_l_(17190)
_c_(17193, _n_(17191, "print", lambda: print), _n_(17192, "arr", lambda: arr))
_l_(17194)