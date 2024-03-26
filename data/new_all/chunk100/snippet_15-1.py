# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(102532)

except ImportError:
    pass
df = _c_(102535, _a_(102534, _n_(102533, "pd", lambda: pd), "DataFrame"), {'school_code': ['s001', 's002', 's003', 's001', 's002', 's004'], 'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'], 'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'], 'weight': [35, 32, 33, 30, 31, 32]}, index=[1, 2, 3, 4, 5, 6])
_l_(102536)
_c_(102538, _n_(102537, "print", lambda: print), 'Original DataFrame with single index:')
_l_(102539)
_c_(102542, _n_(102540, "print", lambda: print), _n_(102541, "df", lambda: df))
_l_(102543)
date_of_birth = ['15/05/2002', '17/05/2002', '16/02/1999', '25/09/1998', '11/05/2002', '15/09/1997']
_l_(102544)
_c_(102546, _n_(102545, "print", lambda: print), "\nInsert 'date_of_birth' column in 3rd position of the said DataFrame:")
_l_(102547)
_c_(102552, _a_(102549, _n_(102548, "df", lambda: df), "insert"), loc=_n_(102550, "idx", lambda: idx), column='date_of_birth', value=_n_(102551, "date_of_birth", lambda: date_of_birth))
_l_(102553)
_c_(102556, _n_(102554, "print", lambda: print), _n_(102555, "df", lambda: df))
_l_(102557)