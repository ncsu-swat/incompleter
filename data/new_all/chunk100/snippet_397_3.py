# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(39420)

except ImportError:
    pass
try:
    from pandas.tseries.offsets import *
    _l_(39422)

except ImportError:
    pass
try:
    import datetime
    _l_(39424)

except ImportError:
    pass
try:
    from datetime import datetime, date
    _l_(39426)

except ImportError:
    pass
dt = _c_(39428, _n_(39427, "datetime", lambda: datetime), 2020, 1, 4)
_l_(39429)
_c_(39431, _n_(39430, "print", lambda: print), 'Specified date:')
_l_(39432)
_c_(39435, _n_(39433, "print", lambda: print), _n_(39434, "dt", lambda: dt))
_l_(39436)
_c_(39438, _n_(39437, "print", lambda: print), '\nOne business day from the said date:')
_l_(39439)
obday = _n_(39440, "dt", lambda: dt) + _c_(39442, _n_(39441, "BusinessDay", lambda: BusinessDay))
_l_(39443)
_c_(39446, _n_(39444, "print", lambda: print), _n_(39445, "obday", lambda: obday))
_l_(39447)
_c_(39449, _n_(39448, "print", lambda: print), '\nTwo business days from the said date:')
_l_(39450)
_c_(39453, _n_(39451, "print", lambda: print), _n_(39452, "tbday", lambda: tbday))
_l_(39454)
_c_(39456, _n_(39455, "print", lambda: print), '\nThree business days from the said date:')
_l_(39457)
thbday = _n_(39458, "dt", lambda: dt) + 3 * _c_(39460, _n_(39459, "BusinessDay", lambda: BusinessDay))
_l_(39461)
_c_(39464, _n_(39462, "print", lambda: print), _n_(39463, "thbday", lambda: thbday))
_l_(39465)
_c_(39467, _n_(39466, "print", lambda: print), '\nNext business month end from the said date:')
_l_(39468)
nbday = _n_(39469, "dt", lambda: dt) + _c_(39471, _n_(39470, "BMonthEnd", lambda: BMonthEnd))
_l_(39472)
_c_(39475, _n_(39473, "print", lambda: print), _n_(39474, "nbday", lambda: nbday))
_l_(39476)