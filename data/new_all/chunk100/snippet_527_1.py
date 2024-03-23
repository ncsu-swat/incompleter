# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(53391)

except ImportError:
    pass
series1 = _c_(53394, _a_(53393, _n_(53392, "pd", lambda: pd), "Series"), ['php', 'python', 'java', 'c#'])
_l_(53395)
_c_(53397, _n_(53396, "print", lambda: print), 'Original Series:')
_l_(53398)
_c_(53401, _n_(53399, "print", lambda: print), _n_(53400, "series1", lambda: series1))
_l_(53402)
_c_(53404, _n_(53403, "print", lambda: print), '\nFirst and last character of each word to upper case:')
_l_(53405)
_c_(53408, _n_(53406, "print", lambda: print), _n_(53407, "result", lambda: result))
_l_(53409)