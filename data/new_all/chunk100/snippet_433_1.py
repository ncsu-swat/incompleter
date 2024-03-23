# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(44109)

except ImportError:
    pass
try:
    import re as re
    _l_(44111)

except ImportError:
    pass
_c_(44114, _a_(44113, _n_(44112, "pd", lambda: pd), "set_option"), 'display.max_columns', 10)
_l_(44115)
df = _c_(44118, _a_(44117, _n_(44116, "pd", lambda: pd), "DataFrame"), {'company_code': ['c0001', 'c0002', 'c0003', 'c0003', 'c0004'], 'address': ['9910 Surrey Ave.', '92 N. Bishop Ave.', '9910 Golden Star Ave.', '102 Dunbar St.', '17 West Livingston Court']})
_l_(44119)
_c_(44121, _n_(44120, "print", lambda: print), 'Original DataFrame:')
_l_(44122)
_c_(44125, _n_(44123, "print", lambda: print), _n_(44124, "df", lambda: df))
_l_(44126)

def test_and_cond(text):
    _l_(44131)

    aux = _c_(44129, _a_(44127, ' ', "join"), _n_(44128, "result", lambda: result))
    _l_(44130)
    return aux
_n_(44132, "df", lambda: df)['check_two_words'] = _c_(44138, _a_(44134, _n_(44133, "df", lambda: df)['address'], "apply"), lambda x: _c_(44137, _n_(44135, "test_and_cond", lambda: test_and_cond), _n_(44136, "x", lambda: x)))
_l_(44139)
_c_(44141, _n_(44140, "print", lambda: print), '\nPresent two words!')
_l_(44142)
_c_(44145, _n_(44143, "print", lambda: print), _n_(44144, "df", lambda: df))
_l_(44146)