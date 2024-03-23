# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(17357)

except ImportError:
    pass
_c_(17359, _n_(17358, "print", lambda: print), 'Original array: ')
_l_(17360)
_c_(17363, _n_(17361, "print", lambda: print), _n_(17362, "x", lambda: x))
_l_(17364)
r1 = _c_(17368, _a_(17366, _n_(17365, "np", lambda: np), "ediff1d"), _n_(17367, "x", lambda: x), to_begin=[0, 0], to_end=[200])
_l_(17369)
r2 = _c_(17379, _a_(17371, _n_(17370, "np", lambda: np), "insert"), _c_(17378, _a_(17373, _n_(17372, "np", lambda: np), "append"), _c_(17377, _a_(17375, _n_(17374, "np", lambda: np), "diff"), _n_(17376, "x", lambda: x)), 200), 0, [0, 0])
_l_(17380)
assert _c_(17385, _a_(17382, _n_(17381, "np", lambda: np), "array_equiv"), _n_(17383, "r1", lambda: r1), _n_(17384, "r2", lambda: r2))
_l_(17386)
_c_(17388, _n_(17387, "print", lambda: print), 'Difference between neighboring elements, element-wise, and prepend [0, 0] and append[200] to the said array:')
_l_(17389)
_c_(17392, _n_(17390, "print", lambda: print), _n_(17391, "r2", lambda: r2))
_l_(17393)