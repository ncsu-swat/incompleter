# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(18694)

except ImportError:
    pass
_c_(18696, _n_(18695, "print", lambda: print), '\nOriginal arrays:')
_l_(18697)
x = _c_(18700, _a_(18699, _n_(18698, "np", lambda: np), "array"), (1, 2, 3))
_l_(18701)
_c_(18703, _n_(18702, "print", lambda: print), 'Array-1')
_l_(18704)
_c_(18707, _n_(18705, "print", lambda: print), _n_(18706, "x", lambda: x))
_l_(18708)
_c_(18710, _n_(18709, "print", lambda: print), 'Array-2')
_l_(18711)
_c_(18714, _n_(18712, "print", lambda: print), _n_(18713, "y", lambda: y))
_l_(18715)
new_array = _c_(18720, _a_(18717, _n_(18716, "np", lambda: np), "row_stack"), (_n_(18718, "x", lambda: x), _n_(18719, "y", lambda: y)))
_l_(18721)
_c_(18723, _n_(18722, "print", lambda: print), '\nStack 1-D arrays as rows wise:')
_l_(18724)
_c_(18727, _n_(18725, "print", lambda: print), _n_(18726, "new_array", lambda: new_array))
_l_(18728)