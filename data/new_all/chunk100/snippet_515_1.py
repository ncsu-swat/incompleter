# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(52771)

except ImportError:
    pass
index = _c_(52774, _a_(52773, _n_(52772, "pd", lambda: pd), "DatetimeIndex"), ['2011-09-02', '2012-08-04', '2015-09-03', '2010-08-04', '2015-03-03', '2011-08-04', '2015-04-03', '2012-08-04'])
_l_(52775)
_c_(52777, _n_(52776, "print", lambda: print), 'Time series object with indexed data:')
_l_(52778)
_c_(52781, _n_(52779, "print", lambda: print), _n_(52780, "s_dates", lambda: s_dates))
_l_(52782)
_c_(52784, _n_(52783, "print", lambda: print), '\nDates of same year:')
_l_(52785)
_c_(52788, _n_(52786, "print", lambda: print), _n_(52787, "s_dates", lambda: s_dates)['2015'])
_l_(52789)
_c_(52791, _n_(52790, "print", lambda: print), '\nDates between 2012-01-01 and 2012-12-31')
_l_(52792)
_c_(52795, _n_(52793, "print", lambda: print), _n_(52794, "s_dates", lambda: s_dates)['2012-01-01':'2012-12-31'])
_l_(52796)