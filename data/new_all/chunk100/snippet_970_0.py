# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(97330)

except ImportError:
    pass
_c_(97332, _n_(97331, "print", lambda: print), 'Original array:')
_l_(97333)
_c_(97336, _n_(97334, "print", lambda: print), _n_(97335, "x", lambda: x))
_l_(97337)
_n_(97338, "x", lambda: x)[_c_(97341, _a_(97340, _n_(97339, "x", lambda: x), "argmax"))] = -1
_l_(97342)
_c_(97344, _n_(97343, "print", lambda: print), 'Maximum value replaced by -1:')
_l_(97345)
_c_(97348, _n_(97346, "print", lambda: print), _n_(97347, "x", lambda: x))
_l_(97349)