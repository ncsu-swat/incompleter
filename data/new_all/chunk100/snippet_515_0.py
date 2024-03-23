# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(52743)

except ImportError:
    pass
s_dates = _c_(52747, _a_(52745, _n_(52744, "pd", lambda: pd), "Series"), [0, 1, 2, 3, 4, 5, 6, 7], index=_n_(52746, "index", lambda: index))
_l_(52748)
_c_(52750, _n_(52749, "print", lambda: print), 'Time series object with indexed data:')
_l_(52751)
_c_(52754, _n_(52752, "print", lambda: print), _n_(52753, "s_dates", lambda: s_dates))
_l_(52755)
_c_(52757, _n_(52756, "print", lambda: print), '\nDates of same year:')
_l_(52758)
_c_(52761, _n_(52759, "print", lambda: print), _n_(52760, "s_dates", lambda: s_dates)['2015'])
_l_(52762)
_c_(52764, _n_(52763, "print", lambda: print), '\nDates between 2012-01-01 and 2012-12-31')
_l_(52765)
_c_(52768, _n_(52766, "print", lambda: print), _n_(52767, "s_dates", lambda: s_dates)['2012-01-01':'2012-12-31'])
_l_(52769)