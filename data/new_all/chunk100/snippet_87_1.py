# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(86389)

except ImportError:
    pass
_c_(86391, _n_(86390, "print", lambda: print), 'Original dataframe:')
_l_(86392)
df = _c_(86396, _a_(86394, _n_(86393, "pd", lambda: pd), "DataFrame"), _n_(86395, "nums", lambda: nums))
_l_(86397)
_c_(86400, _n_(86398, "print", lambda: print), _n_(86399, "df", lambda: df))
_l_(86401)
_c_(86403, _n_(86402, "print", lambda: print), '\nAdd leading zeros:')
_l_(86404)
_n_(86405, "df", lambda: df)['amount'] = _c_(86413, _n_(86406, "list", lambda: list), _c_(86412, _n_(86407, "map", lambda: map), lambda x: _c_(86410, _a_(86409, _n_(86408, "x", lambda: x), "zfill"), 10), _n_(86411, "df", lambda: df)['amount']))
_l_(86414)
_c_(86417, _n_(86415, "print", lambda: print), _n_(86416, "df", lambda: df))
_l_(86418)