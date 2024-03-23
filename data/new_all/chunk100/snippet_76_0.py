# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(78196)

except ImportError:
    pass
_c_(78198, _n_(78197, "print", lambda: print), 'Original DataFrame:')
_l_(78199)
_c_(78202, _n_(78200, "print", lambda: print), _n_(78201, "df", lambda: df))
_l_(78203)
_c_(78205, _n_(78204, "print", lambda: print), '\nNumeric values present in company_code column:')
_l_(78206)
_n_(78207, "df", lambda: df)['company_code_is_digit'] = _c_(78215, _n_(78208, "list", lambda: list), _c_(78214, _n_(78209, "map", lambda: map), lambda x: _c_(78212, _a_(78211, _n_(78210, "x", lambda: x), "isdigit")), _n_(78213, "df", lambda: df)['company_code']))
_l_(78216)
_c_(78219, _n_(78217, "print", lambda: print), _n_(78218, "df", lambda: df))
_l_(78220)