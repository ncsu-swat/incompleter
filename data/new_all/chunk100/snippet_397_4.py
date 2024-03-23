# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(39478)

except ImportError:
    pass
try:
    from pandas.tseries.offsets import *
    _l_(39480)

except ImportError:
    pass
try:
    import datetime
    _l_(39482)

except ImportError:
    pass
try:
    from datetime import datetime, date
    _l_(39484)

except ImportError:
    pass
dt = _c_(39486, _n_(39485, "datetime", lambda: datetime), 2020, 1, 4)
_l_(39487)
_c_(39489, _n_(39488, "print", lambda: print), 'Specified date:')
_l_(39490)
_c_(39493, _n_(39491, "print", lambda: print), _n_(39492, "dt", lambda: dt))
_l_(39494)
_c_(39496, _n_(39495, "print", lambda: print), '\nOne business day from the said date:')
_l_(39497)
_c_(39500, _n_(39498, "print", lambda: print), _n_(39499, "obday", lambda: obday))
_l_(39501)
_c_(39503, _n_(39502, "print", lambda: print), '\nTwo business days from the said date:')
_l_(39504)
tbday = _n_(39505, "dt", lambda: dt) + 2 * _c_(39507, _n_(39506, "BusinessDay", lambda: BusinessDay))
_l_(39508)
_c_(39511, _n_(39509, "print", lambda: print), _n_(39510, "tbday", lambda: tbday))
_l_(39512)
_c_(39514, _n_(39513, "print", lambda: print), '\nThree business days from the said date:')
_l_(39515)
thbday = _n_(39516, "dt", lambda: dt) + 3 * _c_(39518, _n_(39517, "BusinessDay", lambda: BusinessDay))
_l_(39519)
_c_(39522, _n_(39520, "print", lambda: print), _n_(39521, "thbday", lambda: thbday))
_l_(39523)
_c_(39525, _n_(39524, "print", lambda: print), '\nNext business month end from the said date:')
_l_(39526)
nbday = _n_(39527, "dt", lambda: dt) + _c_(39529, _n_(39528, "BMonthEnd", lambda: BMonthEnd))
_l_(39530)
_c_(39533, _n_(39531, "print", lambda: print), _n_(39532, "nbday", lambda: nbday))
_l_(39534)