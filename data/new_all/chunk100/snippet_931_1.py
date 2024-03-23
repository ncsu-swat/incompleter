# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(94270)

except ImportError:
    pass
_c_(94272, _n_(94271, "print", lambda: print), 'Original array:')
_l_(94273)
_c_(94276, _n_(94274, "print", lambda: print), _n_(94275, "x", lambda: x))
_l_(94277)
y = _c_(94293, _a_(94282, _c_(94281, _a_(94279, _n_(94278, "np", lambda: np), "ascontiguousarray"), _n_(94280, "x", lambda: x)), "view"), _c_(94292, _a_(94284, _n_(94283, "np", lambda: np), "dtype"), (_a_(94286, _n_(94285, "np", lambda: np), "void"), _a_(94289, _a_(94288, _n_(94287, "x", lambda: x), "dtype"), "itemsize") * _a_(94291, _n_(94290, "x", lambda: x), "shape")[1])))
_l_(94294)
(_, idx) = _c_(94298, _a_(94296, _n_(94295, "np", lambda: np), "unique"), _n_(94297, "y", lambda: y), return_index=True)
_l_(94299)
unique_result = _n_(94300, "x", lambda: x)[_n_(94301, "idx", lambda: idx)]
_l_(94302)
_c_(94304, _n_(94303, "print", lambda: print), 'Unique rows of the above array:')
_l_(94305)
_c_(94308, _n_(94306, "print", lambda: print), _n_(94307, "unique_result", lambda: unique_result))
_l_(94309)