# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from datetime import date, timedelta
    _l_(10329)

except ImportError:
    pass

def all_sundays(year):
    _l_(10345)

    dt += _c_(10334, _n_(10330, "timedelta", lambda: timedelta), days=6 - _c_(10333, _a_(10332, _n_(10331, "dt", lambda: dt), "weekday")))
    _l_(10335)
    while _a_(10337, _n_(10336, "dt", lambda: dt), "year") == _n_(10338, "year", lambda: year):
        _l_(10344)

        yield _n_(10339, "dt", lambda: dt)
        _l_(10340)
        dt += _c_(10342, _n_(10341, "timedelta", lambda: timedelta), days=7)
        _l_(10343)
for s in _c_(10347, _n_(10346, "all_sundays", lambda: all_sundays), 2020):
    _l_(10352)

    _c_(10350, _n_(10348, "print", lambda: print), _n_(10349, "s", lambda: s))
    _l_(10351)