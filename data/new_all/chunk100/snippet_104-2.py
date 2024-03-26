# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import datetime
    _l_(100491)

except ImportError:
    pass
now = _c_(100495, _a_(100494, _a_(100493, _n_(100492, "datetime", lambda: datetime), "datetime"), "now"))
_l_(100496)
_c_(100499, _n_(100497, "print", lambda: print), _n_(100498, "now", lambda: now))
_l_(100500)
year = lambda x: _a_(100502, _n_(100501, "x", lambda: x), "year")
_l_(100503)
day = lambda x: _a_(100505, _n_(100504, "x", lambda: x), "day")
_l_(100506)
t = lambda x: _c_(100509, _a_(100508, _n_(100507, "x", lambda: x), "time"))
_l_(100510)
_c_(100515, _n_(100511, "print", lambda: print), _c_(100514, _n_(100512, "year", lambda: year), _n_(100513, "now", lambda: now)))
_l_(100516)
_c_(100521, _n_(100517, "print", lambda: print), _c_(100520, _n_(100518, "month", lambda: month), _n_(100519, "now", lambda: now)))
_l_(100522)
_c_(100527, _n_(100523, "print", lambda: print), _c_(100526, _n_(100524, "day", lambda: day), _n_(100525, "now", lambda: now)))
_l_(100528)
_c_(100533, _n_(100529, "print", lambda: print), _c_(100532, _n_(100530, "t", lambda: t), _n_(100531, "now", lambda: now)))
_l_(100534)