# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(73989)

except ImportError:
    pass
try:
    import re as re
    _l_(73991)

except ImportError:
    pass
_c_(73994, _a_(73993, _n_(73992, "pd", lambda: pd), "set_option"), 'display.max_columns', 10)
_l_(73995)
df = _c_(73998, _a_(73997, _n_(73996, "pd", lambda: pd), "DataFrame"), {'company_code': ['c0001', 'c0002', 'c0003', 'c0003', 'c0004'], 'address': ['7277 Surrey Ave.', '920 N. Bishop Ave.', '9910 Golden Star St.', '25 Dunbar St.', '17 West Livingston Court']})
_l_(73999)
_c_(74001, _n_(74000, "print", lambda: print), 'Original DataFrame:')
_l_(74002)
_c_(74005, _n_(74003, "print", lambda: print), _n_(74004, "df", lambda: df))
_l_(74006)

def find_number(text):
    _l_(74011)

    aux = _c_(74009, _a_(74007, ' ', "join"), _n_(74008, "num", lambda: num))
    _l_(74010)
    return aux
_n_(74012, "df", lambda: df)['number'] = _c_(74018, _a_(74014, _n_(74013, "df", lambda: df)['address'], "apply"), lambda x: _c_(74017, _n_(74015, "find_number", lambda: find_number), _n_(74016, "x", lambda: x)))
_l_(74019)
_c_(74021, _n_(74020, "print", lambda: print), '\\Extracting numbers from dataframe columns:')
_l_(74022)
_c_(74025, _n_(74023, "print", lambda: print), _n_(74024, "df", lambda: df))
_l_(74026)