# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(10257)

except ImportError:
    pass
s = _c_(10260, _a_(10259, _n_(10258, "pd", lambda: pd), "Series"), [['Red', 'Green', 'White'], ['Red', 'Black'], ['Yellow']])
_l_(10261)
_c_(10263, _n_(10262, "print", lambda: print), 'Original Series of list')
_l_(10264)
_c_(10267, _n_(10265, "print", lambda: print), _n_(10266, "s", lambda: s))
_l_(10268)
_c_(10270, _n_(10269, "print", lambda: print), 'One Series')
_l_(10271)
_c_(10274, _n_(10272, "print", lambda: print), _n_(10273, "s", lambda: s))
_l_(10275)