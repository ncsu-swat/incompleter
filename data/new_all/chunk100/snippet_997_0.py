# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(98715)

except ImportError:
    pass
_c_(98717, _n_(98716, "print", lambda: print), 'Original array:')
_l_(98718)
_c_(98721, _n_(98719, "print", lambda: print), _n_(98720, "nums", lambda: nums))
_l_(98722)
_c_(98724, _n_(98723, "print", lambda: print), '\nNew array after swapping first and last columns of the said array:')
_l_(98725)
new_nums = _n_(98726, "nums", lambda: nums)[:, ::-1]
_l_(98727)
_c_(98730, _n_(98728, "print", lambda: print), _n_(98729, "new_nums", lambda: new_nums))
_l_(98731)