# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(52619)

except ImportError:
    pass
try:
    import re as re
    _l_(52621)

except ImportError:
    pass
_c_(52623, _n_(52622, "print", lambda: print), 'Original DataFrame:')
_l_(52624)
_c_(52627, _n_(52625, "print", lambda: print), _n_(52626, "df", lambda: df))
_l_(52628)

def search_words(text):
    _l_(52638)

    result = _c_(52632, _a_(52630, _n_(52629, "re", lambda: re), "findall"), '\\b[^\\d\\W]+\\b', _n_(52631, "text", lambda: text))
    _l_(52633)
    aux = _c_(52636, _a_(52634, ' ', "join"), _n_(52635, "result", lambda: result))
    _l_(52637)
    return aux
_n_(52639, "df", lambda: df)['only_words'] = _c_(52645, _a_(52641, _n_(52640, "df", lambda: df)['address'], "apply"), lambda x: _c_(52644, _n_(52642, "search_words", lambda: search_words), _n_(52643, "x", lambda: x)))
_l_(52646)
_c_(52648, _n_(52647, "print", lambda: print), '\nOnly words:')
_l_(52649)
_c_(52652, _n_(52650, "print", lambda: print), _n_(52651, "df", lambda: df))
_l_(52653)