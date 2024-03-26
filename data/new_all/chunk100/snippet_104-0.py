# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import datetime
    _l_(100401)

except ImportError:
    pass
now = _c_(100405, _a_(100404, _a_(100403, _n_(100402, "datetime", lambda: datetime), "datetime"), "now"))
_l_(100406)
_c_(100409, _n_(100407, "print", lambda: print), _n_(100408, "now", lambda: now))
_l_(100410)
month = lambda x: _a_(100412, _n_(100411, "x", lambda: x), "month")
_l_(100413)
day = lambda x: _a_(100415, _n_(100414, "x", lambda: x), "day")
_l_(100416)
t = lambda x: _c_(100419, _a_(100418, _n_(100417, "x", lambda: x), "time"))
_l_(100420)
_c_(100425, _n_(100421, "print", lambda: print), _c_(100424, _n_(100422, "year", lambda: year), _n_(100423, "now", lambda: now)))
_l_(100426)
_c_(100431, _n_(100427, "print", lambda: print), _c_(100430, _n_(100428, "month", lambda: month), _n_(100429, "now", lambda: now)))
_l_(100432)
_c_(100437, _n_(100433, "print", lambda: print), _c_(100436, _n_(100434, "day", lambda: day), _n_(100435, "now", lambda: now)))
_l_(100438)
_c_(100443, _n_(100439, "print", lambda: print), _c_(100442, _n_(100440, "t", lambda: t), _n_(100441, "now", lambda: now)))
_l_(100444)