# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(86362)

except ImportError:
    pass
nums = {'amount': ['10', '250', '3000', '40000', '500000']}
_l_(86363)
_c_(86365, _n_(86364, "print", lambda: print), 'Original dataframe:')
_l_(86366)
_c_(86369, _n_(86367, "print", lambda: print), _n_(86368, "df", lambda: df))
_l_(86370)
_c_(86372, _n_(86371, "print", lambda: print), '\nAdd leading zeros:')
_l_(86373)
_n_(86374, "df", lambda: df)['amount'] = _c_(86382, _n_(86375, "list", lambda: list), _c_(86381, _n_(86376, "map", lambda: map), lambda x: _c_(86379, _a_(86378, _n_(86377, "x", lambda: x), "zfill"), 10), _n_(86380, "df", lambda: df)['amount']))
_l_(86383)
_c_(86386, _n_(86384, "print", lambda: print), _n_(86385, "df", lambda: df))
_l_(86387)