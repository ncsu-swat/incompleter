# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(118710)

except ImportError:
    pass
_c_(118712, _n_(118711, "print", lambda: print), '\nOriginal arrays:')
_l_(118713)
x = _c_(118716, _a_(118715, _n_(118714, "np", lambda: np), "array"), (1, 2, 3))
_l_(118717)
_c_(118719, _n_(118718, "print", lambda: print), 'Array-1')
_l_(118720)
_c_(118723, _n_(118721, "print", lambda: print), _n_(118722, "x", lambda: x))
_l_(118724)
_c_(118726, _n_(118725, "print", lambda: print), 'Array-2')
_l_(118727)
_c_(118730, _n_(118728, "print", lambda: print), _n_(118729, "y", lambda: y))
_l_(118731)
new_array = _c_(118736, _a_(118733, _n_(118732, "np", lambda: np), "column_stack"), (_n_(118734, "x", lambda: x), _n_(118735, "y", lambda: y)))
_l_(118737)
_c_(118739, _n_(118738, "print", lambda: print), '\nStack 1-D arrays as columns wise:')
_l_(118740)
_c_(118743, _n_(118741, "print", lambda: print), _n_(118742, "new_array", lambda: new_array))
_l_(118744)