# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(65577)

except ImportError:
    pass
B = _c_(65580, _a_(65579, _n_(65578, "np", lambda: np), "arange"), 3)
_l_(65581)
_c_(65583, _n_(65582, "print", lambda: print), 'Original array:')
_l_(65584)
_c_(65586, _n_(65585, "print", lambda: print), 'Array-1')
_l_(65587)
_c_(65590, _n_(65588, "print", lambda: print), _n_(65589, "A", lambda: A))
_l_(65591)
_c_(65593, _n_(65592, "print", lambda: print), 'Array-2')
_l_(65594)
_c_(65597, _n_(65595, "print", lambda: print), _n_(65596, "B", lambda: B))
_l_(65598)
_c_(65600, _n_(65599, "print", lambda: print), 'A + B:')
_l_(65601)
new_array = _n_(65602, "A", lambda: A) + _n_(65603, "B", lambda: B)
_l_(65604)
_c_(65607, _n_(65605, "print", lambda: print), _n_(65606, "new_array", lambda: new_array))
_l_(65608)