# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(73949)

except ImportError:
    pass
try:
    import re as re
    _l_(73951)

except ImportError:
    pass
_c_(73954, _a_(73953, _n_(73952, "pd", lambda: pd), "set_option"), 'display.max_columns', 10)
_l_(73955)
_c_(73957, _n_(73956, "print", lambda: print), 'Original DataFrame:')
_l_(73958)
_c_(73961, _n_(73959, "print", lambda: print), _n_(73960, "df", lambda: df))
_l_(73962)

def find_number(text):
    _l_(73972)

    num = _c_(73966, _a_(73964, _n_(73963, "re", lambda: re), "findall"), '[0-9]+', _n_(73965, "text", lambda: text))
    _l_(73967)
    aux = _c_(73970, _a_(73968, ' ', "join"), _n_(73969, "num", lambda: num))
    _l_(73971)
    return aux
_n_(73973, "df", lambda: df)['number'] = _c_(73979, _a_(73975, _n_(73974, "df", lambda: df)['address'], "apply"), lambda x: _c_(73978, _n_(73976, "find_number", lambda: find_number), _n_(73977, "x", lambda: x)))
_l_(73980)
_c_(73982, _n_(73981, "print", lambda: print), '\\Extracting numbers from dataframe columns:')
_l_(73983)
_c_(73986, _n_(73984, "print", lambda: print), _n_(73985, "df", lambda: df))
_l_(73987)