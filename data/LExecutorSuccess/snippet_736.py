# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/2891790/pretty-print-a-numpy-array-without-scientific-notation-and-with-given-precision
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(1539334)

except ImportError:
    pass

x = _c_(1539338, _a_(1539337, _a_(1539336, _n_(1539335, "np", lambda: np), "random"), "random"), [5,5])
_l_(1539339)
_c_(1539344, _n_(1539340, "print", lambda: print), _c_(1539343, _a_(1539342, _n_(1539341, "x", lambda: x), "round"), 3))
_l_(1539345)

