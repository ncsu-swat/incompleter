# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(97351)

except ImportError:
    pass
try:
    import datetime
    _l_(97353)

except ImportError:
    pass
_c_(97355, _n_(97354, "print", lambda: print), 'Generate a random integer between 0 and 6:')
_l_(97356)
_c_(97361, _n_(97357, "print", lambda: print), _c_(97360, _a_(97359, _n_(97358, "random", lambda: random), "randrange"), 5))
_l_(97362)
_c_(97364, _n_(97363, "print", lambda: print), 'Generate random integer between 5 and 10, excluding 10:')
_l_(97365)
_c_(97370, _n_(97366, "print", lambda: print), _c_(97369, _a_(97368, _n_(97367, "random", lambda: random), "randrange"), start=5, stop=10))
_l_(97371)
_c_(97373, _n_(97372, "print", lambda: print), 'Generate random integer between 0 and 10, with a step of 3:')
_l_(97374)
_c_(97379, _n_(97375, "print", lambda: print), _c_(97378, _a_(97377, _n_(97376, "random", lambda: random), "randrange"), start=0, stop=10, step=3))
_l_(97380)
_c_(97382, _n_(97381, "print", lambda: print), '\nRandom date between two dates:')
_l_(97383)
start_dt = _c_(97386, _a_(97385, _n_(97384, "datetime", lambda: datetime), "date"), 2019, 2, 1)
_l_(97387)
end_dt = _c_(97390, _a_(97389, _n_(97388, "datetime", lambda: datetime), "date"), 2019, 3, 1)
_l_(97391)
time_between_dates = _n_(97392, "end_dt", lambda: end_dt) - _n_(97393, "start_dt", lambda: start_dt)
_l_(97394)
days_between_dates = _a_(97396, _n_(97395, "time_between_dates", lambda: time_between_dates), "days")
_l_(97397)
random_date = _n_(97398, "start_dt", lambda: start_dt) + _c_(97402, _a_(97400, _n_(97399, "datetime", lambda: datetime), "timedelta"), days=_n_(97401, "random_number_of_days", lambda: random_number_of_days))
_l_(97403)
_c_(97406, _n_(97404, "print", lambda: print), _n_(97405, "random_date", lambda: random_date))
_l_(97407)