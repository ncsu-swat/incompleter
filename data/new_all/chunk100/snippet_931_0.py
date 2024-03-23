# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(94242)

except ImportError:
    pass
x = _c_(94245, _a_(94244, _n_(94243, "np", lambda: np), "array"), [[20, 20, 20, 0], [0, 20, 20, 20], [0, 20, 20, 20], [20, 20, 20, 0], [10, 20, 20, 20]])
_l_(94246)
_c_(94248, _n_(94247, "print", lambda: print), 'Original array:')
_l_(94249)
_c_(94252, _n_(94250, "print", lambda: print), _n_(94251, "x", lambda: x))
_l_(94253)
(_, idx) = _c_(94257, _a_(94255, _n_(94254, "np", lambda: np), "unique"), _n_(94256, "y", lambda: y), return_index=True)
_l_(94258)
unique_result = _n_(94259, "x", lambda: x)[_n_(94260, "idx", lambda: idx)]
_l_(94261)
_c_(94263, _n_(94262, "print", lambda: print), 'Unique rows of the above array:')
_l_(94264)
_c_(94267, _n_(94265, "print", lambda: print), _n_(94266, "unique_result", lambda: unique_result))
_l_(94268)