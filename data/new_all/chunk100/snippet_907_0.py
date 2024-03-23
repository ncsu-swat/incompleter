# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(91074)

except ImportError:
    pass
try:
    from collections import Counter
    _l_(91076)

except ImportError:
    pass
_c_(91078, _n_(91077, "print", lambda: print), 'Original Series:')
_l_(91079)
_c_(91082, _n_(91080, "print", lambda: print), _n_(91081, "color_series", lambda: color_series))
_l_(91083)
_c_(91085, _n_(91084, "print", lambda: print), '\nFiltered words:')
_l_(91086)
result = mask = _c_(91101, _a_(91088, _n_(91087, "color_series", lambda: color_series), "map"), lambda c: _c_(91100, _n_(91089, "sum", lambda: sum), [_c_(91097, _a_(91095, _c_(91094, _n_(91090, "Counter", lambda: Counter), _c_(91093, _a_(91092, _n_(91091, "c", lambda: c), "lower"))), "get"), _n_(91096, "i", lambda: i), 0) for i in _c_(91099, _n_(91098, "list", lambda: list), 'aeiou')]) >= 2)
_l_(91102)
_c_(91106, _n_(91103, "print", lambda: print), _n_(91104, "color_series", lambda: color_series)[_n_(91105, "result", lambda: result)])
_l_(91107)