# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(71802)

except ImportError:
    pass
df = _c_(71805, _a_(71804, _n_(71803, "pd", lambda: pd), "DataFrame"), {'company_code': ['A', 'B', 'C', 'D', 'A'], 'date_of_sale': ['12/05/2002', '16/02/1999', '25/09/1998', '12/02/2022', '15/09/1997'], 'sale_amount': [12348.5, 233331.2, 22.5, 2566552.0, 23.0]})
_l_(71806)
_c_(71808, _n_(71807, "print", lambda: print), 'Original DataFrame:')
_l_(71809)
_c_(71812, _n_(71810, "print", lambda: print), _n_(71811, "df", lambda: df))
_l_(71813)
_c_(71815, _n_(71814, "print", lambda: print), '\nReplace A with c:')
_l_(71816)
_c_(71819, _n_(71817, "print", lambda: print), _n_(71818, "df", lambda: df))
_l_(71820)