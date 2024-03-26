# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(120025)

except ImportError:
    pass
_c_(120027, _n_(120026, "print", lambda: print), 'Original DataFrame:')
_l_(120028)
_c_(120031, _n_(120029, "print", lambda: print), _n_(120030, "df", lambda: df))
_l_(120032)
_c_(120034, _n_(120033, "print", lambda: print), '\nNumeric values present in company_code column:')
_l_(120035)
_n_(120036, "df", lambda: df)['company_code_is_digit'] = _c_(120044, _n_(120037, "list", lambda: list), _c_(120043, _n_(120038, "map", lambda: map), lambda x: _c_(120041, _a_(120040, _n_(120039, "x", lambda: x), "isdigit")), _n_(120042, "df", lambda: df)['company_code']))
_l_(120045)
_c_(120048, _n_(120046, "print", lambda: print), _n_(120047, "df", lambda: df))
_l_(120049)