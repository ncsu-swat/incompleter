# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import itertools
    _l_(51947)

except ImportError:
    pass
for combo in _c_(51957, _a_(51949, _n_(51948, "itertools", lambda: itertools), "product"), *[_n_(51950, "d", lambda: d)[_n_(51951, "k", lambda: k)] for k in _c_(51956, _n_(51952, "sorted", lambda: sorted), _c_(51955, _a_(51954, _n_(51953, "d", lambda: d), "keys")))]):
    _l_(51964)

    _c_(51962, _n_(51958, "print", lambda: print), _c_(51961, _a_(51959, '', "join"), _n_(51960, "combo", lambda: combo)))
    _l_(51963)