# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(116809)

except ImportError:
    pass
try:
    import re as re
    _l_(116811)

except ImportError:
    pass
_c_(116814, _a_(116813, _n_(116812, "pd", lambda: pd), "set_option"), 'display.max_columns', 10)
_l_(116815)
_c_(116817, _n_(116816, "print", lambda: print), 'Original DataFrame:')
_l_(116818)
_c_(116821, _n_(116819, "print", lambda: print), _n_(116820, "df", lambda: df))
_l_(116822)

def test_num_great(text):
    _l_(116832)

    result = _c_(116826, _a_(116824, _n_(116823, "re", lambda: re), "findall"), '95[5-9]|9[6-9]\\d|[1-9]\\d{3,}', _n_(116825, "text", lambda: text))
    _l_(116827)
    aux = _c_(116830, _a_(116828, ' ', "join"), _n_(116829, "result", lambda: result))
    _l_(116831)
    return aux
_n_(116833, "df", lambda: df)['num_great'] = _c_(116839, _a_(116835, _n_(116834, "df", lambda: df)['address'], "apply"), lambda x: _c_(116838, _n_(116836, "test_num_great", lambda: test_num_great), _n_(116837, "x", lambda: x)))
_l_(116840)
_c_(116842, _n_(116841, "print", lambda: print), '\nNumber greater than 940:')
_l_(116843)
_c_(116846, _n_(116844, "print", lambda: print), _n_(116845, "df", lambda: df))
_l_(116847)