# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(10277)

except ImportError:
    pass
_c_(10279, _n_(10278, "print", lambda: print), 'Original matrix:\n')
_l_(10280)
X = _c_(10284, _a_(10283, _a_(10282, _n_(10281, "np", lambda: np), "random"), "rand"), 5, 10)
_l_(10285)
_c_(10288, _n_(10286, "print", lambda: print), _n_(10287, "X", lambda: X))
_l_(10289)
_c_(10291, _n_(10290, "print", lambda: print), '\nSubtract the mean of each row of the said matrix:\n')
_l_(10292)
_c_(10295, _n_(10293, "print", lambda: print), _n_(10294, "Y", lambda: Y))
_l_(10296)