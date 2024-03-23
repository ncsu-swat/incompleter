# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(10754)

except ImportError:
    pass
df = _c_(10757, _a_(10756, _n_(10755, "pd", lambda: pd), "DataFrame"), {'school_code': ['s001', 's002', 's003', 's001', 's002', 's004'], 'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'], 'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'], 'weight': [35, 32, 33, 30, 31, 32]}, index=[1, 2, 3, 4, 5, 6])
_l_(10758)
_c_(10760, _n_(10759, "print", lambda: print), 'Original DataFrame with single index:')
_l_(10761)
_c_(10764, _n_(10762, "print", lambda: print), _n_(10763, "df", lambda: df))
_l_(10765)
idx = 3
_l_(10766)
_c_(10768, _n_(10767, "print", lambda: print), "\nInsert 'date_of_birth' column in 3rd position of the said DataFrame:")
_l_(10769)
_c_(10774, _a_(10771, _n_(10770, "df", lambda: df), "insert"), loc=_n_(10772, "idx", lambda: idx), column='date_of_birth', value=_n_(10773, "date_of_birth", lambda: date_of_birth))
_l_(10775)
_c_(10778, _n_(10776, "print", lambda: print), _n_(10777, "df", lambda: df))
_l_(10779)