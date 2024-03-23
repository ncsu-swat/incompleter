# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(82754)

except ImportError:
    pass
arr1 = _c_(82758, _a_(82756, _n_(82755, "np", lambda: np), "reshape"), _n_(82757, "num", lambda: num), [4, 9])
_l_(82759)
_c_(82761, _n_(82760, "print", lambda: print), 'Original array:')
_l_(82762)
_c_(82765, _n_(82763, "print", lambda: print), _n_(82764, "arr1", lambda: arr1))
_l_(82766)
result = _c_(82769, _a_(82768, _n_(82767, "arr1", lambda: arr1), "sum"), axis=0)
_l_(82770)
_c_(82772, _n_(82771, "print", lambda: print), '\nSum of all columns:')
_l_(82773)
_c_(82776, _n_(82774, "print", lambda: print), _n_(82775, "result", lambda: result))
_l_(82777)