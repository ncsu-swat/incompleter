# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(102466)

except ImportError:
    pass
_c_(102468, _n_(102467, "print", lambda: print), 'Original matrix:\n')
_l_(102469)
X = _c_(102473, _a_(102472, _a_(102471, _n_(102470, "np", lambda: np), "random"), "rand"), 5, 10)
_l_(102474)
_c_(102477, _n_(102475, "print", lambda: print), _n_(102476, "X", lambda: X))
_l_(102478)
_c_(102480, _n_(102479, "print", lambda: print), '\nSubtract the mean of each row of the said matrix:\n')
_l_(102481)
_c_(102484, _n_(102482, "print", lambda: print), _n_(102483, "Y", lambda: Y))
_l_(102485)