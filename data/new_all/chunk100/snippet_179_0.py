# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(14131)

except ImportError:
    pass
_c_(14133, _n_(14132, "print", lambda: print), 'Original arrays:')
_l_(14134)
_c_(14137, _n_(14135, "print", lambda: print), _n_(14136, "x", lambda: x))
_l_(14138)
new_array = _c_(14142, _a_(14140, _n_(14139, "np", lambda: np), "transpose"), _n_(14141, "x", lambda: x))
_l_(14143)
_c_(14145, _n_(14144, "print", lambda: print), 'After reverse the dimensions:')
_l_(14146)
_c_(14149, _n_(14147, "print", lambda: print), _n_(14148, "new_array", lambda: new_array))
_l_(14150)