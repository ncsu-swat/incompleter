# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(114476)

except ImportError:
    pass
try:
    from pandas.tseries.offsets import *
    _l_(114478)

except ImportError:
    pass
try:
    import datetime
    _l_(114480)

except ImportError:
    pass
try:
    from datetime import datetime, date
    _l_(114482)

except ImportError:
    pass
dt = _c_(114484, _n_(114483, "datetime", lambda: datetime), 2020, 1, 4)
_l_(114485)
_c_(114487, _n_(114486, "print", lambda: print), 'Specified date:')
_l_(114488)
_c_(114491, _n_(114489, "print", lambda: print), _n_(114490, "dt", lambda: dt))
_l_(114492)
_c_(114494, _n_(114493, "print", lambda: print), '\nOne business day from the said date:')
_l_(114495)
obday = _n_(114496, "dt", lambda: dt) + _c_(114498, _n_(114497, "BusinessDay", lambda: BusinessDay))
_l_(114499)
_c_(114502, _n_(114500, "print", lambda: print), _n_(114501, "obday", lambda: obday))
_l_(114503)
_c_(114505, _n_(114504, "print", lambda: print), '\nTwo business days from the said date:')
_l_(114506)
_c_(114509, _n_(114507, "print", lambda: print), _n_(114508, "tbday", lambda: tbday))
_l_(114510)
_c_(114512, _n_(114511, "print", lambda: print), '\nThree business days from the said date:')
_l_(114513)
thbday = _n_(114514, "dt", lambda: dt) + 3 * _c_(114516, _n_(114515, "BusinessDay", lambda: BusinessDay))
_l_(114517)
_c_(114520, _n_(114518, "print", lambda: print), _n_(114519, "thbday", lambda: thbday))
_l_(114521)
_c_(114523, _n_(114522, "print", lambda: print), '\nNext business month end from the said date:')
_l_(114524)
nbday = _n_(114525, "dt", lambda: dt) + _c_(114527, _n_(114526, "BMonthEnd", lambda: BMonthEnd))
_l_(114528)
_c_(114531, _n_(114529, "print", lambda: print), _n_(114530, "nbday", lambda: nbday))
_l_(114532)