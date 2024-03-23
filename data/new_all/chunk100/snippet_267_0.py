# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(21495)

except ImportError:
    pass
_c_(21497, _n_(21496, "print", lambda: print), 'Elements of the array in Fortan array:')
_l_(21498)
for x in _c_(21502, _a_(21500, _n_(21499, "np", lambda: np), "nditer"), _n_(21501, "x", lambda: x), order='F'):
    _l_(21507)

    _c_(21505, _n_(21503, "print", lambda: print), _n_(21504, "x", lambda: x), end=' ')
    _l_(21506)
_c_(21509, _n_(21508, "print", lambda: print), '\n')
_l_(21510)