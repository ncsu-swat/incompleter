# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(49577)

except ImportError:
    pass
_c_(49579, _n_(49578, "print", lambda: print), 'Original DataFrame:')
_l_(49580)
_c_(49583, _n_(49581, "print", lambda: print), _n_(49582, "df", lambda: df))
_l_(49584)
_c_(49586, _n_(49585, "print", lambda: print), "\nMultiIndex using columns 't_id', ‘school_code’ and 'class':")
_l_(49587)
df1 = _c_(49590, _a_(49589, _n_(49588, "df", lambda: df), "set_index"), ['t_id', 'school_code', 'class'])
_l_(49591)
_c_(49594, _n_(49592, "print", lambda: print), _n_(49593, "df1", lambda: df1))
_l_(49595)
_c_(49597, _n_(49596, "print", lambda: print), '\nConvert 1st and 3rd levels in the index frame into columns:')
_l_(49598)
df2 = _c_(49601, _a_(49600, _n_(49599, "df1", lambda: df1), "reset_index"), level=['t_id', 'class'])
_l_(49602)
_c_(49605, _n_(49603, "print", lambda: print), _n_(49604, "df2", lambda: df2))
_l_(49606)