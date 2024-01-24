# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68002673/how-to-resolve-an-attributeerror-can-only-use-str-accessor-with-string-values
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(608592)

except ImportError:
    pass
try:
    import numpy as np
    _l_(608594)

except ImportError:
    pass
try:
    from pandas import DataFrame as df
    _l_(608596)

except ImportError:
    pass
try:
    import re
    _l_(608598)

except ImportError:
    pass


data = {'Tim': 'Tim@google.com', 'Rob': 'Rob@gmail.com', 'Jen': 'Jen@gmail.com', 'Wes': _a_(608600, _n_(608599, "np", lambda: np), "nan")}
_l_(608601)

data = _c_(608605, _a_(608603, _n_(608602, "pd", lambda: pd), "Series"), _n_(608604, "data", lambda: data))
_l_(608606)
    
pattern = r'([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\.([A-Z]{2,4})'
_l_(608607)

matches = _c_(608614, _a_(608610, _a_(608609, _n_(608608, "data", lambda: data), "str"), "match"), _n_(608611, "pattern", lambda: pattern), flags=_a_(608613, _n_(608612, "re", lambda: re), "IGNORECASE"))
_l_(608615)

_c_(608619, _a_(608618, _a_(608617, _n_(608616, "matches", lambda: matches), "str"), "get"), 1)
_l_(608620)