# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(38512)

except ImportError:
    pass
x = _c_(38515, _a_(38514, _n_(38513, "np", lambda: np), "array"), [24, 27, 30, 29, 18, 14])
_l_(38516)
_c_(38518, _n_(38517, "print", lambda: print), 'Original array:')
_l_(38519)
_c_(38522, _n_(38520, "print", lambda: print), _n_(38521, "x", lambda: x))
_l_(38523)
_n_(38524, "y", lambda: y)[:] = _n_(38525, "x", lambda: x)
_l_(38526)
_c_(38528, _n_(38527, "print", lambda: print), '\nCopy of the said array:')
_l_(38529)
_c_(38532, _n_(38530, "print", lambda: print), _n_(38531, "y", lambda: y))
_l_(38533)