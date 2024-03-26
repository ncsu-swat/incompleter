# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(114418)

except ImportError:
    pass
try:
    from pandas.tseries.offsets import *
    _l_(114420)

except ImportError:
    pass
try:
    import datetime
    _l_(114422)

except ImportError:
    pass
try:
    from datetime import datetime, date
    _l_(114424)

except ImportError:
    pass
dt = _c_(114426, _n_(114425, "datetime", lambda: datetime), 2020, 1, 4)
_l_(114427)
_c_(114429, _n_(114428, "print", lambda: print), 'Specified date:')
_l_(114430)
_c_(114433, _n_(114431, "print", lambda: print), _n_(114432, "dt", lambda: dt))
_l_(114434)
_c_(114436, _n_(114435, "print", lambda: print), '\nOne business day from the said date:')
_l_(114437)
_c_(114440, _n_(114438, "print", lambda: print), _n_(114439, "obday", lambda: obday))
_l_(114441)
_c_(114443, _n_(114442, "print", lambda: print), '\nTwo business days from the said date:')
_l_(114444)
tbday = _n_(114445, "dt", lambda: dt) + 2 * _c_(114447, _n_(114446, "BusinessDay", lambda: BusinessDay))
_l_(114448)
_c_(114451, _n_(114449, "print", lambda: print), _n_(114450, "tbday", lambda: tbday))
_l_(114452)
_c_(114454, _n_(114453, "print", lambda: print), '\nThree business days from the said date:')
_l_(114455)
thbday = _n_(114456, "dt", lambda: dt) + 3 * _c_(114458, _n_(114457, "BusinessDay", lambda: BusinessDay))
_l_(114459)
_c_(114462, _n_(114460, "print", lambda: print), _n_(114461, "thbday", lambda: thbday))
_l_(114463)
_c_(114465, _n_(114464, "print", lambda: print), '\nNext business month end from the said date:')
_l_(114466)
nbday = _n_(114467, "dt", lambda: dt) + _c_(114469, _n_(114468, "BMonthEnd", lambda: BMonthEnd))
_l_(114470)
_c_(114473, _n_(114471, "print", lambda: print), _n_(114472, "nbday", lambda: nbday))
_l_(114474)