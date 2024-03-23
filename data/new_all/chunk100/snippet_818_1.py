# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(82458)

except ImportError:
    pass
x = _c_(82461, _a_(82460, _n_(82459, "np", lambda: np), "array"), [4, 5])
_l_(82462)
_c_(82464, _n_(82463, "print", lambda: print), 'Original vectors:')
_l_(82465)
_c_(82468, _n_(82466, "print", lambda: print), _n_(82467, "x", lambda: x))
_l_(82469)
_c_(82472, _n_(82470, "print", lambda: print), _n_(82471, "y", lambda: y))
_l_(82473)
_c_(82475, _n_(82474, "print", lambda: print), 'Inner product of said vectors:')
_l_(82476)
_c_(82483, _n_(82477, "print", lambda: print), _c_(82482, _a_(82479, _n_(82478, "np", lambda: np), "dot"), _n_(82480, "x", lambda: x), _n_(82481, "y", lambda: y)))
_l_(82484)