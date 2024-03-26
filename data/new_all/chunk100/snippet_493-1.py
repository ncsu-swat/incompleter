# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(118674)

except ImportError:
    pass
_c_(118676, _n_(118675, "print", lambda: print), '\nOriginal arrays:')
_l_(118677)
y = _c_(118680, _a_(118679, _n_(118678, "np", lambda: np), "array"), (2, 3, 4))
_l_(118681)
_c_(118683, _n_(118682, "print", lambda: print), 'Array-1')
_l_(118684)
_c_(118687, _n_(118685, "print", lambda: print), _n_(118686, "x", lambda: x))
_l_(118688)
_c_(118690, _n_(118689, "print", lambda: print), 'Array-2')
_l_(118691)
_c_(118694, _n_(118692, "print", lambda: print), _n_(118693, "y", lambda: y))
_l_(118695)
new_array = _c_(118700, _a_(118697, _n_(118696, "np", lambda: np), "column_stack"), (_n_(118698, "x", lambda: x), _n_(118699, "y", lambda: y)))
_l_(118701)
_c_(118703, _n_(118702, "print", lambda: print), '\nStack 1-D arrays as columns wise:')
_l_(118704)
_c_(118707, _n_(118705, "print", lambda: print), _n_(118706, "new_array", lambda: new_array))
_l_(118708)