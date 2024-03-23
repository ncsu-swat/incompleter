# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(8981)

except ImportError:
    pass
try:
    import re as re
    _l_(8983)

except ImportError:
    pass
df = _c_(8986, _a_(8985, _n_(8984, "pd", lambda: pd), "DataFrame"), {'company_code': ['Abcd', 'EFGF', 'zefsalf', 'sdfslew', 'zekfsdf'], 'date_of_sale': ['12/05/2002', '16/02/1999', '05/09/1998', '12/02/2022', '15/09/1997'], 'address': ['9910 Surrey Avenue\n9910 Surrey Avenue', '92 N. Bishop Avenue', '9910 Golden Star Avenue', '102 Dunbar St.\n102 Dunbar St.', '17 West Livingston Court']})
_l_(8987)
_c_(8989, _n_(8988, "print", lambda: print), 'Original DataFrame:')
_l_(8990)
_c_(8993, _n_(8991, "print", lambda: print), _n_(8992, "df", lambda: df))
_l_(8994)

def find_unique_sentence(str1):
    _l_(8997)

    aux = _n_(8995, "result", lambda: result)
    _l_(8996)
    return aux
_n_(8998, "df", lambda: df)['unique_sentence'] = _c_(9004, _a_(9000, _n_(8999, "df", lambda: df)['address'], "apply"), lambda st: _c_(9003, _n_(9001, "find_unique_sentence", lambda: find_unique_sentence), _n_(9002, "st", lambda: st)))
_l_(9005)
_c_(9007, _n_(9006, "print", lambda: print), '\nExtract unique sentences :')
_l_(9008)
_c_(9011, _n_(9009, "print", lambda: print), _n_(9010, "df", lambda: df))
_l_(9012)