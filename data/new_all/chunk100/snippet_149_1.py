# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(10298)

except ImportError:
    pass
_c_(10300, _n_(10299, "print", lambda: print), 'Original matrix:\n')
_l_(10301)
_c_(10304, _n_(10302, "print", lambda: print), _n_(10303, "X", lambda: X))
_l_(10305)
_c_(10307, _n_(10306, "print", lambda: print), '\nSubtract the mean of each row of the said matrix:\n')
_l_(10308)
Y = _n_(10309, "X", lambda: X) - _c_(10312, _a_(10311, _n_(10310, "X", lambda: X), "mean"), axis=1, keepdims=True)
_l_(10313)
_c_(10316, _n_(10314, "print", lambda: print), _n_(10315, "Y", lambda: Y))
_l_(10317)