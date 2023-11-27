# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/32490629/getting-todays-date-in-yyyy-mm-dd-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from datetime import date
    _l_(1539647)

except ImportError:
    pass
today = _c_(1539652, _a_(1539651, _c_(1539650, _a_(1539649, _n_(1539648, "date", lambda: date), "today")), "isoformat"))
_l_(1539653)
_c_(1539656, _n_(1539654, "print", lambda: print), _n_(1539655, "today", lambda: today))  # '2018-12-05'
_l_(1539657)  # '2018-12-05'
try:
    from datetime import datetime
    _l_(1539659)

except ImportError:
    pass
now = _c_(1539664, _a_(1539663, _c_(1539662, _a_(1539661, _n_(1539660, "datetime", lambda: datetime), "today")), "isoformat"))
_l_(1539665)
_c_(1539668, _n_(1539666, "print", lambda: print), _n_(1539667, "now", lambda: now))  # '2018-12-05T11:15:55.126382'
_l_(1539669)  # '2018-12-05T11:15:55.126382'

