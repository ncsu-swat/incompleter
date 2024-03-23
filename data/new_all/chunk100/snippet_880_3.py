# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(86595)

except ImportError:
    pass
x = _c_(86604, _a_(86597, _n_(86596, "np", lambda: np), "array"), [200, 300, _a_(86599, _n_(86598, "np", lambda: np), "nan"), _a_(86601, _n_(86600, "np", lambda: np), "nan"), _a_(86603, _n_(86602, "np", lambda: np), "nan"), 700])
_l_(86605)
y = _c_(86614, _a_(86607, _n_(86606, "np", lambda: np), "array"), [[1, 2, 3], [_a_(86609, _n_(86608, "np", lambda: np), "nan"), 0, _a_(86611, _n_(86610, "np", lambda: np), "nan")], [6, 7, _a_(86613, _n_(86612, "np", lambda: np), "nan")]])
_l_(86615)
_c_(86617, _n_(86616, "print", lambda: print), 'Original array:')
_l_(86618)
_c_(86621, _n_(86619, "print", lambda: print), _n_(86620, "x", lambda: x))
_l_(86622)
_c_(86624, _n_(86623, "print", lambda: print), 'After removing nan values:')
_l_(86625)
result = _n_(86626, "x", lambda: x)[_c_(86633, _a_(86628, _n_(86627, "np", lambda: np), "logical_not"), _c_(86632, _a_(86630, _n_(86629, "np", lambda: np), "isnan"), _n_(86631, "x", lambda: x)))]
_l_(86634)
_c_(86637, _n_(86635, "print", lambda: print), _n_(86636, "result", lambda: result))
_l_(86638)
_c_(86640, _n_(86639, "print", lambda: print), '\nOriginal array:')
_l_(86641)
_c_(86644, _n_(86642, "print", lambda: print), _n_(86643, "y", lambda: y))
_l_(86645)
_c_(86647, _n_(86646, "print", lambda: print), 'After removing nan values:')
_l_(86648)
_c_(86651, _n_(86649, "print", lambda: print), _n_(86650, "result", lambda: result))
_l_(86652)