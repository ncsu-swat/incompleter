# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(51581)

except ImportError:
    pass
df1 = _c_(51584, _a_(51583, _n_(51582, "pd", lambda: pd), "DataFrame"), {'company_code': ['Abcd', 'EFGF', 'zefsalf', 'sdfslew', 'zekfsdf'], 'date_of_sale': ['12/05/2002', '16/02/1999', '25/09/1998', '12/02/2022', '15/09/1997'], 'sale_amount': [12348.5, 233331.2, 22.5, 2566552.0, 23.0]})
_l_(51585)
_c_(51587, _n_(51586, "print", lambda: print), 'Original DataFrame:')
_l_(51588)
_c_(51591, _n_(51589, "print", lambda: print), _n_(51590, "df", lambda: df))
_l_(51592)
_c_(51594, _n_(51593, "print", lambda: print), '\nUpper cases in comapny_code:')
_l_(51595)
_n_(51596, "df", lambda: df)['upper_company_code'] = _c_(51604, _n_(51597, "list", lambda: list), _c_(51603, _n_(51598, "map", lambda: map), lambda x: _c_(51601, _a_(51600, _n_(51599, "x", lambda: x), "upper")), _n_(51602, "df", lambda: df)['company_code']))
_l_(51605)
_c_(51608, _n_(51606, "print", lambda: print), _n_(51607, "df", lambda: df))
_l_(51609)
_c_(51611, _n_(51610, "print", lambda: print), '\nLower cases in comapny_code:')
_l_(51612)
_n_(51613, "df1", lambda: df1)['lower_company_code'] = _c_(51621, _n_(51614, "list", lambda: list), _c_(51620, _n_(51615, "map", lambda: map), lambda x: _c_(51618, _a_(51617, _n_(51616, "x", lambda: x), "lower")), _n_(51619, "df1", lambda: df1)['company_code']))
_l_(51622)
_c_(51625, _n_(51623, "print", lambda: print), _n_(51624, "df1", lambda: df1))
_l_(51626)