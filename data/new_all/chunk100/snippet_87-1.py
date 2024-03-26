# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(121001)

except ImportError:
    pass
nums = {'amount': ['10', '250', '3000', '40000', '500000']}
_l_(121002)
_c_(121004, _n_(121003, "print", lambda: print), 'Original dataframe:')
_l_(121005)
_c_(121008, _n_(121006, "print", lambda: print), _n_(121007, "df", lambda: df))
_l_(121009)
_c_(121011, _n_(121010, "print", lambda: print), '\nAdd leading zeros:')
_l_(121012)
_n_(121013, "df", lambda: df)['amount'] = _c_(121021, _n_(121014, "list", lambda: list), _c_(121020, _n_(121015, "map", lambda: map), lambda x: _c_(121018, _a_(121017, _n_(121016, "x", lambda: x), "zfill"), 10), _n_(121019, "df", lambda: df)['amount']))
_l_(121022)
_c_(121025, _n_(121023, "print", lambda: print), _n_(121024, "df", lambda: df))
_l_(121026)