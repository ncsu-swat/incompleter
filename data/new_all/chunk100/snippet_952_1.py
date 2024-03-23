# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from datetime import date
    _l_(95502)

except ImportError:
    pass
f_date = _c_(95504, _n_(95503, "date", lambda: date), 2014, 7, 2)
_l_(95505)
delta = _n_(95506, "l_date", lambda: l_date) - _n_(95507, "f_date", lambda: f_date)
_l_(95508)
_c_(95512, _n_(95509, "print", lambda: print), _a_(95511, _n_(95510, "delta", lambda: delta), "days"))
_l_(95513)