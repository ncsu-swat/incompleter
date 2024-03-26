# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(104912)

except ImportError:
    pass
y = [[3, 1], [2, 2]]
_l_(104913)
_c_(104915, _n_(104914, "print", lambda: print), 'Matrices and vectors.')
_l_(104916)
_c_(104918, _n_(104917, "print", lambda: print), 'x:')
_l_(104919)
_c_(104922, _n_(104920, "print", lambda: print), _n_(104921, "x", lambda: x))
_l_(104923)
_c_(104925, _n_(104924, "print", lambda: print), 'y:')
_l_(104926)
_c_(104929, _n_(104927, "print", lambda: print), _n_(104928, "y", lambda: y))
_l_(104930)
_c_(104932, _n_(104931, "print", lambda: print), 'Matrix product of above two arrays:')
_l_(104933)
_c_(104940, _n_(104934, "print", lambda: print), _c_(104939, _a_(104936, _n_(104935, "np", lambda: np), "matmul"), _n_(104937, "x", lambda: x), _n_(104938, "y", lambda: y)))
_l_(104941)