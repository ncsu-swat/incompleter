# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(10727)

except ImportError:
    pass
df = _c_(10730, _a_(10729, _n_(10728, "pd", lambda: pd), "DataFrame"), {'school_code': ['s001', 's002', 's003', 's001', 's002', 's004'], 'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'], 'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'], 'weight': [35, 32, 33, 30, 31, 32]}, index=[1, 2, 3, 4, 5, 6])
_l_(10731)
_c_(10733, _n_(10732, "print", lambda: print), 'Original DataFrame with single index:')
_l_(10734)
_c_(10737, _n_(10735, "print", lambda: print), _n_(10736, "df", lambda: df))
_l_(10738)
date_of_birth = ['15/05/2002', '17/05/2002', '16/02/1999', '25/09/1998', '11/05/2002', '15/09/1997']
_l_(10739)
_c_(10741, _n_(10740, "print", lambda: print), "\nInsert 'date_of_birth' column in 3rd position of the said DataFrame:")
_l_(10742)
_c_(10747, _a_(10744, _n_(10743, "df", lambda: df), "insert"), loc=_n_(10745, "idx", lambda: idx), column='date_of_birth', value=_n_(10746, "date_of_birth", lambda: date_of_birth))
_l_(10748)
_c_(10751, _n_(10749, "print", lambda: print), _n_(10750, "df", lambda: df))
_l_(10752)