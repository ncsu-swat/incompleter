# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(78799)

except ImportError:
    pass
try:
    import re as re
    _l_(78801)

except ImportError:
    pass
_c_(78804, _a_(78803, _n_(78802, "pd", lambda: pd), "set_option"), 'display.max_columns', 10)
_l_(78805)
df = _c_(78808, _a_(78807, _n_(78806, "pd", lambda: pd), "DataFrame"), {'company_code': ['c0001.', 'c000,2', 'c0003', 'c0003#', 'c0004,'], 'year': ['year 1800', 'year 1700', 'year 2300', 'year 1900', 'year 2200']})
_l_(78809)
_c_(78811, _n_(78810, "print", lambda: print), 'Original DataFrame:')
_l_(78812)
_c_(78815, _n_(78813, "print", lambda: print), _n_(78814, "df", lambda: df))
_l_(78816)

def find_punctuations(text):
    _l_(78826)

    result = _c_(78820, _a_(78818, _n_(78817, "re", lambda: re), "findall"), '[!"\\$%&\\\'()*+,\\-.\\/:;=#@?\\[\\\\\\]^_`{|}~]*', _n_(78819, "text", lambda: text))
    _l_(78821)
    aux = _c_(78824, _n_(78822, "list", lambda: list), _n_(78823, "string", lambda: string))
    _l_(78825)
    return aux
_n_(78827, "df", lambda: df)['nonalpha'] = _c_(78833, _a_(78829, _n_(78828, "df", lambda: df)['company_code'], "apply"), lambda x: _c_(78832, _n_(78830, "find_punctuations", lambda: find_punctuations), _n_(78831, "x", lambda: x)))
_l_(78834)
_c_(78836, _n_(78835, "print", lambda: print), '\nExtracting punctuation:')
_l_(78837)
_c_(78840, _n_(78838, "print", lambda: print), _n_(78839, "df", lambda: df))
_l_(78841)