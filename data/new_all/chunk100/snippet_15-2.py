# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(102559)

except ImportError:
    pass
df = _c_(102562, _a_(102561, _n_(102560, "pd", lambda: pd), "DataFrame"), {'school_code': ['s001', 's002', 's003', 's001', 's002', 's004'], 'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'], 'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'], 'weight': [35, 32, 33, 30, 31, 32]}, index=[1, 2, 3, 4, 5, 6])
_l_(102563)
_c_(102565, _n_(102564, "print", lambda: print), 'Original DataFrame with single index:')
_l_(102566)
_c_(102569, _n_(102567, "print", lambda: print), _n_(102568, "df", lambda: df))
_l_(102570)
idx = 3
_l_(102571)
_c_(102573, _n_(102572, "print", lambda: print), "\nInsert 'date_of_birth' column in 3rd position of the said DataFrame:")
_l_(102574)
_c_(102579, _a_(102576, _n_(102575, "df", lambda: df), "insert"), loc=_n_(102577, "idx", lambda: idx), column='date_of_birth', value=_n_(102578, "date_of_birth", lambda: date_of_birth))
_l_(102580)
_c_(102583, _n_(102581, "print", lambda: print), _n_(102582, "df", lambda: df))
_l_(102584)