# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(121232)

except ImportError:
    pass
arr1 = _c_(121236, _a_(121234, _n_(121233, "np", lambda: np), "reshape"), _n_(121235, "num", lambda: num), [6, 3])
_l_(121237)
_c_(121239, _n_(121238, "print", lambda: print), 'Original array:')
_l_(121240)
_c_(121243, _n_(121241, "print", lambda: print), _n_(121242, "arr1", lambda: arr1))
_l_(121244)
result = _n_(121245, "arr1", lambda: arr1)[_c_(121248, _a_(121247, _n_(121246, "np", lambda: np), "triu_indices"), 3)]
_l_(121249)
_c_(121251, _n_(121250, "print", lambda: print), '\nExtract upper triangular part of the said array:')
_l_(121252)
_c_(121255, _n_(121253, "print", lambda: print), _n_(121254, "result", lambda: result))
_l_(121256)
result = _n_(121257, "arr1", lambda: arr1)[_c_(121260, _a_(121259, _n_(121258, "np", lambda: np), "triu_indices"), 2)]
_l_(121261)
_c_(121263, _n_(121262, "print", lambda: print), '\nExtract upper triangular part of the said array:')
_l_(121264)
_c_(121267, _n_(121265, "print", lambda: print), _n_(121266, "result", lambda: result))
_l_(121268)