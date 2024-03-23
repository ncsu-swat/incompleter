# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(85094)

except ImportError:
    pass
try:
    from datetime import datetime
    _l_(85096)

except ImportError:
    pass
_c_(85098, _n_(85097, "print", lambda: print), 'Current date:')
_l_(85099)
_c_(85102, _n_(85100, "print", lambda: print), _n_(85101, "dt", lambda: dt))
_l_(85103)
dt64 = _c_(85107, _a_(85105, _n_(85104, "np", lambda: np), "datetime64"), _n_(85106, "dt", lambda: dt))
_l_(85108)
ts = (_n_(85109, "dt64", lambda: dt64) - _c_(85112, _a_(85111, _n_(85110, "np", lambda: np), "datetime64"), '1970-01-01T00:00:00Z')) / _c_(85115, _a_(85114, _n_(85113, "np", lambda: np), "timedelta64"), 1, 's')
_l_(85116)
_c_(85118, _n_(85117, "print", lambda: print), 'Timestamp:')
_l_(85119)
_c_(85122, _n_(85120, "print", lambda: print), _n_(85121, "ts", lambda: ts))
_l_(85123)
_c_(85125, _n_(85124, "print", lambda: print), 'UTC from Timestamp:')
_l_(85126)
_c_(85132, _n_(85127, "print", lambda: print), _c_(85131, _a_(85129, _n_(85128, "datetime", lambda: datetime), "utcfromtimestamp"), _n_(85130, "ts", lambda: ts)))
_l_(85133)