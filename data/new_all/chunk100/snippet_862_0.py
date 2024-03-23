# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(85054)

except ImportError:
    pass
try:
    from datetime import datetime
    _l_(85056)

except ImportError:
    pass
dt = _c_(85059, _a_(85058, _n_(85057, "datetime", lambda: datetime), "utcnow"))
_l_(85060)
_c_(85062, _n_(85061, "print", lambda: print), 'Current date:')
_l_(85063)
_c_(85066, _n_(85064, "print", lambda: print), _n_(85065, "dt", lambda: dt))
_l_(85067)
ts = (_n_(85068, "dt64", lambda: dt64) - _c_(85071, _a_(85070, _n_(85069, "np", lambda: np), "datetime64"), '1970-01-01T00:00:00Z')) / _c_(85074, _a_(85073, _n_(85072, "np", lambda: np), "timedelta64"), 1, 's')
_l_(85075)
_c_(85077, _n_(85076, "print", lambda: print), 'Timestamp:')
_l_(85078)
_c_(85081, _n_(85079, "print", lambda: print), _n_(85080, "ts", lambda: ts))
_l_(85082)
_c_(85084, _n_(85083, "print", lambda: print), 'UTC from Timestamp:')
_l_(85085)
_c_(85091, _n_(85086, "print", lambda: print), _c_(85090, _a_(85088, _n_(85087, "datetime", lambda: datetime), "utcfromtimestamp"), _n_(85089, "ts", lambda: ts)))
_l_(85092)