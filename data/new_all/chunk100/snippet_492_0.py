# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(51534)

except ImportError:
    pass
df = _c_(51537, _a_(51536, _n_(51535, "pd", lambda: pd), "DataFrame"), {'company_code': ['Abcd', 'EFGF', 'zefsalf', 'sdfslew', 'zekfsdf'], 'date_of_sale': ['12/05/2002', '16/02/1999', '25/09/1998', '12/02/2022', '15/09/1997'], 'sale_amount': [12348.5, 233331.2, 22.5, 2566552.0, 23.0]})
_l_(51538)
_c_(51540, _n_(51539, "print", lambda: print), 'Original DataFrame:')
_l_(51541)
_c_(51544, _n_(51542, "print", lambda: print), _n_(51543, "df", lambda: df))
_l_(51545)
_c_(51547, _n_(51546, "print", lambda: print), '\nUpper cases in comapny_code:')
_l_(51548)
_n_(51549, "df", lambda: df)['upper_company_code'] = _c_(51557, _n_(51550, "list", lambda: list), _c_(51556, _n_(51551, "map", lambda: map), lambda x: _c_(51554, _a_(51553, _n_(51552, "x", lambda: x), "upper")), _n_(51555, "df", lambda: df)['company_code']))
_l_(51558)
_c_(51561, _n_(51559, "print", lambda: print), _n_(51560, "df", lambda: df))
_l_(51562)
_c_(51564, _n_(51563, "print", lambda: print), '\nLower cases in comapny_code:')
_l_(51565)
_n_(51566, "df1", lambda: df1)['lower_company_code'] = _c_(51574, _n_(51567, "list", lambda: list), _c_(51573, _n_(51568, "map", lambda: map), lambda x: _c_(51571, _a_(51570, _n_(51569, "x", lambda: x), "lower")), _n_(51572, "df1", lambda: df1)['company_code']))
_l_(51575)
_c_(51578, _n_(51576, "print", lambda: print), _n_(51577, "df1", lambda: df1))
_l_(51579)