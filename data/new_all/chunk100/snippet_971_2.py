# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(97469)

except ImportError:
    pass
try:
    import datetime
    _l_(97471)

except ImportError:
    pass
_c_(97473, _n_(97472, "print", lambda: print), 'Generate a random integer between 0 and 6:')
_l_(97474)
_c_(97479, _n_(97475, "print", lambda: print), _c_(97478, _a_(97477, _n_(97476, "random", lambda: random), "randrange"), 5))
_l_(97480)
_c_(97482, _n_(97481, "print", lambda: print), 'Generate random integer between 5 and 10, excluding 10:')
_l_(97483)
_c_(97488, _n_(97484, "print", lambda: print), _c_(97487, _a_(97486, _n_(97485, "random", lambda: random), "randrange"), start=5, stop=10))
_l_(97489)
_c_(97491, _n_(97490, "print", lambda: print), 'Generate random integer between 0 and 10, with a step of 3:')
_l_(97492)
_c_(97497, _n_(97493, "print", lambda: print), _c_(97496, _a_(97495, _n_(97494, "random", lambda: random), "randrange"), start=0, stop=10, step=3))
_l_(97498)
_c_(97500, _n_(97499, "print", lambda: print), '\nRandom date between two dates:')
_l_(97501)
start_dt = _c_(97504, _a_(97503, _n_(97502, "datetime", lambda: datetime), "date"), 2019, 2, 1)
_l_(97505)
end_dt = _c_(97508, _a_(97507, _n_(97506, "datetime", lambda: datetime), "date"), 2019, 3, 1)
_l_(97509)
time_between_dates = _n_(97510, "end_dt", lambda: end_dt) - _n_(97511, "start_dt", lambda: start_dt)
_l_(97512)
days_between_dates = _a_(97514, _n_(97513, "time_between_dates", lambda: time_between_dates), "days")
_l_(97515)
random_number_of_days = _c_(97519, _a_(97517, _n_(97516, "random", lambda: random), "randrange"), _n_(97518, "days_between_dates", lambda: days_between_dates))
_l_(97520)
_c_(97523, _n_(97521, "print", lambda: print), _n_(97522, "random_date", lambda: random_date))
_l_(97524)