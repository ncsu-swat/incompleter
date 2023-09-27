# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/3743222/how-do-i-convert-a-datetime-to-date
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from datetime import datetime
    _l_(1543686)

except ImportError:
    pass

#your date-and-time object
# let's supposed it is defined as
datetime_element = _c_(1543688, _n_(1543687, "datetime", lambda: datetime), 2020, 7, 10, 12, 56, 54, 324893)
_l_(1543689)

# where
# datetime_element = datetime(year, month, day, hour, minute, second, milliseconds)

# WHAT YOU WANT: your date-only object
date_element = _c_(1543692, _a_(1543691, _n_(1543690, "datetime_element", lambda: datetime_element), "date"))
_l_(1543693)

_c_(1543696, _n_(1543694, "print", lambda: print), _n_(1543695, "datetime_element", lambda: datetime_element))
_l_(1543697)

_c_(1543700, _n_(1543698, "print", lambda: print), _n_(1543699, "date_element", lambda: date_element))
_l_(1543701)

