# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(18147)

except ImportError:
    pass
try:
    import re as re
    _l_(18149)

except ImportError:
    pass
df = _c_(18152, _a_(18151, _n_(18150, "pd", lambda: pd), "DataFrame"), {'company_code': ['Abcd', 'EFGF', 'zefsalf', 'sdfslew', 'zekfsdf'], 'date_of_sale': ['12/05/2002', '16/02/1999', '05/09/1998', '12/02/2022', '15/09/1997'], 'address': ['9910 Surrey Avenue', '92 N. Bishop Avenue', '9910 Golden Star Avenue', '102 Dunbar St.', '17 West Livingston Court']})
_l_(18153)
_c_(18155, _n_(18154, "print", lambda: print), 'Original DataFrame:')
_l_(18156)
_c_(18159, _n_(18157, "print", lambda: print), _n_(18158, "df", lambda: df))
_l_(18160)

def find_capital_word(str1):
    _l_(18163)

    aux = _n_(18161, "result", lambda: result)
    _l_(18162)
    return aux
_n_(18164, "df", lambda: df)['caps_word_in'] = _c_(18170, _a_(18166, _n_(18165, "df", lambda: df)['address'], "apply"), lambda cw: _c_(18169, _n_(18167, "find_capital_word", lambda: find_capital_word), _n_(18168, "cw", lambda: cw)))
_l_(18171)
_c_(18173, _n_(18172, "print", lambda: print), "\nExtract words starting with capital words from the sentences':")
_l_(18174)
_c_(18177, _n_(18175, "print", lambda: print), _n_(18176, "df", lambda: df))
_l_(18178)