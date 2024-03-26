# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(121158)

except ImportError:
    pass
num = _c_(121161, _a_(121160, _n_(121159, "np", lambda: np), "arange"), 18)
_l_(121162)
arr1 = _c_(121166, _a_(121164, _n_(121163, "np", lambda: np), "reshape"), _n_(121165, "num", lambda: num), [6, 3])
_l_(121167)
_c_(121169, _n_(121168, "print", lambda: print), 'Original array:')
_l_(121170)
_c_(121173, _n_(121171, "print", lambda: print), _n_(121172, "arr1", lambda: arr1))
_l_(121174)
_c_(121176, _n_(121175, "print", lambda: print), '\nExtract upper triangular part of the said array:')
_l_(121177)
_c_(121180, _n_(121178, "print", lambda: print), _n_(121179, "result", lambda: result))
_l_(121181)
result = _n_(121182, "arr1", lambda: arr1)[_c_(121185, _a_(121184, _n_(121183, "np", lambda: np), "triu_indices"), 2)]
_l_(121186)
_c_(121188, _n_(121187, "print", lambda: print), '\nExtract upper triangular part of the said array:')
_l_(121189)
_c_(121192, _n_(121190, "print", lambda: print), _n_(121191, "result", lambda: result))
_l_(121193)