# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(51628)

except ImportError:
    pass
_c_(51630, _n_(51629, "print", lambda: print), '\nOriginal arrays:')
_l_(51631)
y = _c_(51634, _a_(51633, _n_(51632, "np", lambda: np), "array"), (2, 3, 4))
_l_(51635)
_c_(51637, _n_(51636, "print", lambda: print), 'Array-1')
_l_(51638)
_c_(51641, _n_(51639, "print", lambda: print), _n_(51640, "x", lambda: x))
_l_(51642)
_c_(51644, _n_(51643, "print", lambda: print), 'Array-2')
_l_(51645)
_c_(51648, _n_(51646, "print", lambda: print), _n_(51647, "y", lambda: y))
_l_(51649)
new_array = _c_(51654, _a_(51651, _n_(51650, "np", lambda: np), "column_stack"), (_n_(51652, "x", lambda: x), _n_(51653, "y", lambda: y)))
_l_(51655)
_c_(51657, _n_(51656, "print", lambda: print), '\nStack 1-D arrays as columns wise:')
_l_(51658)
_c_(51661, _n_(51659, "print", lambda: print), _n_(51660, "new_array", lambda: new_array))
_l_(51662)