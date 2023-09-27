# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/2331592/why-does-datetime-datetime-utcnow-not-contain-timezone-information
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from datetime import timedelta, tzinfo
    _l_(1542397)

except ImportError:
    pass

ZERO = _c_(1542399, _n_(1542398, "timedelta", lambda: timedelta), 0)
_l_(1542400)

# A UTC class.

class UTC(_n_(1542401, "tzinfo", lambda: tzinfo)):
    _l_(1542410)

    """UTC"""

    def utcoffset(self, dt):
        _l_(1542404)

        aux = _n_(1542402, "ZERO", lambda: ZERO)
        _l_(1542403)
        return aux

    def tzname(self, dt):
        _l_(1542406)

        aux = "UTC"
        _l_(1542405)
        return aux

    def dst(self, dt):
        _l_(1542409)

        aux = _n_(1542407, "ZERO", lambda: ZERO)
        _l_(1542408)
        return aux

utc = _c_(1542412, _n_(1542411, "UTC", lambda: UTC))
_l_(1542413)
try:
    from datetime import datetime
    _l_(1542415)

except ImportError:
    pass

now = _c_(1542419, _a_(1542417, _n_(1542416, "datetime", lambda: datetime), "now"), _n_(1542418, "utc", lambda: utc))
_l_(1542420)
try:
    from datetime import datetime, timezone
    _l_(1542422)

except ImportError:
    pass

now = _c_(1542427, _a_(1542424, _n_(1542423, "datetime", lambda: datetime), "now"), _a_(1542426, _n_(1542425, "timezone", lambda: timezone), "utc"))
_l_(1542428)

