# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(15873)

except ImportError:
    pass
x = [[1, 0], [1, 1]]
_l_(15874)
_c_(15876, _n_(15875, "print", lambda: print), 'Matrices and vectors.')
_l_(15877)
_c_(15879, _n_(15878, "print", lambda: print), 'x:')
_l_(15880)
_c_(15883, _n_(15881, "print", lambda: print), _n_(15882, "x", lambda: x))
_l_(15884)
_c_(15886, _n_(15885, "print", lambda: print), 'y:')
_l_(15887)
_c_(15890, _n_(15888, "print", lambda: print), _n_(15889, "y", lambda: y))
_l_(15891)
_c_(15893, _n_(15892, "print", lambda: print), 'Matrix product of above two arrays:')
_l_(15894)
_c_(15901, _n_(15895, "print", lambda: print), _c_(15900, _a_(15897, _n_(15896, "np", lambda: np), "matmul"), _n_(15898, "x", lambda: x), _n_(15899, "y", lambda: y)))
_l_(15902)