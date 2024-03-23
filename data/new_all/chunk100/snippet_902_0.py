# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(88325)

except ImportError:
    pass
x = _c_(88329, _a_(88328, _a_(88327, _n_(88326, "np", lambda: np), "random"), "random"), (5, 3))
_l_(88330)
_c_(88332, _n_(88331, "print", lambda: print), 'First array:')
_l_(88333)
_c_(88336, _n_(88334, "print", lambda: print), _n_(88335, "x", lambda: x))
_l_(88337)
_c_(88339, _n_(88338, "print", lambda: print), 'Second array:')
_l_(88340)
_c_(88343, _n_(88341, "print", lambda: print), _n_(88342, "y", lambda: y))
_l_(88344)
z = _c_(88349, _a_(88346, _n_(88345, "np", lambda: np), "dot"), _n_(88347, "x", lambda: x), _n_(88348, "y", lambda: y))
_l_(88350)
_c_(88352, _n_(88351, "print", lambda: print), 'Dot product of two arrays:')
_l_(88353)
_c_(88356, _n_(88354, "print", lambda: print), _n_(88355, "z", lambda: z))
_l_(88357)