# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(73859)

except ImportError:
    pass
series1 = _c_(73864, _a_(73861, _n_(73860, "pd", lambda: pd), "Series"), _c_(73863, _n_(73862, "range", lambda: range), 10))
_l_(73865)
_c_(73867, _n_(73866, "print", lambda: print), 'Original Series:')
_l_(73868)
_c_(73871, _n_(73869, "print", lambda: print), _n_(73870, "series1", lambda: series1))
_l_(73872)
_c_(73875, _n_(73873, "print", lambda: print), _n_(73874, "series2", lambda: series2))
_l_(73876)
_c_(73880, _a_(73878, _n_(73877, "series1", lambda: series1), "append"), _n_(73879, "series2", lambda: series2))
_l_(73881)
df = _c_(73886, _a_(73883, _n_(73882, "pd", lambda: pd), "concat"), [_n_(73884, "series1", lambda: series1), _n_(73885, "series2", lambda: series2)], axis=1)
_l_(73887)
_c_(73889, _n_(73888, "print", lambda: print), '\nStack two given series vertically and horizontally:')
_l_(73890)
_c_(73893, _n_(73891, "print", lambda: print), _n_(73892, "df", lambda: df))
_l_(73894)