# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(97409)

except ImportError:
    pass
try:
    import datetime
    _l_(97411)

except ImportError:
    pass
_c_(97413, _n_(97412, "print", lambda: print), 'Generate a random integer between 0 and 6:')
_l_(97414)
_c_(97419, _n_(97415, "print", lambda: print), _c_(97418, _a_(97417, _n_(97416, "random", lambda: random), "randrange"), 5))
_l_(97420)
_c_(97422, _n_(97421, "print", lambda: print), 'Generate random integer between 5 and 10, excluding 10:')
_l_(97423)
_c_(97428, _n_(97424, "print", lambda: print), _c_(97427, _a_(97426, _n_(97425, "random", lambda: random), "randrange"), start=5, stop=10))
_l_(97429)
_c_(97431, _n_(97430, "print", lambda: print), 'Generate random integer between 0 and 10, with a step of 3:')
_l_(97432)
_c_(97437, _n_(97433, "print", lambda: print), _c_(97436, _a_(97435, _n_(97434, "random", lambda: random), "randrange"), start=0, stop=10, step=3))
_l_(97438)
_c_(97440, _n_(97439, "print", lambda: print), '\nRandom date between two dates:')
_l_(97441)
start_dt = _c_(97444, _a_(97443, _n_(97442, "datetime", lambda: datetime), "date"), 2019, 2, 1)
_l_(97445)
end_dt = _c_(97448, _a_(97447, _n_(97446, "datetime", lambda: datetime), "date"), 2019, 3, 1)
_l_(97449)
days_between_dates = _a_(97451, _n_(97450, "time_between_dates", lambda: time_between_dates), "days")
_l_(97452)
random_number_of_days = _c_(97456, _a_(97454, _n_(97453, "random", lambda: random), "randrange"), _n_(97455, "days_between_dates", lambda: days_between_dates))
_l_(97457)
random_date = _n_(97458, "start_dt", lambda: start_dt) + _c_(97462, _a_(97460, _n_(97459, "datetime", lambda: datetime), "timedelta"), days=_n_(97461, "random_number_of_days", lambda: random_number_of_days))
_l_(97463)
_c_(97466, _n_(97464, "print", lambda: print), _n_(97465, "random_date", lambda: random_date))
_l_(97467)