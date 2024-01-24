# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58132205/attributeerror-type-object-datetime-datetime-has-no-attribute-timedelta
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from datetime import datetime, time, timedelta
    _l_(688984)

except ImportError:
    pass

att1 = _c_(688987, _a_(688986, _n_(688985, "datetime", lambda: datetime), "strptime"), '09:00 AM','%H:%M %p')
_l_(688988)

att2 = _c_(688991, _a_(688990, _n_(688989, "datetime", lambda: datetime), "timedelta"), minutes = 15)
_l_(688992)

time_zero = _c_(688995, _a_(688994, _n_(688993, "datetime", lambda: datetime), "strptime"), '00:00 AM','%H:%M %p')
_l_(688996)

att3 =  _c_(689001, _a_(689000, (_n_(688997, "att1", lambda: att1) - _n_(688998, "time_zero", lambda: time_zero) + _n_(688999, "att2", lambda: att2)), "strftime"), "%X %p")
_l_(689002)

_c_(689005, _n_(689003, "print", lambda: print), " sTime and Approx time is",_n_(689004, "att3", lambda: att3))
_l_(689006)