# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(85135)

except ImportError:
    pass
try:
    from datetime import datetime
    _l_(85137)

except ImportError:
    pass
dt = _c_(85140, _a_(85139, _n_(85138, "datetime", lambda: datetime), "utcnow"))
_l_(85141)
_c_(85143, _n_(85142, "print", lambda: print), 'Current date:')
_l_(85144)
_c_(85147, _n_(85145, "print", lambda: print), _n_(85146, "dt", lambda: dt))
_l_(85148)
dt64 = _c_(85152, _a_(85150, _n_(85149, "np", lambda: np), "datetime64"), _n_(85151, "dt", lambda: dt))
_l_(85153)
_c_(85155, _n_(85154, "print", lambda: print), 'Timestamp:')
_l_(85156)
_c_(85159, _n_(85157, "print", lambda: print), _n_(85158, "ts", lambda: ts))
_l_(85160)
_c_(85162, _n_(85161, "print", lambda: print), 'UTC from Timestamp:')
_l_(85163)
_c_(85169, _n_(85164, "print", lambda: print), _c_(85168, _a_(85166, _n_(85165, "datetime", lambda: datetime), "utcfromtimestamp"), _n_(85167, "ts", lambda: ts)))
_l_(85170)