# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(118939)

except ImportError:
    pass
_c_(118941, _n_(118940, "print", lambda: print), 'Original array:')
_l_(118942)
_c_(118945, _n_(118943, "print", lambda: print), _n_(118944, "arr1", lambda: arr1))
_l_(118946)
result = _c_(118952, _a_(118948, _n_(118947, "np", lambda: np), "mean"), _c_(118951, _a_(118950, _n_(118949, "arr1", lambda: arr1), "reshape"), -1, 3), axis=1)
_l_(118953)
_c_(118955, _n_(118954, "print", lambda: print), 'Average of every consecutive triplet of elements of the said array:')
_l_(118956)
_c_(118959, _n_(118957, "print", lambda: print), _n_(118958, "result", lambda: result))
_l_(118960)