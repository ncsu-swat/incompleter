# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(68711)

except ImportError:
    pass
_c_(68713, _n_(68712, "print", lambda: print), 'Array x:')
_l_(68714)
_c_(68717, _n_(68715, "print", lambda: print), _n_(68716, "x", lambda: x))
_l_(68718)
_c_(68720, _n_(68719, "print", lambda: print), 'Array y:')
_l_(68721)
y = _c_(68724, _a_(68723, _n_(68722, "np", lambda: np), "arange"), 4)
_l_(68725)
_c_(68728, _n_(68726, "print", lambda: print), _n_(68727, "y", lambda: y))
_l_(68729)
_c_(68731, _n_(68730, "print", lambda: print), 'Inner of x and y arrays:')
_l_(68732)
_c_(68739, _n_(68733, "print", lambda: print), _c_(68738, _a_(68735, _n_(68734, "np", lambda: np), "inner"), _n_(68736, "x", lambda: x), _n_(68737, "y", lambda: y)))
_l_(68740)