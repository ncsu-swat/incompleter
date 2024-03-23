# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(71249)

except ImportError:
    pass
_c_(71251, _n_(71250, "print", lambda: print), 'Original array: ')
_l_(71252)
_c_(71255, _n_(71253, "print", lambda: print), _n_(71254, "x", lambda: x))
_l_(71256)
_c_(71260, _n_(71257, "print", lambda: print), 'Values bigger than 10 =', _n_(71258, "x", lambda: x)[_n_(71259, "x", lambda: x) > 10])
_l_(71261)
_c_(71267, _n_(71262, "print", lambda: print), 'Their indices are ', _c_(71266, _a_(71264, _n_(71263, "np", lambda: np), "nonzero"), _n_(71265, "x", lambda: x) > 10))
_l_(71268)