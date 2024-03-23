# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(82430)

except ImportError:
    pass
y = _c_(82433, _a_(82432, _n_(82431, "np", lambda: np), "array"), [7, 10])
_l_(82434)
_c_(82436, _n_(82435, "print", lambda: print), 'Original vectors:')
_l_(82437)
_c_(82440, _n_(82438, "print", lambda: print), _n_(82439, "x", lambda: x))
_l_(82441)
_c_(82444, _n_(82442, "print", lambda: print), _n_(82443, "y", lambda: y))
_l_(82445)
_c_(82447, _n_(82446, "print", lambda: print), 'Inner product of said vectors:')
_l_(82448)
_c_(82455, _n_(82449, "print", lambda: print), _c_(82454, _a_(82451, _n_(82450, "np", lambda: np), "dot"), _n_(82452, "x", lambda: x), _n_(82453, "y", lambda: y)))
_l_(82456)