# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(97526)

except ImportError:
    pass
try:
    import datetime
    _l_(97528)

except ImportError:
    pass
_c_(97530, _n_(97529, "print", lambda: print), 'Generate a random integer between 0 and 6:')
_l_(97531)
_c_(97536, _n_(97532, "print", lambda: print), _c_(97535, _a_(97534, _n_(97533, "random", lambda: random), "randrange"), 5))
_l_(97537)
_c_(97539, _n_(97538, "print", lambda: print), 'Generate random integer between 5 and 10, excluding 10:')
_l_(97540)
_c_(97545, _n_(97541, "print", lambda: print), _c_(97544, _a_(97543, _n_(97542, "random", lambda: random), "randrange"), start=5, stop=10))
_l_(97546)
_c_(97548, _n_(97547, "print", lambda: print), 'Generate random integer between 0 and 10, with a step of 3:')
_l_(97549)
_c_(97554, _n_(97550, "print", lambda: print), _c_(97553, _a_(97552, _n_(97551, "random", lambda: random), "randrange"), start=0, stop=10, step=3))
_l_(97555)
_c_(97557, _n_(97556, "print", lambda: print), '\nRandom date between two dates:')
_l_(97558)
start_dt = _c_(97561, _a_(97560, _n_(97559, "datetime", lambda: datetime), "date"), 2019, 2, 1)
_l_(97562)
end_dt = _c_(97565, _a_(97564, _n_(97563, "datetime", lambda: datetime), "date"), 2019, 3, 1)
_l_(97566)
time_between_dates = _n_(97567, "end_dt", lambda: end_dt) - _n_(97568, "start_dt", lambda: start_dt)
_l_(97569)
random_number_of_days = _c_(97573, _a_(97571, _n_(97570, "random", lambda: random), "randrange"), _n_(97572, "days_between_dates", lambda: days_between_dates))
_l_(97574)
random_date = _n_(97575, "start_dt", lambda: start_dt) + _c_(97579, _a_(97577, _n_(97576, "datetime", lambda: datetime), "timedelta"), days=_n_(97578, "random_number_of_days", lambda: random_number_of_days))
_l_(97580)
_c_(97583, _n_(97581, "print", lambda: print), _n_(97582, "random_date", lambda: random_date))
_l_(97584)