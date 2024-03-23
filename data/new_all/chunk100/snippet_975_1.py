# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(97829)

except ImportError:
    pass
try:
    import re as re
    _l_(97831)

except ImportError:
    pass
_c_(97834, _a_(97833, _n_(97832, "pd", lambda: pd), "set_option"), 'display.max_columns', 10)
_l_(97835)
df = _c_(97838, _a_(97837, _n_(97836, "pd", lambda: pd), "DataFrame"), {'company_code': ['c0001', 'c0002', 'c0003', 'c0003', 'c0004'], 'company_phone_no': ['Company1-Phone no. 4695168357', 'Company2-Phone no. 8088729013', 'Company3-Phone no. 6204658086', 'Company4-Phone no. 5159530096', 'Company5-Phone no. 9037952371']})
_l_(97839)
_c_(97841, _n_(97840, "print", lambda: print), 'Original DataFrame:')
_l_(97842)
_c_(97845, _n_(97843, "print", lambda: print), _n_(97844, "df", lambda: df))
_l_(97846)

def find_phone_number(text):
    _l_(97851)

    aux = _c_(97849, _a_(97847, '', "join"), _n_(97848, "ph_no", lambda: ph_no))
    _l_(97850)
    return aux
_n_(97852, "df", lambda: df)['number'] = _c_(97858, _a_(97854, _n_(97853, "df", lambda: df)['company_phone_no'], "apply"), lambda x: _c_(97857, _n_(97855, "find_phone_number", lambda: find_phone_number), _n_(97856, "x", lambda: x)))
_l_(97859)
_c_(97861, _n_(97860, "print", lambda: print), '\\Extracting numbers from dataframe columns:')
_l_(97862)
_c_(97865, _n_(97863, "print", lambda: print), _n_(97864, "df", lambda: df))
_l_(97866)