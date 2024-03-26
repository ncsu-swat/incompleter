# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(101846)

except ImportError:
    pass
try:
    import re as re
    _l_(101848)

except ImportError:
    pass
_c_(101850, _n_(101849, "print", lambda: print), 'Original DataFrame:')
_l_(101851)
_c_(101854, _n_(101852, "print", lambda: print), _n_(101853, "df", lambda: df))
_l_(101855)

def find_unique_sentence(str1):
    _l_(101863)

    result = _c_(101859, _a_(101857, _n_(101856, "re", lambda: re), "findall"), '(?sm)(^[^\\r\\n]+$)(?!.*^\\1$)', _n_(101858, "str1", lambda: str1))
    _l_(101860)
    aux = _n_(101861, "result", lambda: result)
    _l_(101862)
    return aux
_n_(101864, "df", lambda: df)['unique_sentence'] = _c_(101870, _a_(101866, _n_(101865, "df", lambda: df)['address'], "apply"), lambda st: _c_(101869, _n_(101867, "find_unique_sentence", lambda: find_unique_sentence), _n_(101868, "st", lambda: st)))
_l_(101871)
_c_(101873, _n_(101872, "print", lambda: print), '\nExtract unique sentences :')
_l_(101874)
_c_(101877, _n_(101875, "print", lambda: print), _n_(101876, "df", lambda: df))
_l_(101878)