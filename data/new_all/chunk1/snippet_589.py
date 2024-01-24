# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61173063/attributeerror-module-cupy-has-no-attribute-array
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(378128)

except ImportError:
    pass
try:
    import cupy as cp
    _l_(378130)

except ImportError:
    pass

x_gpu = _c_(378133, _a_(378132, _n_(378131, "cp", lambda: cp), "array"), [1, 2, 3])
_l_(378134)