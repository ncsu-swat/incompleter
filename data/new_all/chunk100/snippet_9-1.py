# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(121195)

except ImportError:
    pass
num = _c_(121198, _a_(121197, _n_(121196, "np", lambda: np), "arange"), 18)
_l_(121199)
_c_(121201, _n_(121200, "print", lambda: print), 'Original array:')
_l_(121202)
_c_(121205, _n_(121203, "print", lambda: print), _n_(121204, "arr1", lambda: arr1))
_l_(121206)
result = _n_(121207, "arr1", lambda: arr1)[_c_(121210, _a_(121209, _n_(121208, "np", lambda: np), "triu_indices"), 3)]
_l_(121211)
_c_(121213, _n_(121212, "print", lambda: print), '\nExtract upper triangular part of the said array:')
_l_(121214)
_c_(121217, _n_(121215, "print", lambda: print), _n_(121216, "result", lambda: result))
_l_(121218)
result = _n_(121219, "arr1", lambda: arr1)[_c_(121222, _a_(121221, _n_(121220, "np", lambda: np), "triu_indices"), 2)]
_l_(121223)
_c_(121225, _n_(121224, "print", lambda: print), '\nExtract upper triangular part of the said array:')
_l_(121226)
_c_(121229, _n_(121227, "print", lambda: print), _n_(121228, "result", lambda: result))
_l_(121230)