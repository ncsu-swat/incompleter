# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import datetime
    _l_(5059)

except ImportError:
    pass
now = _c_(5063, _a_(5062, _a_(5061, _n_(5060, "datetime", lambda: datetime), "datetime"), "now"))
_l_(5064)
_c_(5067, _n_(5065, "print", lambda: print), _n_(5066, "now", lambda: now))
_l_(5068)
month = lambda x: _a_(5070, _n_(5069, "x", lambda: x), "month")
_l_(5071)
day = lambda x: _a_(5073, _n_(5072, "x", lambda: x), "day")
_l_(5074)
t = lambda x: _c_(5077, _a_(5076, _n_(5075, "x", lambda: x), "time"))
_l_(5078)
_c_(5083, _n_(5079, "print", lambda: print), _c_(5082, _n_(5080, "year", lambda: year), _n_(5081, "now", lambda: now)))
_l_(5084)
_c_(5089, _n_(5085, "print", lambda: print), _c_(5088, _n_(5086, "month", lambda: month), _n_(5087, "now", lambda: now)))
_l_(5090)
_c_(5095, _n_(5091, "print", lambda: print), _c_(5094, _n_(5092, "day", lambda: day), _n_(5093, "now", lambda: now)))
_l_(5096)
_c_(5101, _n_(5097, "print", lambda: print), _c_(5100, _n_(5098, "t", lambda: t), _n_(5099, "now", lambda: now)))
_l_(5102)