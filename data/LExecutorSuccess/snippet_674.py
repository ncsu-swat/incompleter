# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/6999726/how-can-i-convert-a-datetime-object-to-milliseconds-since-epoch-unix-time-in-p
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from datetime import datetime
    _l_(1544660)

except ImportError:
    pass
try:
    from time import mktime
    _l_(1544662)

except ImportError:
    pass

dt = _c_(1544665, _a_(1544664, _n_(1544663, "datetime", lambda: datetime), "now"))
_l_(1544666)
sec_since_epoch = _c_(1544671, _n_(1544667, "mktime", lambda: mktime), _c_(1544670, _a_(1544669, _n_(1544668, "dt", lambda: dt), "timetuple"))) + _a_(1544673, _n_(1544672, "dt", lambda: dt), "microsecond")/1000000.0
_l_(1544674)

millis_since_epoch = _n_(1544675, "sec_since_epoch", lambda: sec_since_epoch) * 1000
_l_(1544676)

