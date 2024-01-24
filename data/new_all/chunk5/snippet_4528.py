# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56100786/why-does-adding-two-counters-with-timedelta-values-raise-a-typeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import Counter
    _l_(655352)

except ImportError:
    pass
try:
    from datetime import timedelta
    _l_(655354)

except ImportError:
    pass
a = _c_(655358, _n_(655355, "Counter", lambda: Counter), time=_c_(655357, _n_(655356, "timedelta", lambda: timedelta), microseconds=167242))
_l_(655359)
_n_(655360, "a", lambda: a) + _n_(655361, "a", lambda: a)
_l_(655362)