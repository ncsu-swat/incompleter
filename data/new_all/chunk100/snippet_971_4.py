# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(97586)

except ImportError:
    pass
try:
    import datetime
    _l_(97588)

except ImportError:
    pass
_c_(97590, _n_(97589, "print", lambda: print), 'Generate a random integer between 0 and 6:')
_l_(97591)
_c_(97596, _n_(97592, "print", lambda: print), _c_(97595, _a_(97594, _n_(97593, "random", lambda: random), "randrange"), 5))
_l_(97597)
_c_(97599, _n_(97598, "print", lambda: print), 'Generate random integer between 5 and 10, excluding 10:')
_l_(97600)
_c_(97605, _n_(97601, "print", lambda: print), _c_(97604, _a_(97603, _n_(97602, "random", lambda: random), "randrange"), start=5, stop=10))
_l_(97606)
_c_(97608, _n_(97607, "print", lambda: print), 'Generate random integer between 0 and 10, with a step of 3:')
_l_(97609)
_c_(97614, _n_(97610, "print", lambda: print), _c_(97613, _a_(97612, _n_(97611, "random", lambda: random), "randrange"), start=0, stop=10, step=3))
_l_(97615)
_c_(97617, _n_(97616, "print", lambda: print), '\nRandom date between two dates:')
_l_(97618)
end_dt = _c_(97621, _a_(97620, _n_(97619, "datetime", lambda: datetime), "date"), 2019, 3, 1)
_l_(97622)
time_between_dates = _n_(97623, "end_dt", lambda: end_dt) - _n_(97624, "start_dt", lambda: start_dt)
_l_(97625)
days_between_dates = _a_(97627, _n_(97626, "time_between_dates", lambda: time_between_dates), "days")
_l_(97628)
random_number_of_days = _c_(97632, _a_(97630, _n_(97629, "random", lambda: random), "randrange"), _n_(97631, "days_between_dates", lambda: days_between_dates))
_l_(97633)
random_date = _n_(97634, "start_dt", lambda: start_dt) + _c_(97638, _a_(97636, _n_(97635, "datetime", lambda: datetime), "timedelta"), days=_n_(97637, "random_number_of_days", lambda: random_number_of_days))
_l_(97639)
_c_(97642, _n_(97640, "print", lambda: print), _n_(97641, "random_date", lambda: random_date))
_l_(97643)