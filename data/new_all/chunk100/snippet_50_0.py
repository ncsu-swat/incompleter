# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(52584)

except ImportError:
    pass
try:
    import re as re
    _l_(52586)

except ImportError:
    pass
df = _c_(52589, _a_(52588, _n_(52587, "pd", lambda: pd), "DataFrame"), {'company_code': ['Abcd', 'EFGF', 'zefsalf', 'sdfslew', 'zekfsdf'], 'date_of_sale': ['12/05/2002', '16/02/1999', '05/09/1998', '12/02/2022', '15/09/1997'], 'address': ['9910 Surrey Ave.', '92 N. Bishop Ave.', '9910 Golden Star Ave.', '102 Dunbar St.', '17 West Livingston Court']})
_l_(52590)
_c_(52592, _n_(52591, "print", lambda: print), 'Original DataFrame:')
_l_(52593)
_c_(52596, _n_(52594, "print", lambda: print), _n_(52595, "df", lambda: df))
_l_(52597)

def search_words(text):
    _l_(52602)

    aux = _c_(52600, _a_(52598, ' ', "join"), _n_(52599, "result", lambda: result))
    _l_(52601)
    return aux
_n_(52603, "df", lambda: df)['only_words'] = _c_(52609, _a_(52605, _n_(52604, "df", lambda: df)['address'], "apply"), lambda x: _c_(52608, _n_(52606, "search_words", lambda: search_words), _n_(52607, "x", lambda: x)))
_l_(52610)
_c_(52612, _n_(52611, "print", lambda: print), '\nOnly words:')
_l_(52613)
_c_(52616, _n_(52614, "print", lambda: print), _n_(52615, "df", lambda: df))
_l_(52617)