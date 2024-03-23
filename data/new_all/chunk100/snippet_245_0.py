# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(19380)

except ImportError:
    pass
x = _c_(19383, _a_(19382, _n_(19381, "np", lambda: np), "arange"), 10)
_l_(19384)
_c_(19386, _n_(19385, "print", lambda: print), 'Original array:')
_l_(19387)
_c_(19390, _n_(19388, "print", lambda: print), _n_(19389, "x", lambda: x))
_l_(19391)
_c_(19396, _a_(19394, _a_(19393, _n_(19392, "np", lambda: np), "random"), "shuffle"), _n_(19395, "x", lambda: x))
_l_(19397)
_c_(19405, _n_(19398, "print", lambda: print), _n_(19399, "x", lambda: x)[_c_(19403, _a_(19401, _n_(19400, "np", lambda: np), "argsort"), _n_(19402, "x", lambda: x))[-_n_(19404, "n", lambda: n):]])
_l_(19406)