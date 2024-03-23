# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from datetime import datetime, timedelta
    _l_(4768)

except ImportError:
    pass
try:
    from dateutil.relativedelta import relativedelta
    _l_(4770)

except ImportError:
    pass

# Replace with any valid datetime object
start_date = _c_(4773, _a_(4772, _n_(4771, "datetime", lambda: datetime), "now"))   # e.g., today's date
_l_(4774)   # e.g., today's date

# Replace with desired delta in months
delta_period = 4              # e.g., adding 4 months
_l_(4775)              # e.g., adding 4 months

end_date = _n_(4776, "start_date", lambda: start_date) + _c_(4779, _n_(4777, "relativedelta", lambda: relativedelta), months=_n_(4778, "delta_period", lambda: delta_period))
_l_(4780)
_c_(4783, _n_(4781, "print", lambda: print), "Start Date:", _n_(4782, "start_date", lambda: start_date))
_l_(4784)
_c_(4787, _n_(4785, "print", lambda: print), "End Date:", _n_(4786, "end_date", lambda: end_date))
_l_(4788)