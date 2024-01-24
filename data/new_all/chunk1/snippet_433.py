# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/34057159/attributeerror-function-object-has-no-attribute-quad-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from scipy import linalg
    _l_(404563)

except ImportError:
    pass
try:
    from scipy.integrate import quad
    _l_(404565)

except ImportError:
    pass
try:
    import numpy as np
    _l_(404567)

except ImportError:
    pass


a = _c_(404571, _a_(404569, _n_(404568, "integrate", lambda: integrate), "quad"), lambda x: _n_(404570, "x", lambda: x)**2, 0, 4.5)
_l_(404572)
_c_(404575, _n_(404573, "print", lambda: print), _n_(404574, "a", lambda: a))
_l_(404576)