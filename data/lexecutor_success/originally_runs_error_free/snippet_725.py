# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/10624937/convert-datetime-object-to-a-string-of-date-only-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from datetime import datetime
    _l_(1543535)

except ImportError:
    pass

date_time = _c_(1543537, _n_(1543536, "datetime", lambda: datetime), 2012, 2, 23, 0, 0)
_l_(1543538)
date = _c_(1543541, _a_(1543540, _n_(1543539, "date_time", lambda: date_time), "strftime"), '%m/%d/%Y')
_l_(1543542)
_c_(1543545, _n_(1543543, "print", lambda: print), "date: %s" % _n_(1543544, "date", lambda: date))
_l_(1543546)

