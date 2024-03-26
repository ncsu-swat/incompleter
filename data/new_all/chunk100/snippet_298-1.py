# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(109102)

except ImportError:
    pass
b = _c_(109105, _a_(109104, _n_(109103, "np", lambda: np), "array"), [4, 5])
_l_(109106)
_c_(109109, _n_(109107, "print", lambda: print), 'Array a: ', _n_(109108, "a", lambda: a))
_l_(109110)
_c_(109113, _n_(109111, "print", lambda: print), 'Array b: ', _n_(109112, "b", lambda: b))
_l_(109114)
_c_(109116, _n_(109115, "print", lambda: print), 'a > b')
_l_(109117)
_c_(109124, _n_(109118, "print", lambda: print), _c_(109123, _a_(109120, _n_(109119, "np", lambda: np), "greater"), _n_(109121, "a", lambda: a), _n_(109122, "b", lambda: b)))
_l_(109125)
_c_(109127, _n_(109126, "print", lambda: print), 'a >= b')
_l_(109128)
_c_(109135, _n_(109129, "print", lambda: print), _c_(109134, _a_(109131, _n_(109130, "np", lambda: np), "greater_equal"), _n_(109132, "a", lambda: a), _n_(109133, "b", lambda: b)))
_l_(109136)
_c_(109138, _n_(109137, "print", lambda: print), 'a < b')
_l_(109139)
_c_(109146, _n_(109140, "print", lambda: print), _c_(109145, _a_(109142, _n_(109141, "np", lambda: np), "less"), _n_(109143, "a", lambda: a), _n_(109144, "b", lambda: b)))
_l_(109147)
_c_(109149, _n_(109148, "print", lambda: print), 'a <= b')
_l_(109150)
_c_(109157, _n_(109151, "print", lambda: print), _c_(109156, _a_(109153, _n_(109152, "np", lambda: np), "less_equal"), _n_(109154, "a", lambda: a), _n_(109155, "b", lambda: b)))
_l_(109158)