# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(107632)

except ImportError:
    pass
_c_(107634, _n_(107633, "print", lambda: print), 'Original Numpy array:')
_l_(107635)
_c_(107638, _n_(107636, "print", lambda: print), _n_(107637, "np_array", lambda: np_array))
_l_(107639)
_c_(107644, _n_(107640, "print", lambda: print), 'Type: ', _c_(107643, _n_(107641, "type", lambda: type), _n_(107642, "np_array", lambda: np_array)))
_l_(107645)
result = _c_(107649, _a_(107647, _n_(107646, "np", lambda: np), "diagonal"), _n_(107648, "np_array", lambda: np_array), axis1=1, axis2=2)
_l_(107650)
_c_(107652, _n_(107651, "print", lambda: print), '\n2D diagonals: ')
_l_(107653)
_c_(107656, _n_(107654, "print", lambda: print), _n_(107655, "result", lambda: result))
_l_(107657)
_c_(107662, _n_(107658, "print", lambda: print), 'Type: ', _c_(107661, _n_(107659, "type", lambda: type), _n_(107660, "result", lambda: result)))
_l_(107663)