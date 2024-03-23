# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(48219)

except ImportError:
    pass
try:
    import re as re
    _l_(48221)

except ImportError:
    pass
_c_(48224, _a_(48223, _n_(48222, "pd", lambda: pd), "set_option"), 'display.max_columns', 10)
_l_(48225)
_c_(48227, _n_(48226, "print", lambda: print), 'Original DataFrame:')
_l_(48228)
_c_(48231, _n_(48229, "print", lambda: print), _n_(48230, "df", lambda: df))
_l_(48232)

def test_num_great(text):
    _l_(48242)

    result = _c_(48236, _a_(48234, _n_(48233, "re", lambda: re), "findall"), '95[5-9]|9[6-9]\\d|[1-9]\\d{3,}', _n_(48235, "text", lambda: text))
    _l_(48237)
    aux = _c_(48240, _a_(48238, ' ', "join"), _n_(48239, "result", lambda: result))
    _l_(48241)
    return aux
_n_(48243, "df", lambda: df)['num_great'] = _c_(48249, _a_(48245, _n_(48244, "df", lambda: df)['address'], "apply"), lambda x: _c_(48248, _n_(48246, "test_num_great", lambda: test_num_great), _n_(48247, "x", lambda: x)))
_l_(48250)
_c_(48252, _n_(48251, "print", lambda: print), '\nNumber greater than 940:')
_l_(48253)
_c_(48256, _n_(48254, "print", lambda: print), _n_(48255, "df", lambda: df))
_l_(48257)