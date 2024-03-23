# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(68775)

except ImportError:
    pass
_c_(68777, _n_(68776, "print", lambda: print), 'Original DataFrame:')
_l_(68778)
_c_(68781, _n_(68779, "print", lambda: print), _n_(68780, "df", lambda: df))
_l_(68782)
_c_(68784, _n_(68783, "print", lambda: print), '\nConvert index of the said dataframe into a column:')
_l_(68785)
_c_(68788, _a_(68787, _n_(68786, "df", lambda: df), "reset_index"), level=0, inplace=True)
_l_(68789)
_c_(68792, _n_(68790, "print", lambda: print), _n_(68791, "df", lambda: df))
_l_(68793)