# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(105937)

except ImportError:
    pass
try:
    import re as re
    _l_(105939)

except ImportError:
    pass
_c_(105941, _n_(105940, "print", lambda: print), 'Original DataFrame:')
_l_(105942)
_c_(105945, _n_(105943, "print", lambda: print), _n_(105944, "df", lambda: df))
_l_(105946)

def find_capital_word(str1):
    _l_(105954)

    result = _c_(105950, _a_(105948, _n_(105947, "re", lambda: re), "findall"), '\\b[A-Z]\\w+', _n_(105949, "str1", lambda: str1))
    _l_(105951)
    aux = _n_(105952, "result", lambda: result)
    _l_(105953)
    return aux
_n_(105955, "df", lambda: df)['caps_word_in'] = _c_(105961, _a_(105957, _n_(105956, "df", lambda: df)['address'], "apply"), lambda cw: _c_(105960, _n_(105958, "find_capital_word", lambda: find_capital_word), _n_(105959, "cw", lambda: cw)))
_l_(105962)
_c_(105964, _n_(105963, "print", lambda: print), "\nExtract words starting with capital words from the sentences':")
_l_(105965)
_c_(105968, _n_(105966, "print", lambda: print), _n_(105967, "df", lambda: df))
_l_(105969)