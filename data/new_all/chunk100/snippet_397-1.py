# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(114360)

except ImportError:
    pass
try:
    from pandas.tseries.offsets import *
    _l_(114362)

except ImportError:
    pass
try:
    import datetime
    _l_(114364)

except ImportError:
    pass
try:
    from datetime import datetime, date
    _l_(114366)

except ImportError:
    pass
dt = _c_(114368, _n_(114367, "datetime", lambda: datetime), 2020, 1, 4)
_l_(114369)
_c_(114371, _n_(114370, "print", lambda: print), 'Specified date:')
_l_(114372)
_c_(114375, _n_(114373, "print", lambda: print), _n_(114374, "dt", lambda: dt))
_l_(114376)
_c_(114378, _n_(114377, "print", lambda: print), '\nOne business day from the said date:')
_l_(114379)
obday = _n_(114380, "dt", lambda: dt) + _c_(114382, _n_(114381, "BusinessDay", lambda: BusinessDay))
_l_(114383)
_c_(114386, _n_(114384, "print", lambda: print), _n_(114385, "obday", lambda: obday))
_l_(114387)
_c_(114389, _n_(114388, "print", lambda: print), '\nTwo business days from the said date:')
_l_(114390)
tbday = _n_(114391, "dt", lambda: dt) + 2 * _c_(114393, _n_(114392, "BusinessDay", lambda: BusinessDay))
_l_(114394)
_c_(114397, _n_(114395, "print", lambda: print), _n_(114396, "tbday", lambda: tbday))
_l_(114398)
_c_(114400, _n_(114399, "print", lambda: print), '\nThree business days from the said date:')
_l_(114401)
_c_(114404, _n_(114402, "print", lambda: print), _n_(114403, "thbday", lambda: thbday))
_l_(114405)
_c_(114407, _n_(114406, "print", lambda: print), '\nNext business month end from the said date:')
_l_(114408)
nbday = _n_(114409, "dt", lambda: dt) + _c_(114411, _n_(114410, "BMonthEnd", lambda: BMonthEnd))
_l_(114412)
_c_(114415, _n_(114413, "print", lambda: print), _n_(114414, "nbday", lambda: nbday))
_l_(114416)