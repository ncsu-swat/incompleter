# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(75850)

except ImportError:
    pass
try:
    import re as re
    _l_(75852)

except ImportError:
    pass
df = _c_(75855, _a_(75854, _n_(75853, "pd", lambda: pd), "DataFrame"), {'company_code': ['Abcd', 'EFGF', 'zefsalf', 'sdfslew', 'zekfsdf'], 'date_of_sale': ['12/05/2002', '16/02/1999', '05/09/1998', '12/02/2022', '15/09/1997'], 'sale_amount': [12348.5, 233331.2, 22.5, 2566552.0, 23.0]})
_l_(75856)
_c_(75858, _n_(75857, "print", lambda: print), 'Original DataFrame:')
_l_(75859)
_c_(75862, _n_(75860, "print", lambda: print), _n_(75861, "df", lambda: df))
_l_(75863)

def find_valid_dates(dt):
    _l_(75866)

    aux = _n_(75864, "result", lambda: result)
    _l_(75865)
    return aux
_n_(75867, "df", lambda: df)['valid_dates'] = _c_(75873, _a_(75869, _n_(75868, "df", lambda: df)['date_of_sale'], "apply"), lambda dt: _c_(75872, _n_(75870, "find_valid_dates", lambda: find_valid_dates), _n_(75871, "dt", lambda: dt)))
_l_(75874)
_c_(75876, _n_(75875, "print", lambda: print), '\nValid dates (format: mm-dd-yyyy):')
_l_(75877)
_c_(75880, _n_(75878, "print", lambda: print), _n_(75879, "df", lambda: df))
_l_(75881)