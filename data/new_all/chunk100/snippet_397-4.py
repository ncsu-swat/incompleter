# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(114534)

except ImportError:
    pass
try:
    from pandas.tseries.offsets import *
    _l_(114536)

except ImportError:
    pass
try:
    import datetime
    _l_(114538)

except ImportError:
    pass
try:
    from datetime import datetime, date
    _l_(114540)

except ImportError:
    pass
_c_(114542, _n_(114541, "print", lambda: print), 'Specified date:')
_l_(114543)
_c_(114546, _n_(114544, "print", lambda: print), _n_(114545, "dt", lambda: dt))
_l_(114547)
_c_(114549, _n_(114548, "print", lambda: print), '\nOne business day from the said date:')
_l_(114550)
obday = _n_(114551, "dt", lambda: dt) + _c_(114553, _n_(114552, "BusinessDay", lambda: BusinessDay))
_l_(114554)
_c_(114557, _n_(114555, "print", lambda: print), _n_(114556, "obday", lambda: obday))
_l_(114558)
_c_(114560, _n_(114559, "print", lambda: print), '\nTwo business days from the said date:')
_l_(114561)
tbday = _n_(114562, "dt", lambda: dt) + 2 * _c_(114564, _n_(114563, "BusinessDay", lambda: BusinessDay))
_l_(114565)
_c_(114568, _n_(114566, "print", lambda: print), _n_(114567, "tbday", lambda: tbday))
_l_(114569)
_c_(114571, _n_(114570, "print", lambda: print), '\nThree business days from the said date:')
_l_(114572)
thbday = _n_(114573, "dt", lambda: dt) + 3 * _c_(114575, _n_(114574, "BusinessDay", lambda: BusinessDay))
_l_(114576)
_c_(114579, _n_(114577, "print", lambda: print), _n_(114578, "thbday", lambda: thbday))
_l_(114580)
_c_(114582, _n_(114581, "print", lambda: print), '\nNext business month end from the said date:')
_l_(114583)
nbday = _n_(114584, "dt", lambda: dt) + _c_(114586, _n_(114585, "BMonthEnd", lambda: BMonthEnd))
_l_(114587)
_c_(114590, _n_(114588, "print", lambda: print), _n_(114589, "nbday", lambda: nbday))
_l_(114591)