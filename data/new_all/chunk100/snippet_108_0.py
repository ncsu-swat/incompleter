# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(5638)

except ImportError:
    pass
df = _c_(5641, _a_(5640, _n_(5639, "pd", lambda: pd), "DataFrame"), {'company_code': ['A', 'B', 'C', 'D', 'A'], 'date_of_sale': ['12/05/2002', '16/02/1999', '25/09/1998', '12/02/2022', '15/09/1997'], 'sale_amount': [12348.5, 233331.2, 22.5, 2566552.0, 23.0]})
_l_(5642)
_c_(5644, _n_(5643, "print", lambda: print), 'Original DataFrame:')
_l_(5645)
_c_(5648, _n_(5646, "print", lambda: print), _n_(5647, "df", lambda: df))
_l_(5649)
_c_(5651, _n_(5650, "print", lambda: print), '\nReplace A with c:')
_l_(5652)
_c_(5655, _n_(5653, "print", lambda: print), _n_(5654, "df", lambda: df))
_l_(5656)