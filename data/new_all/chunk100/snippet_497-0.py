# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import itertools
    _l_(118920)

except ImportError:
    pass
for combo in _c_(118930, _a_(118922, _n_(118921, "itertools", lambda: itertools), "product"), *[_n_(118923, "d", lambda: d)[_n_(118924, "k", lambda: k)] for k in _c_(118929, _n_(118925, "sorted", lambda: sorted), _c_(118928, _a_(118927, _n_(118926, "d", lambda: d), "keys")))]):
    _l_(118937)

    _c_(118935, _n_(118931, "print", lambda: print), _c_(118934, _a_(118932, '', "join"), _n_(118933, "combo", lambda: combo)))
    _l_(118936)