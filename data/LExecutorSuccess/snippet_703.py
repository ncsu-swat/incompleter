# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/30071886/how-to-get-current-time-in-python-and-break-up-into-year-month-day-hour-minu
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import time
    _l_(1539036)

except ImportError:
    pass
year, month, day, hour, min = _c_(1539044, _n_(1539037, "map", lambda: map), _n_(1539038, "int", lambda: int), _c_(1539043, _a_(1539042, _c_(1539041, _a_(1539040, _n_(1539039, "time", lambda: time), "strftime"), "%Y %m %d %H %M"), "split")))
_l_(1539045)

