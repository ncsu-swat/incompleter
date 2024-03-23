# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(15038)

except ImportError:
    pass
_c_(15040, _n_(15039, "print", lambda: print), 'Original array elements:')
_l_(15041)
_c_(15044, _n_(15042, "print", lambda: print), _n_(15043, "x", lambda: x))
_l_(15045)
_c_(15047, _n_(15046, "print", lambda: print), 'Print array values with precision 3:')
_l_(15048)
_c_(15051, _a_(15050, _n_(15049, "np", lambda: np), "set_printoptions"), suppress=True)
_l_(15052)
_c_(15055, _n_(15053, "print", lambda: print), _n_(15054, "x", lambda: x))
_l_(15056)