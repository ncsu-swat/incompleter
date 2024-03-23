# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(39303)

except ImportError:
    pass
try:
    from pandas.tseries.offsets import *
    _l_(39305)

except ImportError:
    pass
try:
    import datetime
    _l_(39307)

except ImportError:
    pass
try:
    from datetime import datetime, date
    _l_(39309)

except ImportError:
    pass
dt = _c_(39311, _n_(39310, "datetime", lambda: datetime), 2020, 1, 4)
_l_(39312)
_c_(39314, _n_(39313, "print", lambda: print), 'Specified date:')
_l_(39315)
_c_(39318, _n_(39316, "print", lambda: print), _n_(39317, "dt", lambda: dt))
_l_(39319)
_c_(39321, _n_(39320, "print", lambda: print), '\nOne business day from the said date:')
_l_(39322)
obday = _n_(39323, "dt", lambda: dt) + _c_(39325, _n_(39324, "BusinessDay", lambda: BusinessDay))
_l_(39326)
_c_(39329, _n_(39327, "print", lambda: print), _n_(39328, "obday", lambda: obday))
_l_(39330)
_c_(39332, _n_(39331, "print", lambda: print), '\nTwo business days from the said date:')
_l_(39333)
tbday = _n_(39334, "dt", lambda: dt) + 2 * _c_(39336, _n_(39335, "BusinessDay", lambda: BusinessDay))
_l_(39337)
_c_(39340, _n_(39338, "print", lambda: print), _n_(39339, "tbday", lambda: tbday))
_l_(39341)
_c_(39343, _n_(39342, "print", lambda: print), '\nThree business days from the said date:')
_l_(39344)
_c_(39347, _n_(39345, "print", lambda: print), _n_(39346, "thbday", lambda: thbday))
_l_(39348)
_c_(39350, _n_(39349, "print", lambda: print), '\nNext business month end from the said date:')
_l_(39351)
nbday = _n_(39352, "dt", lambda: dt) + _c_(39354, _n_(39353, "BMonthEnd", lambda: BMonthEnd))
_l_(39355)
_c_(39358, _n_(39356, "print", lambda: print), _n_(39357, "nbday", lambda: nbday))
_l_(39359)