# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(113894)

except ImportError:
    pass
x = _c_(113897, _a_(113896, _n_(113895, "np", lambda: np), "array"), [24, 27, 30, 29, 18, 14])
_l_(113898)
_c_(113900, _n_(113899, "print", lambda: print), 'Original array:')
_l_(113901)
_c_(113904, _n_(113902, "print", lambda: print), _n_(113903, "x", lambda: x))
_l_(113905)
_n_(113906, "y", lambda: y)[:] = _n_(113907, "x", lambda: x)
_l_(113908)
_c_(113910, _n_(113909, "print", lambda: print), '\nCopy of the said array:')
_l_(113911)
_c_(113914, _n_(113912, "print", lambda: print), _n_(113913, "y", lambda: y))
_l_(113915)