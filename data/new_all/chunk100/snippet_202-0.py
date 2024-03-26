# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(104881)

except ImportError:
    pass
x = [[1, 0], [1, 1]]
_l_(104882)
_c_(104884, _n_(104883, "print", lambda: print), 'Matrices and vectors.')
_l_(104885)
_c_(104887, _n_(104886, "print", lambda: print), 'x:')
_l_(104888)
_c_(104891, _n_(104889, "print", lambda: print), _n_(104890, "x", lambda: x))
_l_(104892)
_c_(104894, _n_(104893, "print", lambda: print), 'y:')
_l_(104895)
_c_(104898, _n_(104896, "print", lambda: print), _n_(104897, "y", lambda: y))
_l_(104899)
_c_(104901, _n_(104900, "print", lambda: print), 'Matrix product of above two arrays:')
_l_(104902)
_c_(104909, _n_(104903, "print", lambda: print), _c_(104908, _a_(104905, _n_(104904, "np", lambda: np), "matmul"), _n_(104906, "x", lambda: x), _n_(104907, "y", lambda: y)))
_l_(104910)