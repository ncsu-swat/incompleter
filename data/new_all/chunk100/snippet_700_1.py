# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(71973)

except ImportError:
    pass
_c_(71975, _n_(71974, "print", lambda: print), 'Original array:')
_l_(71976)
_c_(71979, _n_(71977, "print", lambda: print), _n_(71978, "x", lambda: x))
_l_(71980)
_c_(71982, _n_(71981, "print", lambda: print), '0 on the border and 1 inside in the array')
_l_(71983)
x = _c_(71987, _a_(71985, _n_(71984, "np", lambda: np), "pad"), _n_(71986, "x", lambda: x), pad_width=1, mode='constant', constant_values=0)
_l_(71988)
_c_(71991, _n_(71989, "print", lambda: print), _n_(71990, "x", lambda: x))
_l_(71992)