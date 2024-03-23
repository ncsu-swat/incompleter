# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(17562)

except ImportError:
    pass
_c_(17564, _n_(17563, "print", lambda: print), 'Original DataFrame:')
_l_(17565)
_c_(17568, _n_(17566, "print", lambda: print), _n_(17567, "df", lambda: df))
_l_(17569)
_c_(17571, _n_(17570, "print", lambda: print), "\nCreate MultiIndex on 'tcode' and 'school_code':")
_l_(17572)
df = _c_(17575, _a_(17574, _n_(17573, "df", lambda: df), "set_index"), ['tcode', 'school_code'])
_l_(17576)
_c_(17579, _n_(17577, "print", lambda: print), _n_(17578, "df", lambda: df))
_l_(17580)
_c_(17582, _n_(17581, "print", lambda: print), "\nSelect rows(s) from 'tcode' column:")
_l_(17583)
_c_(17588, _n_(17584, "print", lambda: print), _c_(17587, _a_(17586, _n_(17585, "df", lambda: df), "query"), "tcode == 't2'"))
_l_(17589)
_c_(17591, _n_(17590, "print", lambda: print), "\nSelect rows(s) from 'school_code' column:")
_l_(17592)
_c_(17597, _n_(17593, "print", lambda: print), _c_(17596, _a_(17595, _n_(17594, "df", lambda: df), "query"), "school_code == 's001'"))
_l_(17598)
_c_(17600, _n_(17599, "print", lambda: print), "\nSelect rows(s) from 'tcode' and 'scode' columns:")
_l_(17601)
_c_(17606, _n_(17602, "print", lambda: print), _c_(17605, _a_(17604, _n_(17603, "df", lambda: df), "query"), "tcode == 't1'" and "school_code == 's001'"))
_l_(17607)