# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(111977)

except ImportError:
    pass
newday = _c_(111980, _a_(111979, _n_(111978, "pd", lambda: pd), "Timestamp"), '2020-02-07')
_l_(111981)
_c_(111983, _n_(111982, "print", lambda: print), 'First date:')
_l_(111984)
_c_(111987, _n_(111985, "print", lambda: print), _n_(111986, "newday", lambda: newday))
_l_(111988)
_c_(111990, _n_(111989, "print", lambda: print), '\nThe day name of the said date:')
_l_(111991)
_c_(111996, _n_(111992, "print", lambda: print), _c_(111995, _a_(111994, _n_(111993, "newday", lambda: newday), "day_name")))
_l_(111997)
_c_(111999, _n_(111998, "print", lambda: print), '\nAdd 2 days with the said date:')
_l_(112000)
newday1 = _n_(112001, "newday", lambda: newday) + _c_(112004, _a_(112003, _n_(112002, "pd", lambda: pd), "Timedelta"), '2 day')
_l_(112005)
_c_(112010, _n_(112006, "print", lambda: print), _c_(112009, _a_(112008, _n_(112007, "newday1", lambda: newday1), "day_name")))
_l_(112011)
_c_(112013, _n_(112012, "print", lambda: print), '\nNext business day:')
_l_(112014)
_c_(112019, _n_(112015, "print", lambda: print), _c_(112018, _a_(112017, _n_(112016, "nbday", lambda: nbday), "day_name")))
_l_(112020)