# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(75735)

except ImportError:
    pass
try:
    import datetime
    _l_(75737)

except ImportError:
    pass
try:
    from datetime import datetime, date
    _l_(75739)

except ImportError:
    pass
today = _c_(75741, _n_(75740, "datetime", lambda: datetime), 2012, 10, 30)
_l_(75742)
_c_(75745, _n_(75743, "print", lambda: print), 'Current date:', _n_(75744, "today", lambda: today))
_l_(75746)
tomorrow = _n_(75747, "today", lambda: today) + _c_(75750, _a_(75749, _n_(75748, "pd", lambda: pd), "Timedelta"), days=1)
_l_(75751)
_c_(75754, _n_(75752, "print", lambda: print), 'Tomorrow:', _n_(75753, "tomorrow", lambda: tomorrow))
_l_(75755)
_c_(75758, _n_(75756, "print", lambda: print), 'Yesterday:', _n_(75757, "yesterday", lambda: yesterday))
_l_(75759)
date1 = _c_(75761, _n_(75760, "datetime", lambda: datetime), 2016, 8, 2)
_l_(75762)
date2 = _c_(75764, _n_(75763, "datetime", lambda: datetime), 2016, 7, 19)
_l_(75765)
_c_(75769, _n_(75766, "print", lambda: print), '\nDifference between two dates: ', _n_(75767, "date1", lambda: date1) - _n_(75768, "date2", lambda: date2))
_l_(75770)