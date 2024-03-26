# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(118593)

except ImportError:
    pass
df = _c_(118596, _a_(118595, _n_(118594, "pd", lambda: pd), "DataFrame"), {'company_code': ['Abcd', 'EFGF', 'zefsalf', 'sdfslew', 'zekfsdf'], 'date_of_sale': ['12/05/2002', '16/02/1999', '25/09/1998', '12/02/2022', '15/09/1997'], 'sale_amount': [12348.5, 233331.2, 22.5, 2566552.0, 23.0]})
_l_(118597)
_c_(118599, _n_(118598, "print", lambda: print), 'Original DataFrame:')
_l_(118600)
_c_(118603, _n_(118601, "print", lambda: print), _n_(118602, "df", lambda: df))
_l_(118604)
_c_(118606, _n_(118605, "print", lambda: print), '\nUpper cases in comapny_code:')
_l_(118607)
_n_(118608, "df", lambda: df)['upper_company_code'] = _c_(118616, _n_(118609, "list", lambda: list), _c_(118615, _n_(118610, "map", lambda: map), lambda x: _c_(118613, _a_(118612, _n_(118611, "x", lambda: x), "upper")), _n_(118614, "df", lambda: df)['company_code']))
_l_(118617)
_c_(118620, _n_(118618, "print", lambda: print), _n_(118619, "df", lambda: df))
_l_(118621)
_c_(118623, _n_(118622, "print", lambda: print), '\nLower cases in comapny_code:')
_l_(118624)
_n_(118625, "df1", lambda: df1)['lower_company_code'] = _c_(118633, _n_(118626, "list", lambda: list), _c_(118632, _n_(118627, "map", lambda: map), lambda x: _c_(118630, _a_(118629, _n_(118628, "x", lambda: x), "lower")), _n_(118631, "df1", lambda: df1)['company_code']))
_l_(118634)
_c_(118637, _n_(118635, "print", lambda: print), _n_(118636, "df1", lambda: df1))
_l_(118638)