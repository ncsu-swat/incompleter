# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(106232)

except ImportError:
    pass
_c_(106234, _n_(106233, "print", lambda: print), '\nOriginal arrays:')
_l_(106235)
y = _c_(106238, _a_(106237, _n_(106236, "np", lambda: np), "array"), (2, 3, 4))
_l_(106239)
_c_(106241, _n_(106240, "print", lambda: print), 'Array-1')
_l_(106242)
_c_(106245, _n_(106243, "print", lambda: print), _n_(106244, "x", lambda: x))
_l_(106246)
_c_(106248, _n_(106247, "print", lambda: print), 'Array-2')
_l_(106249)
_c_(106252, _n_(106250, "print", lambda: print), _n_(106251, "y", lambda: y))
_l_(106253)
new_array = _c_(106258, _a_(106255, _n_(106254, "np", lambda: np), "row_stack"), (_n_(106256, "x", lambda: x), _n_(106257, "y", lambda: y)))
_l_(106259)
_c_(106261, _n_(106260, "print", lambda: print), '\nStack 1-D arrays as rows wise:')
_l_(106262)
_c_(106265, _n_(106263, "print", lambda: print), _n_(106264, "new_array", lambda: new_array))
_l_(106266)