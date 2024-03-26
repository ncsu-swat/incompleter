# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(102295)

except ImportError:
    pass
x = _c_(102298, _a_(102297, _n_(102296, "np", lambda: np), "array"), [[10, 20, 30], [40, 50, 60]])
_l_(102299)
_c_(102306, _n_(102300, "print", lambda: print), _c_(102305, _a_(102302, _n_(102301, "np", lambda: np), "append"), _n_(102303, "x", lambda: x), _n_(102304, "y", lambda: y), axis=1))
_l_(102307)