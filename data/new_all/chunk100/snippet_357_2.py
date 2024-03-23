# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(35412)

except ImportError:
    pass
newday = _c_(35415, _a_(35414, _n_(35413, "pd", lambda: pd), "Timestamp"), '2020-02-07')
_l_(35416)
_c_(35418, _n_(35417, "print", lambda: print), 'First date:')
_l_(35419)
_c_(35422, _n_(35420, "print", lambda: print), _n_(35421, "newday", lambda: newday))
_l_(35423)
_c_(35425, _n_(35424, "print", lambda: print), '\nThe day name of the said date:')
_l_(35426)
_c_(35431, _n_(35427, "print", lambda: print), _c_(35430, _a_(35429, _n_(35428, "newday", lambda: newday), "day_name")))
_l_(35432)
_c_(35434, _n_(35433, "print", lambda: print), '\nAdd 2 days with the said date:')
_l_(35435)
newday1 = _n_(35436, "newday", lambda: newday) + _c_(35439, _a_(35438, _n_(35437, "pd", lambda: pd), "Timedelta"), '2 day')
_l_(35440)
_c_(35445, _n_(35441, "print", lambda: print), _c_(35444, _a_(35443, _n_(35442, "newday1", lambda: newday1), "day_name")))
_l_(35446)
_c_(35448, _n_(35447, "print", lambda: print), '\nNext business day:')
_l_(35449)
_c_(35454, _n_(35450, "print", lambda: print), _c_(35453, _a_(35452, _n_(35451, "nbday", lambda: nbday), "day_name")))
_l_(35455)