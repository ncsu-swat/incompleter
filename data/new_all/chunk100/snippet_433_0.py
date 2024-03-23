# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(44069)

except ImportError:
    pass
try:
    import re as re
    _l_(44071)

except ImportError:
    pass
_c_(44074, _a_(44073, _n_(44072, "pd", lambda: pd), "set_option"), 'display.max_columns', 10)
_l_(44075)
_c_(44077, _n_(44076, "print", lambda: print), 'Original DataFrame:')
_l_(44078)
_c_(44081, _n_(44079, "print", lambda: print), _n_(44080, "df", lambda: df))
_l_(44082)

def test_and_cond(text):
    _l_(44092)

    result = _c_(44086, _a_(44084, _n_(44083, "re", lambda: re), "findall"), '(?=.*Ave.)(?=.*9910).*', _n_(44085, "text", lambda: text))
    _l_(44087)
    aux = _c_(44090, _a_(44088, ' ', "join"), _n_(44089, "result", lambda: result))
    _l_(44091)
    return aux
_n_(44093, "df", lambda: df)['check_two_words'] = _c_(44099, _a_(44095, _n_(44094, "df", lambda: df)['address'], "apply"), lambda x: _c_(44098, _n_(44096, "test_and_cond", lambda: test_and_cond), _n_(44097, "x", lambda: x)))
_l_(44100)
_c_(44102, _n_(44101, "print", lambda: print), '\nPresent two words!')
_l_(44103)
_c_(44106, _n_(44104, "print", lambda: print), _n_(44105, "df", lambda: df))
_l_(44107)