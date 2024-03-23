# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(97645)

except ImportError:
    pass
try:
    import datetime
    _l_(97647)

except ImportError:
    pass
_c_(97649, _n_(97648, "print", lambda: print), 'Generate a random integer between 0 and 6:')
_l_(97650)
_c_(97655, _n_(97651, "print", lambda: print), _c_(97654, _a_(97653, _n_(97652, "random", lambda: random), "randrange"), 5))
_l_(97656)
_c_(97658, _n_(97657, "print", lambda: print), 'Generate random integer between 5 and 10, excluding 10:')
_l_(97659)
_c_(97664, _n_(97660, "print", lambda: print), _c_(97663, _a_(97662, _n_(97661, "random", lambda: random), "randrange"), start=5, stop=10))
_l_(97665)
_c_(97667, _n_(97666, "print", lambda: print), 'Generate random integer between 0 and 10, with a step of 3:')
_l_(97668)
_c_(97673, _n_(97669, "print", lambda: print), _c_(97672, _a_(97671, _n_(97670, "random", lambda: random), "randrange"), start=0, stop=10, step=3))
_l_(97674)
_c_(97676, _n_(97675, "print", lambda: print), '\nRandom date between two dates:')
_l_(97677)
start_dt = _c_(97680, _a_(97679, _n_(97678, "datetime", lambda: datetime), "date"), 2019, 2, 1)
_l_(97681)
time_between_dates = _n_(97682, "end_dt", lambda: end_dt) - _n_(97683, "start_dt", lambda: start_dt)
_l_(97684)
days_between_dates = _a_(97686, _n_(97685, "time_between_dates", lambda: time_between_dates), "days")
_l_(97687)
random_number_of_days = _c_(97691, _a_(97689, _n_(97688, "random", lambda: random), "randrange"), _n_(97690, "days_between_dates", lambda: days_between_dates))
_l_(97692)
random_date = _n_(97693, "start_dt", lambda: start_dt) + _c_(97697, _a_(97695, _n_(97694, "datetime", lambda: datetime), "timedelta"), days=_n_(97696, "random_number_of_days", lambda: random_number_of_days))
_l_(97698)
_c_(97701, _n_(97699, "print", lambda: print), _n_(97700, "random_date", lambda: random_date))
_l_(97702)