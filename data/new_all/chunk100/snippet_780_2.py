# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(78843)

except ImportError:
    pass
try:
    import re as re
    _l_(78845)

except ImportError:
    pass
_c_(78848, _a_(78847, _n_(78846, "pd", lambda: pd), "set_option"), 'display.max_columns', 10)
_l_(78849)
df = _c_(78852, _a_(78851, _n_(78850, "pd", lambda: pd), "DataFrame"), {'company_code': ['c0001.', 'c000,2', 'c0003', 'c0003#', 'c0004,'], 'year': ['year 1800', 'year 1700', 'year 2300', 'year 1900', 'year 2200']})
_l_(78853)
_c_(78855, _n_(78854, "print", lambda: print), 'Original DataFrame:')
_l_(78856)
_c_(78859, _n_(78857, "print", lambda: print), _n_(78858, "df", lambda: df))
_l_(78860)

def find_punctuations(text):
    _l_(78869)

    string = _c_(78863, _a_(78861, '', "join"), _n_(78862, "result", lambda: result))
    _l_(78864)
    aux = _c_(78867, _n_(78865, "list", lambda: list), _n_(78866, "string", lambda: string))
    _l_(78868)
    return aux
_n_(78870, "df", lambda: df)['nonalpha'] = _c_(78876, _a_(78872, _n_(78871, "df", lambda: df)['company_code'], "apply"), lambda x: _c_(78875, _n_(78873, "find_punctuations", lambda: find_punctuations), _n_(78874, "x", lambda: x)))
_l_(78877)
_c_(78879, _n_(78878, "print", lambda: print), '\nExtracting punctuation:')
_l_(78880)
_c_(78883, _n_(78881, "print", lambda: print), _n_(78882, "df", lambda: df))
_l_(78884)