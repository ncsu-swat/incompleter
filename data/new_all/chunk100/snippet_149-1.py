# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(102487)

except ImportError:
    pass
_c_(102489, _n_(102488, "print", lambda: print), 'Original matrix:\n')
_l_(102490)
_c_(102493, _n_(102491, "print", lambda: print), _n_(102492, "X", lambda: X))
_l_(102494)
_c_(102496, _n_(102495, "print", lambda: print), '\nSubtract the mean of each row of the said matrix:\n')
_l_(102497)
Y = _n_(102498, "X", lambda: X) - _c_(102501, _a_(102500, _n_(102499, "X", lambda: X), "mean"), axis=1, keepdims=True)
_l_(102502)
_c_(102505, _n_(102503, "print", lambda: print), _n_(102504, "Y", lambda: Y))
_l_(102506)