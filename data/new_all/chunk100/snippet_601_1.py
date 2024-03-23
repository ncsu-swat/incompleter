# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(63229)

except ImportError:
    pass
_c_(63231, _n_(63230, "print", lambda: print), 'Original matrix:')
_l_(63232)
_c_(63235, _n_(63233, "print", lambda: print), _n_(63234, "m", lambda: m))
_l_(63236)
result = _c_(63241, _a_(63239, _a_(63238, _n_(63237, "np", lambda: np), "linalg"), "inv"), _n_(63240, "m", lambda: m))
_l_(63242)
_c_(63244, _n_(63243, "print", lambda: print), 'Inverse of the said matrix:')
_l_(63245)
_c_(63248, _n_(63246, "print", lambda: print), _n_(63247, "result", lambda: result))
_l_(63249)