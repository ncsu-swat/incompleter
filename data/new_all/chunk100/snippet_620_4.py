# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(65119)

except ImportError:
    pass
a = _c_(65122, _a_(65121, _n_(65120, "np", lambda: np), "array"), [1, 2, 3])
_l_(65123)
b = _c_(65126, _a_(65125, _n_(65124, "np", lambda: np), "array"), [0, 1, 0])
_l_(65127)
_c_(65129, _n_(65128, "print", lambda: print), 'Original 1-d arrays:')
_l_(65130)
_c_(65133, _n_(65131, "print", lambda: print), _n_(65132, "a", lambda: a))
_l_(65134)
_c_(65137, _n_(65135, "print", lambda: print), _n_(65136, "b", lambda: b))
_l_(65138)
result = _c_(65143, _a_(65140, _n_(65139, "np", lambda: np), "einsum"), 'n,n', _n_(65141, "a", lambda: a), _n_(65142, "b", lambda: b))
_l_(65144)
_c_(65146, _n_(65145, "print", lambda: print), 'Einstein’s summation convention of the said arrays:')
_l_(65147)
_c_(65150, _n_(65148, "print", lambda: print), _n_(65149, "result", lambda: result))
_l_(65151)
y = _c_(65156, _a_(65155, _c_(65154, _a_(65153, _n_(65152, "np", lambda: np), "arange"), 3, 12), "reshape"), 3, 3)
_l_(65157)
_c_(65159, _n_(65158, "print", lambda: print), 'Original Higher dimension:')
_l_(65160)
_c_(65163, _n_(65161, "print", lambda: print), _n_(65162, "x", lambda: x))
_l_(65164)
_c_(65167, _n_(65165, "print", lambda: print), _n_(65166, "y", lambda: y))
_l_(65168)
result = _c_(65173, _a_(65170, _n_(65169, "np", lambda: np), "einsum"), 'mk,kn', _n_(65171, "x", lambda: x), _n_(65172, "y", lambda: y))
_l_(65174)
_c_(65176, _n_(65175, "print", lambda: print), 'Einstein’s summation convention of the said arrays:')
_l_(65177)
_c_(65180, _n_(65178, "print", lambda: print), _n_(65179, "result", lambda: result))
_l_(65181)