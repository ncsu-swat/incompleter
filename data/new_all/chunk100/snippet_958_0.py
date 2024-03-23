# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(96199)

except ImportError:
    pass
df_data = _c_(96202, _a_(96201, _n_(96200, "pd", lambda: pd), "DataFrame"), {'W': [68, 75, 86, 80, None], 'X': [78, 75, None, 80, 86], 'Y': [84, 94, 89, 86, 86], 'Z': [86, 97, 96, 72, 83]})
_l_(96203)
_c_(96205, _n_(96204, "print", lambda: print), 'Original DataFrame:')
_l_(96206)
_c_(96209, _n_(96207, "print", lambda: print), _n_(96208, "df_data", lambda: df_data))
_l_(96210)
_c_(96212, _n_(96211, "print", lambda: print), '\nOriginal Series:')
_l_(96213)
_c_(96216, _n_(96214, "print", lambda: print), _n_(96215, "sr_data", lambda: sr_data))
_l_(96217)
_c_(96219, _n_(96218, "print", lambda: print), '\nCheck for inequality of the said series & dataframe:')
_l_(96220)
_c_(96226, _n_(96221, "print", lambda: print), _c_(96225, _a_(96223, _n_(96222, "df_data", lambda: df_data), "ne"), _n_(96224, "sr_data", lambda: sr_data), axis=0))
_l_(96227)