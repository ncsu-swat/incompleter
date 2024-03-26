# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(114302)

except ImportError:
    pass
try:
    from pandas.tseries.offsets import *
    _l_(114304)

except ImportError:
    pass
try:
    import datetime
    _l_(114306)

except ImportError:
    pass
try:
    from datetime import datetime, date
    _l_(114308)

except ImportError:
    pass
dt = _c_(114310, _n_(114309, "datetime", lambda: datetime), 2020, 1, 4)
_l_(114311)
_c_(114313, _n_(114312, "print", lambda: print), 'Specified date:')
_l_(114314)
_c_(114317, _n_(114315, "print", lambda: print), _n_(114316, "dt", lambda: dt))
_l_(114318)
_c_(114320, _n_(114319, "print", lambda: print), '\nOne business day from the said date:')
_l_(114321)
obday = _n_(114322, "dt", lambda: dt) + _c_(114324, _n_(114323, "BusinessDay", lambda: BusinessDay))
_l_(114325)
_c_(114328, _n_(114326, "print", lambda: print), _n_(114327, "obday", lambda: obday))
_l_(114329)
_c_(114331, _n_(114330, "print", lambda: print), '\nTwo business days from the said date:')
_l_(114332)
tbday = _n_(114333, "dt", lambda: dt) + 2 * _c_(114335, _n_(114334, "BusinessDay", lambda: BusinessDay))
_l_(114336)
_c_(114339, _n_(114337, "print", lambda: print), _n_(114338, "tbday", lambda: tbday))
_l_(114340)
_c_(114342, _n_(114341, "print", lambda: print), '\nThree business days from the said date:')
_l_(114343)
thbday = _n_(114344, "dt", lambda: dt) + 3 * _c_(114346, _n_(114345, "BusinessDay", lambda: BusinessDay))
_l_(114347)
_c_(114350, _n_(114348, "print", lambda: print), _n_(114349, "thbday", lambda: thbday))
_l_(114351)
_c_(114353, _n_(114352, "print", lambda: print), '\nNext business month end from the said date:')
_l_(114354)
_c_(114357, _n_(114355, "print", lambda: print), _n_(114356, "nbday", lambda: nbday))
_l_(114358)