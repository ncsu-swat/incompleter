# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(5910)

except ImportError:
    pass
y = _c_(5913, _a_(5912, _n_(5911, "np", lambda: np), "array"), [72, 79, 85, 90, 150, -135, 120, -10, 60, 100.000001])
_l_(5914)
_c_(5916, _n_(5915, "print", lambda: print), 'Original numbers:')
_l_(5917)
_c_(5920, _n_(5918, "print", lambda: print), _n_(5919, "x", lambda: x))
_l_(5921)
_c_(5924, _n_(5922, "print", lambda: print), _n_(5923, "y", lambda: y))
_l_(5925)
_c_(5927, _n_(5926, "print", lambda: print), 'Comparison - equal:')
_l_(5928)
_c_(5935, _n_(5929, "print", lambda: print), _c_(5934, _a_(5931, _n_(5930, "np", lambda: np), "equal"), _n_(5932, "x", lambda: x), _n_(5933, "y", lambda: y)))
_l_(5936)
_c_(5938, _n_(5937, "print", lambda: print), 'Comparison - equal within a tolerance:')
_l_(5939)
_c_(5946, _n_(5940, "print", lambda: print), _c_(5945, _a_(5942, _n_(5941, "np", lambda: np), "allclose"), _n_(5943, "x", lambda: x), _n_(5944, "y", lambda: y)))
_l_(5947)