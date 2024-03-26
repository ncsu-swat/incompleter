# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(118546)

except ImportError:
    pass
df1 = _c_(118549, _a_(118548, _n_(118547, "pd", lambda: pd), "DataFrame"), {'company_code': ['Abcd', 'EFGF', 'zefsalf', 'sdfslew', 'zekfsdf'], 'date_of_sale': ['12/05/2002', '16/02/1999', '25/09/1998', '12/02/2022', '15/09/1997'], 'sale_amount': [12348.5, 233331.2, 22.5, 2566552.0, 23.0]})
_l_(118550)
_c_(118552, _n_(118551, "print", lambda: print), 'Original DataFrame:')
_l_(118553)
_c_(118556, _n_(118554, "print", lambda: print), _n_(118555, "df", lambda: df))
_l_(118557)
_c_(118559, _n_(118558, "print", lambda: print), '\nUpper cases in comapny_code:')
_l_(118560)
_n_(118561, "df", lambda: df)['upper_company_code'] = _c_(118569, _n_(118562, "list", lambda: list), _c_(118568, _n_(118563, "map", lambda: map), lambda x: _c_(118566, _a_(118565, _n_(118564, "x", lambda: x), "upper")), _n_(118567, "df", lambda: df)['company_code']))
_l_(118570)
_c_(118573, _n_(118571, "print", lambda: print), _n_(118572, "df", lambda: df))
_l_(118574)
_c_(118576, _n_(118575, "print", lambda: print), '\nLower cases in comapny_code:')
_l_(118577)
_n_(118578, "df1", lambda: df1)['lower_company_code'] = _c_(118586, _n_(118579, "list", lambda: list), _c_(118585, _n_(118580, "map", lambda: map), lambda x: _c_(118583, _a_(118582, _n_(118581, "x", lambda: x), "lower")), _n_(118584, "df1", lambda: df1)['company_code']))
_l_(118587)
_c_(118590, _n_(118588, "print", lambda: print), _n_(118589, "df1", lambda: df1))
_l_(118591)