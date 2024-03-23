# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(40006)

except ImportError:
    pass
_c_(40008, _n_(40007, "print", lambda: print), 'Original array:')
_l_(40009)
_c_(40012, _n_(40010, "print", lambda: print), _n_(40011, "nums", lambda: nums))
_l_(40013)
_c_(40015, _n_(40014, "print", lambda: print), '\nExtract array of shape (6,6,3) from the said array:')
_l_(40016)
new_nums = _n_(40017, "nums", lambda: nums)[:6, :6, :]
_l_(40018)
_c_(40021, _n_(40019, "print", lambda: print), _n_(40020, "new_nums", lambda: new_nums))
_l_(40022)