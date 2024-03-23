# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import datetime
    _l_(5014)

except ImportError:
    pass
now = _c_(5018, _a_(5017, _a_(5016, _n_(5015, "datetime", lambda: datetime), "datetime"), "now"))
_l_(5019)
_c_(5022, _n_(5020, "print", lambda: print), _n_(5021, "now", lambda: now))
_l_(5023)
year = lambda x: _a_(5025, _n_(5024, "x", lambda: x), "year")
_l_(5026)
month = lambda x: _a_(5028, _n_(5027, "x", lambda: x), "month")
_l_(5029)
t = lambda x: _c_(5032, _a_(5031, _n_(5030, "x", lambda: x), "time"))
_l_(5033)
_c_(5038, _n_(5034, "print", lambda: print), _c_(5037, _n_(5035, "year", lambda: year), _n_(5036, "now", lambda: now)))
_l_(5039)
_c_(5044, _n_(5040, "print", lambda: print), _c_(5043, _n_(5041, "month", lambda: month), _n_(5042, "now", lambda: now)))
_l_(5045)
_c_(5050, _n_(5046, "print", lambda: print), _c_(5049, _n_(5047, "day", lambda: day), _n_(5048, "now", lambda: now)))
_l_(5051)
_c_(5056, _n_(5052, "print", lambda: print), _c_(5055, _n_(5053, "t", lambda: t), _n_(5054, "now", lambda: now)))
_l_(5057)