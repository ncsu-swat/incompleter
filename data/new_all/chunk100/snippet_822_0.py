# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(82705)

except ImportError:
    pass
num = _c_(82708, _a_(82707, _n_(82706, "np", lambda: np), "arange"), 36)
_l_(82709)
arr1 = _c_(82713, _a_(82711, _n_(82710, "np", lambda: np), "reshape"), _n_(82712, "num", lambda: num), [4, 9])
_l_(82714)
_c_(82716, _n_(82715, "print", lambda: print), 'Original array:')
_l_(82717)
_c_(82720, _n_(82718, "print", lambda: print), _n_(82719, "arr1", lambda: arr1))
_l_(82721)
_c_(82723, _n_(82722, "print", lambda: print), '\nSum of all columns:')
_l_(82724)
_c_(82727, _n_(82725, "print", lambda: print), _n_(82726, "result", lambda: result))
_l_(82728)