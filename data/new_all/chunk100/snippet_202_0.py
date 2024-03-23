# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(15842)

except ImportError:
    pass
y = [[3, 1], [2, 2]]
_l_(15843)
_c_(15845, _n_(15844, "print", lambda: print), 'Matrices and vectors.')
_l_(15846)
_c_(15848, _n_(15847, "print", lambda: print), 'x:')
_l_(15849)
_c_(15852, _n_(15850, "print", lambda: print), _n_(15851, "x", lambda: x))
_l_(15853)
_c_(15855, _n_(15854, "print", lambda: print), 'y:')
_l_(15856)
_c_(15859, _n_(15857, "print", lambda: print), _n_(15858, "y", lambda: y))
_l_(15860)
_c_(15862, _n_(15861, "print", lambda: print), 'Matrix product of above two arrays:')
_l_(15863)
_c_(15870, _n_(15864, "print", lambda: print), _c_(15869, _a_(15866, _n_(15865, "np", lambda: np), "matmul"), _n_(15867, "x", lambda: x), _n_(15868, "y", lambda: y)))
_l_(15871)