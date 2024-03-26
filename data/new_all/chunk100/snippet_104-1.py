# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import datetime
    _l_(100446)

except ImportError:
    pass
now = _c_(100450, _a_(100449, _a_(100448, _n_(100447, "datetime", lambda: datetime), "datetime"), "now"))
_l_(100451)
_c_(100454, _n_(100452, "print", lambda: print), _n_(100453, "now", lambda: now))
_l_(100455)
year = lambda x: _a_(100457, _n_(100456, "x", lambda: x), "year")
_l_(100458)
month = lambda x: _a_(100460, _n_(100459, "x", lambda: x), "month")
_l_(100461)
t = lambda x: _c_(100464, _a_(100463, _n_(100462, "x", lambda: x), "time"))
_l_(100465)
_c_(100470, _n_(100466, "print", lambda: print), _c_(100469, _n_(100467, "year", lambda: year), _n_(100468, "now", lambda: now)))
_l_(100471)
_c_(100476, _n_(100472, "print", lambda: print), _c_(100475, _n_(100473, "month", lambda: month), _n_(100474, "now", lambda: now)))
_l_(100477)
_c_(100482, _n_(100478, "print", lambda: print), _c_(100481, _n_(100479, "day", lambda: day), _n_(100480, "now", lambda: now)))
_l_(100483)
_c_(100488, _n_(100484, "print", lambda: print), _c_(100487, _n_(100485, "t", lambda: t), _n_(100486, "now", lambda: now)))
_l_(100489)