# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import datetime
    _l_(100579)

except ImportError:
    pass
now = _c_(100583, _a_(100582, _a_(100581, _n_(100580, "datetime", lambda: datetime), "datetime"), "now"))
_l_(100584)
_c_(100587, _n_(100585, "print", lambda: print), _n_(100586, "now", lambda: now))
_l_(100588)
year = lambda x: _a_(100590, _n_(100589, "x", lambda: x), "year")
_l_(100591)
month = lambda x: _a_(100593, _n_(100592, "x", lambda: x), "month")
_l_(100594)
day = lambda x: _a_(100596, _n_(100595, "x", lambda: x), "day")
_l_(100597)
_c_(100602, _n_(100598, "print", lambda: print), _c_(100601, _n_(100599, "year", lambda: year), _n_(100600, "now", lambda: now)))
_l_(100603)
_c_(100608, _n_(100604, "print", lambda: print), _c_(100607, _n_(100605, "month", lambda: month), _n_(100606, "now", lambda: now)))
_l_(100609)
_c_(100614, _n_(100610, "print", lambda: print), _c_(100613, _n_(100611, "day", lambda: day), _n_(100612, "now", lambda: now)))
_l_(100615)
_c_(100620, _n_(100616, "print", lambda: print), _c_(100619, _n_(100617, "t", lambda: t), _n_(100618, "now", lambda: now)))
_l_(100621)