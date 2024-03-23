# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(88170)

except ImportError:
    pass
_c_(88172, _n_(88171, "print", lambda: print), 'Original matrix:')
_l_(88173)
_c_(88176, _n_(88174, "print", lambda: print), _n_(88175, "m", lambda: m))
_l_(88177)
result = _c_(88182, _a_(88180, _a_(88179, _n_(88178, "np", lambda: np), "linalg"), "qr"), _n_(88181, "m", lambda: m))
_l_(88183)
_c_(88185, _n_(88184, "print", lambda: print), 'Decomposition of the said matrix:')
_l_(88186)
_c_(88189, _n_(88187, "print", lambda: print), _n_(88188, "result", lambda: result))
_l_(88190)