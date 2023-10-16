# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/3682748/converting-unix-timestamp-string-to-readable-date
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from datetime import datetime
    _l_(1542772)

except ImportError:
    pass
unixtime = _c_(1542774, _n_(1542773, "int", lambda: int), '1284101485')
_l_(1542775)

# Print with local time
_c_(1542783, _n_(1542776, "print", lambda: print), _c_(1542782, _a_(1542781, _c_(1542780, _a_(1542778, _n_(1542777, "datetime", lambda: datetime), "fromtimestamp"), _n_(1542779, "unixtime", lambda: unixtime)), "strftime"), '%Y-%m-%d %H:%M:%S'))
_l_(1542784)

# Print with UTC time
_c_(1542792, _n_(1542785, "print", lambda: print), _c_(1542791, _a_(1542790, _c_(1542789, _a_(1542787, _n_(1542786, "datetime", lambda: datetime), "utcfromtimestamp"), _n_(1542788, "unixtime", lambda: unixtime)), "strftime"), '%Y-%m-%d %H:%M:%S'))
_l_(1542793)

