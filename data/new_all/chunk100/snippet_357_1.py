# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(35366)

except ImportError:
    pass
newday = _c_(35369, _a_(35368, _n_(35367, "pd", lambda: pd), "Timestamp"), '2020-02-07')
_l_(35370)
_c_(35372, _n_(35371, "print", lambda: print), 'First date:')
_l_(35373)
_c_(35376, _n_(35374, "print", lambda: print), _n_(35375, "newday", lambda: newday))
_l_(35377)
_c_(35379, _n_(35378, "print", lambda: print), '\nThe day name of the said date:')
_l_(35380)
_c_(35385, _n_(35381, "print", lambda: print), _c_(35384, _a_(35383, _n_(35382, "newday", lambda: newday), "day_name")))
_l_(35386)
_c_(35388, _n_(35387, "print", lambda: print), '\nAdd 2 days with the said date:')
_l_(35389)
_c_(35394, _n_(35390, "print", lambda: print), _c_(35393, _a_(35392, _n_(35391, "newday1", lambda: newday1), "day_name")))
_l_(35395)
_c_(35397, _n_(35396, "print", lambda: print), '\nNext business day:')
_l_(35398)
nbday = _n_(35399, "newday", lambda: newday) + _c_(35403, _a_(35402, _a_(35401, _n_(35400, "pd", lambda: pd), "offsets"), "BDay"))
_l_(35404)
_c_(35409, _n_(35405, "print", lambda: print), _c_(35408, _a_(35407, _n_(35406, "nbday", lambda: nbday), "day_name")))
_l_(35410)