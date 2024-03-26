# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(115346)

except ImportError:
    pass
_c_(115348, _n_(115347, "print", lambda: print), 'Original array:')
_l_(115349)
_c_(115352, _n_(115350, "print", lambda: print), _n_(115351, "x", lambda: x))
_l_(115353)
_c_(115355, _n_(115354, "print", lambda: print), 'Most frequent value in the above array:')
_l_(115356)
_c_(115364, _n_(115357, "print", lambda: print), _c_(115363, _a_(115362, _c_(115361, _a_(115359, _n_(115358, "np", lambda: np), "bincount"), _n_(115360, "x", lambda: x)), "argmax")))
_l_(115365)