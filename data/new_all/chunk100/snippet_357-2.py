# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(112022)

except ImportError:
    pass
newday = _c_(112025, _a_(112024, _n_(112023, "pd", lambda: pd), "Timestamp"), '2020-02-07')
_l_(112026)
_c_(112028, _n_(112027, "print", lambda: print), 'First date:')
_l_(112029)
_c_(112032, _n_(112030, "print", lambda: print), _n_(112031, "newday", lambda: newday))
_l_(112033)
_c_(112035, _n_(112034, "print", lambda: print), '\nThe day name of the said date:')
_l_(112036)
_c_(112041, _n_(112037, "print", lambda: print), _c_(112040, _a_(112039, _n_(112038, "newday", lambda: newday), "day_name")))
_l_(112042)
_c_(112044, _n_(112043, "print", lambda: print), '\nAdd 2 days with the said date:')
_l_(112045)
_c_(112050, _n_(112046, "print", lambda: print), _c_(112049, _a_(112048, _n_(112047, "newday1", lambda: newday1), "day_name")))
_l_(112051)
_c_(112053, _n_(112052, "print", lambda: print), '\nNext business day:')
_l_(112054)
nbday = _n_(112055, "newday", lambda: newday) + _c_(112059, _a_(112058, _a_(112057, _n_(112056, "pd", lambda: pd), "offsets"), "BDay"))
_l_(112060)
_c_(112065, _n_(112061, "print", lambda: print), _c_(112064, _a_(112063, _n_(112062, "nbday", lambda: nbday), "day_name")))
_l_(112066)