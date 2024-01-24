# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/48276174/hickle-nameerror-name-file-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(400374)

except ImportError:
    pass
try:
    import hickle as hkl
    _l_(400376)

except ImportError:
    pass
try:
    import numpy as np
    _l_(400378)

except ImportError:
    pass
array_obj = _c_(400381, _a_(400380, _n_(400379, "np", lambda: np), "ones"), 32768, dtype='float32')
_l_(400382)
_c_(400386, _a_(400384, _n_(400383, "hkl", lambda: hkl), "dump"), _n_(400385, "array_obj", lambda: array_obj), 'test.hkl', mode='w')
_l_(400387)