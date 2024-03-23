# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(97789)

except ImportError:
    pass
try:
    import re as re
    _l_(97791)

except ImportError:
    pass
_c_(97794, _a_(97793, _n_(97792, "pd", lambda: pd), "set_option"), 'display.max_columns', 10)
_l_(97795)
_c_(97797, _n_(97796, "print", lambda: print), 'Original DataFrame:')
_l_(97798)
_c_(97801, _n_(97799, "print", lambda: print), _n_(97800, "df", lambda: df))
_l_(97802)

def find_phone_number(text):
    _l_(97812)

    ph_no = _c_(97806, _a_(97804, _n_(97803, "re", lambda: re), "findall"), '\\b\\d{10}\\b', _n_(97805, "text", lambda: text))
    _l_(97807)
    aux = _c_(97810, _a_(97808, '', "join"), _n_(97809, "ph_no", lambda: ph_no))
    _l_(97811)
    return aux
_n_(97813, "df", lambda: df)['number'] = _c_(97819, _a_(97815, _n_(97814, "df", lambda: df)['company_phone_no'], "apply"), lambda x: _c_(97818, _n_(97816, "find_phone_number", lambda: find_phone_number), _n_(97817, "x", lambda: x)))
_l_(97820)
_c_(97822, _n_(97821, "print", lambda: print), '\\Extracting numbers from dataframe columns:')
_l_(97823)
_c_(97826, _n_(97824, "print", lambda: print), _n_(97825, "df", lambda: df))
_l_(97827)