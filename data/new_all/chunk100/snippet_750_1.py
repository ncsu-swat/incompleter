# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(75883)

except ImportError:
    pass
try:
    import re as re
    _l_(75885)

except ImportError:
    pass
_c_(75887, _n_(75886, "print", lambda: print), 'Original DataFrame:')
_l_(75888)
_c_(75891, _n_(75889, "print", lambda: print), _n_(75890, "df", lambda: df))
_l_(75892)

def find_valid_dates(dt):
    _l_(75900)

    result = _c_(75896, _a_(75894, _n_(75893, "re", lambda: re), "findall"), '\\b(1[0-2]|0[1-9])/(3[01]|[12][0-9]|0[1-9])/([0-9]{4})\\b', _n_(75895, "dt", lambda: dt))
    _l_(75897)
    aux = _n_(75898, "result", lambda: result)
    _l_(75899)
    return aux
_n_(75901, "df", lambda: df)['valid_dates'] = _c_(75907, _a_(75903, _n_(75902, "df", lambda: df)['date_of_sale'], "apply"), lambda dt: _c_(75906, _n_(75904, "find_valid_dates", lambda: find_valid_dates), _n_(75905, "dt", lambda: dt)))
_l_(75908)
_c_(75910, _n_(75909, "print", lambda: print), '\nValid dates (format: mm-dd-yyyy):')
_l_(75911)
_c_(75914, _n_(75912, "print", lambda: print), _n_(75913, "df", lambda: df))
_l_(75915)