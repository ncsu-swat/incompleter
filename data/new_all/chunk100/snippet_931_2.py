# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(94311)

except ImportError:
    pass
x = _c_(94314, _a_(94313, _n_(94312, "np", lambda: np), "array"), [[20, 20, 20, 0], [0, 20, 20, 20], [0, 20, 20, 20], [20, 20, 20, 0], [10, 20, 20, 20]])
_l_(94315)
_c_(94317, _n_(94316, "print", lambda: print), 'Original array:')
_l_(94318)
_c_(94321, _n_(94319, "print", lambda: print), _n_(94320, "x", lambda: x))
_l_(94322)
y = _c_(94338, _a_(94327, _c_(94326, _a_(94324, _n_(94323, "np", lambda: np), "ascontiguousarray"), _n_(94325, "x", lambda: x)), "view"), _c_(94337, _a_(94329, _n_(94328, "np", lambda: np), "dtype"), (_a_(94331, _n_(94330, "np", lambda: np), "void"), _a_(94334, _a_(94333, _n_(94332, "x", lambda: x), "dtype"), "itemsize") * _a_(94336, _n_(94335, "x", lambda: x), "shape")[1])))
_l_(94339)
(_, idx) = _c_(94343, _a_(94341, _n_(94340, "np", lambda: np), "unique"), _n_(94342, "y", lambda: y), return_index=True)
_l_(94344)
_c_(94346, _n_(94345, "print", lambda: print), 'Unique rows of the above array:')
_l_(94347)
_c_(94350, _n_(94348, "print", lambda: print), _n_(94349, "unique_result", lambda: unique_result))
_l_(94351)