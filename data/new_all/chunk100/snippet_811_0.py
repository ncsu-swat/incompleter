# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(82138)

except ImportError:
    pass
_c_(82140, _n_(82139, "print", lambda: print), 'Original array:')
_l_(82141)
_c_(82144, _n_(82142, "print", lambda: print), _n_(82143, "x", lambda: x))
_l_(82145)
_c_(82147, _n_(82146, "print", lambda: print), 'Replace the negative values of the said array with 0:')
_l_(82148)
_n_(82149, "x", lambda: x)[_n_(82150, "x", lambda: x) < 0] = 0
_l_(82151)
_c_(82154, _n_(82152, "print", lambda: print), _n_(82153, "x", lambda: x))
_l_(82155)