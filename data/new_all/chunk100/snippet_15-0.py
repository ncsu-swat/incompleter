# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(102508)

except ImportError:
    pass
_c_(102510, _n_(102509, "print", lambda: print), 'Original DataFrame with single index:')
_l_(102511)
_c_(102514, _n_(102512, "print", lambda: print), _n_(102513, "df", lambda: df))
_l_(102515)
date_of_birth = ['15/05/2002', '17/05/2002', '16/02/1999', '25/09/1998', '11/05/2002', '15/09/1997']
_l_(102516)
idx = 3
_l_(102517)
_c_(102519, _n_(102518, "print", lambda: print), "\nInsert 'date_of_birth' column in 3rd position of the said DataFrame:")
_l_(102520)
_c_(102525, _a_(102522, _n_(102521, "df", lambda: df), "insert"), loc=_n_(102523, "idx", lambda: idx), column='date_of_birth', value=_n_(102524, "date_of_birth", lambda: date_of_birth))
_l_(102526)
_c_(102529, _n_(102527, "print", lambda: print), _n_(102528, "df", lambda: df))
_l_(102530)