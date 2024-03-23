# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(73822)

except ImportError:
    pass
series2 = _c_(73827, _a_(73824, _n_(73823, "pd", lambda: pd), "Series"), _c_(73826, _n_(73825, "list", lambda: list), 'pqrstuvwxy'))
_l_(73828)
_c_(73830, _n_(73829, "print", lambda: print), 'Original Series:')
_l_(73831)
_c_(73834, _n_(73832, "print", lambda: print), _n_(73833, "series1", lambda: series1))
_l_(73835)
_c_(73838, _n_(73836, "print", lambda: print), _n_(73837, "series2", lambda: series2))
_l_(73839)
_c_(73843, _a_(73841, _n_(73840, "series1", lambda: series1), "append"), _n_(73842, "series2", lambda: series2))
_l_(73844)
df = _c_(73849, _a_(73846, _n_(73845, "pd", lambda: pd), "concat"), [_n_(73847, "series1", lambda: series1), _n_(73848, "series2", lambda: series2)], axis=1)
_l_(73850)
_c_(73852, _n_(73851, "print", lambda: print), '\nStack two given series vertically and horizontally:')
_l_(73853)
_c_(73856, _n_(73854, "print", lambda: print), _n_(73855, "df", lambda: df))
_l_(73857)