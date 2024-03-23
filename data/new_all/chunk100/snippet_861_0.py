# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(85007)

except ImportError:
    pass
try:
    from dateutil.parser import parse
    _l_(85009)

except ImportError:
    pass
_c_(85011, _n_(85010, "print", lambda: print), 'Original Series:')
_l_(85012)
_c_(85015, _n_(85013, "print", lambda: print), _n_(85014, "date_series", lambda: date_series))
_l_(85016)
_c_(85018, _n_(85017, "print", lambda: print), '\nNew dates:')
_l_(85019)
result = _c_(85025, _a_(85021, _n_(85020, "date_series", lambda: date_series), "map"), lambda d: _c_(85024, _n_(85022, "parse", lambda: parse), '11 ' + _n_(85023, "d", lambda: d)))
_l_(85026)
_c_(85029, _n_(85027, "print", lambda: print), _n_(85028, "result", lambda: result))
_l_(85030)