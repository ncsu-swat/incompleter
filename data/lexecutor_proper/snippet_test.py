# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from datetime import datetime, timedelta
    _l_(65278)

except ImportError:
    pass
try:
    from dateutil.relativedelta import relativedelta
    _l_(65280)

except ImportError:
    pass

# Replace with any valid datetime object
start_date = _c_(65283, _a_(65282, _n_(65281, "datetime", lambda: datetime), "now"))   # e.g., today's date
_l_(65284)   # e.g., today's date

# Replace with desired delta in months
delta_period = 4              # e.g., adding 4 months
_l_(65285)              # e.g., adding 4 months

end_date = _n_(65286, "start_date", lambda: start_date) + _c_(65289, _n_(65287, "relativedelta", lambda: relativedelta), months=_n_(65288, "delta_period", lambda: delta_period))
_l_(65290)
_c_(65293, _n_(65291, "print", lambda: print), "Start Date:", _n_(65292, "start_date", lambda: start_date))
_l_(65294)
_c_(65297, _n_(65295, "print", lambda: print), "End Date:", _n_(65296, "end_date", lambda: end_date))
_l_(65298)