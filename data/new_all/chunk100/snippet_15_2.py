# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(10781)

except ImportError:
    pass
_c_(10783, _n_(10782, "print", lambda: print), 'Original DataFrame with single index:')
_l_(10784)
_c_(10787, _n_(10785, "print", lambda: print), _n_(10786, "df", lambda: df))
_l_(10788)
date_of_birth = ['15/05/2002', '17/05/2002', '16/02/1999', '25/09/1998', '11/05/2002', '15/09/1997']
_l_(10789)
idx = 3
_l_(10790)
_c_(10792, _n_(10791, "print", lambda: print), "\nInsert 'date_of_birth' column in 3rd position of the said DataFrame:")
_l_(10793)
_c_(10798, _a_(10795, _n_(10794, "df", lambda: df), "insert"), loc=_n_(10796, "idx", lambda: idx), column='date_of_birth', value=_n_(10797, "date_of_birth", lambda: date_of_birth))
_l_(10799)
_c_(10802, _n_(10800, "print", lambda: print), _n_(10801, "df", lambda: df))
_l_(10803)