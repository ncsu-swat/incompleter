# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(86251)

except ImportError:
    pass
_c_(86253, _n_(86252, "print", lambda: print), 'Original array:')
_l_(86254)
_c_(86257, _n_(86255, "print", lambda: print), _n_(86256, "x", lambda: x))
_l_(86258)
x = _c_(86262, _a_(86260, _n_(86259, "np", lambda: np), "append"), _n_(86261, "x", lambda: x), [[40, 50, 60], [70, 80, 90]])
_l_(86263)
_c_(86265, _n_(86264, "print", lambda: print), 'After append values to the end of the array:')
_l_(86266)
_c_(86269, _n_(86267, "print", lambda: print), _n_(86268, "x", lambda: x))
_l_(86270)