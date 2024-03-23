# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(48259)

except ImportError:
    pass
try:
    import re as re
    _l_(48261)

except ImportError:
    pass
_c_(48264, _a_(48263, _n_(48262, "pd", lambda: pd), "set_option"), 'display.max_columns', 10)
_l_(48265)
df = _c_(48268, _a_(48267, _n_(48266, "pd", lambda: pd), "DataFrame"), {'company_code': ['c0001', 'c0002', 'c0003', 'c0003', 'c0004'], 'address': ['7277 Surrey Ave.1111', '920 N. Bishop Ave.', '9910 Golden Star St.', '1025 Dunbar St.', '1700 West Livingston Court']})
_l_(48269)
_c_(48271, _n_(48270, "print", lambda: print), 'Original DataFrame:')
_l_(48272)
_c_(48275, _n_(48273, "print", lambda: print), _n_(48274, "df", lambda: df))
_l_(48276)

def test_num_great(text):
    _l_(48281)

    aux = _c_(48279, _a_(48277, ' ', "join"), _n_(48278, "result", lambda: result))
    _l_(48280)
    return aux
_n_(48282, "df", lambda: df)['num_great'] = _c_(48288, _a_(48284, _n_(48283, "df", lambda: df)['address'], "apply"), lambda x: _c_(48287, _n_(48285, "test_num_great", lambda: test_num_great), _n_(48286, "x", lambda: x)))
_l_(48289)
_c_(48291, _n_(48290, "print", lambda: print), '\nNumber greater than 940:')
_l_(48292)
_c_(48295, _n_(48293, "print", lambda: print), _n_(48294, "df", lambda: df))
_l_(48296)