# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(79138)

except ImportError:
    pass
_c_(79140, _n_(79139, "print", lambda: print), 'Original array:')
_l_(79141)
_c_(79144, _n_(79142, "print", lambda: print), _n_(79143, "a", lambda: a))
_l_(79145)
result = _c_(79150, _a_(79148, _a_(79147, _n_(79146, "np", lambda: np), "linalg"), "det"), _n_(79149, "a", lambda: a))
_l_(79151)
_c_(79153, _n_(79152, "print", lambda: print), 'Determinant of the said array:')
_l_(79154)
_c_(79157, _n_(79155, "print", lambda: print), _n_(79156, "result", lambda: result))
_l_(79158)