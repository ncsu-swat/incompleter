# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(52267)

except ImportError:
    pass
x = _c_(52271, _a_(52270, _a_(52269, _n_(52268, "np", lambda: np), "random"), "random"), (3, 3))
_l_(52272)
_c_(52274, _n_(52273, "print", lambda: print), 'Original Array:')
_l_(52275)
_c_(52278, _n_(52276, "print", lambda: print), _n_(52277, "x", lambda: x))
_l_(52279)
(xmax, xmin) = (_c_(52282, _a_(52281, _n_(52280, "x", lambda: x), "max")), _c_(52285, _a_(52284, _n_(52283, "x", lambda: x), "min")))
_l_(52286)
_c_(52288, _n_(52287, "print", lambda: print), 'After normalization:')
_l_(52289)
_c_(52292, _n_(52290, "print", lambda: print), _n_(52291, "x", lambda: x))
_l_(52293)