# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(18113)

except ImportError:
    pass
try:
    import re as re
    _l_(18115)

except ImportError:
    pass
_c_(18117, _n_(18116, "print", lambda: print), 'Original DataFrame:')
_l_(18118)
_c_(18121, _n_(18119, "print", lambda: print), _n_(18120, "df", lambda: df))
_l_(18122)

def find_capital_word(str1):
    _l_(18130)

    result = _c_(18126, _a_(18124, _n_(18123, "re", lambda: re), "findall"), '\\b[A-Z]\\w+', _n_(18125, "str1", lambda: str1))
    _l_(18127)
    aux = _n_(18128, "result", lambda: result)
    _l_(18129)
    return aux
_n_(18131, "df", lambda: df)['caps_word_in'] = _c_(18137, _a_(18133, _n_(18132, "df", lambda: df)['address'], "apply"), lambda cw: _c_(18136, _n_(18134, "find_capital_word", lambda: find_capital_word), _n_(18135, "cw", lambda: cw)))
_l_(18138)
_c_(18140, _n_(18139, "print", lambda: print), "\nExtract words starting with capital words from the sentences':")
_l_(18141)
_c_(18144, _n_(18142, "print", lambda: print), _n_(18143, "df", lambda: df))
_l_(18145)