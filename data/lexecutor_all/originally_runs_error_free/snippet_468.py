# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/35215161/most-efficient-way-to-map-function-over-numpy-array
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(1538380)

except ImportError:
    pass
x = _c_(1538383, _a_(1538382, _n_(1538381, "np", lambda: np), "array"), [1, 2, 3, 4, 5])
_l_(1538384)
squarer = lambda t: _n_(1538385, "t", lambda: t) ** 2
_l_(1538386)
vfunc = _c_(1538390, _a_(1538388, _n_(1538387, "np", lambda: np), "vectorize"), _n_(1538389, "squarer", lambda: squarer))
_l_(1538391)
_c_(1538394, _n_(1538392, "vfunc", lambda: vfunc), _n_(1538393, "x", lambda: x))
_l_(1538395)
# Output : array([ 1,  4,  9, 16, 25])

