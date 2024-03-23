# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(39361)

except ImportError:
    pass
try:
    from pandas.tseries.offsets import *
    _l_(39363)

except ImportError:
    pass
try:
    import datetime
    _l_(39365)

except ImportError:
    pass
try:
    from datetime import datetime, date
    _l_(39367)

except ImportError:
    pass
_c_(39369, _n_(39368, "print", lambda: print), 'Specified date:')
_l_(39370)
_c_(39373, _n_(39371, "print", lambda: print), _n_(39372, "dt", lambda: dt))
_l_(39374)
_c_(39376, _n_(39375, "print", lambda: print), '\nOne business day from the said date:')
_l_(39377)
obday = _n_(39378, "dt", lambda: dt) + _c_(39380, _n_(39379, "BusinessDay", lambda: BusinessDay))
_l_(39381)
_c_(39384, _n_(39382, "print", lambda: print), _n_(39383, "obday", lambda: obday))
_l_(39385)
_c_(39387, _n_(39386, "print", lambda: print), '\nTwo business days from the said date:')
_l_(39388)
tbday = _n_(39389, "dt", lambda: dt) + 2 * _c_(39391, _n_(39390, "BusinessDay", lambda: BusinessDay))
_l_(39392)
_c_(39395, _n_(39393, "print", lambda: print), _n_(39394, "tbday", lambda: tbday))
_l_(39396)
_c_(39398, _n_(39397, "print", lambda: print), '\nThree business days from the said date:')
_l_(39399)
thbday = _n_(39400, "dt", lambda: dt) + 3 * _c_(39402, _n_(39401, "BusinessDay", lambda: BusinessDay))
_l_(39403)
_c_(39406, _n_(39404, "print", lambda: print), _n_(39405, "thbday", lambda: thbday))
_l_(39407)
_c_(39409, _n_(39408, "print", lambda: print), '\nNext business month end from the said date:')
_l_(39410)
nbday = _n_(39411, "dt", lambda: dt) + _c_(39413, _n_(39412, "BMonthEnd", lambda: BMonthEnd))
_l_(39414)
_c_(39417, _n_(39415, "print", lambda: print), _n_(39416, "nbday", lambda: nbday))
_l_(39418)