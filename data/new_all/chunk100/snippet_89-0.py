# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(121116)

except ImportError:
    pass
_c_(121118, _n_(121117, "print", lambda: print), 'Original matrix:')
_l_(121119)
_c_(121122, _n_(121120, "print", lambda: print), _n_(121121, "m", lambda: m))
_l_(121123)
result = _c_(121128, _a_(121126, _a_(121125, _n_(121124, "np", lambda: np), "linalg"), "qr"), _n_(121127, "m", lambda: m))
_l_(121129)
_c_(121131, _n_(121130, "print", lambda: print), 'Decomposition of the said matrix:')
_l_(121132)
_c_(121135, _n_(121133, "print", lambda: print), _n_(121134, "result", lambda: result))
_l_(121136)