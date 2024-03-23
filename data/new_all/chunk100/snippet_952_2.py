# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from datetime import date
    _l_(95515)

except ImportError:
    pass
l_date = _c_(95517, _n_(95516, "date", lambda: date), 2014, 7, 11)
_l_(95518)
delta = _n_(95519, "l_date", lambda: l_date) - _n_(95520, "f_date", lambda: f_date)
_l_(95521)
_c_(95525, _n_(95522, "print", lambda: print), _a_(95524, _n_(95523, "delta", lambda: delta), "days"))
_l_(95526)