# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(98403)

except ImportError:
    pass
x = _c_(98408, _a_(98407, _c_(98406, _a_(98405, _n_(98404, "np", lambda: np), "arange"), 16), "reshape"), 4, 4)
_l_(98409)
_c_(98411, _n_(98410, "print", lambda: print), 'Original arrays:')
_l_(98412)
_c_(98415, _n_(98413, "print", lambda: print), _n_(98414, "x", lambda: x))
_l_(98416)
_c_(98418, _n_(98417, "print", lambda: print), '\nArray with size 2x2 from the said array:')
_l_(98419)
_c_(98422, _n_(98420, "print", lambda: print), _n_(98421, "new_array1", lambda: new_array1))
_l_(98423)
_c_(98425, _n_(98424, "print", lambda: print), '\nArray with size 6x6 from the said array:')
_l_(98426)
new_array2 = _c_(98430, _a_(98428, _n_(98427, "np", lambda: np), "resize"), _n_(98429, "x", lambda: x), (6, 6))
_l_(98431)
_c_(98434, _n_(98432, "print", lambda: print), _n_(98433, "new_array2", lambda: new_array2))
_l_(98435)