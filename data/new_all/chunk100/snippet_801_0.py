# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(80860)

except ImportError:
    pass
_c_(80862, _n_(80861, "print", lambda: print), 'Original DataFrame with single index:')
_l_(80863)
_c_(80866, _n_(80864, "print", lambda: print), _n_(80865, "df", lambda: df))
_l_(80867)
_c_(80869, _n_(80868, "print", lambda: print), '\nIndex of rows where specified column matches certain value:')
_l_(80870)
_c_(80877, _n_(80871, "print", lambda: print), _c_(80876, _a_(80875, _a_(80873, _n_(80872, "df", lambda: df), "index")[_n_(80874, "df", lambda: df)['school_code'] == 's001'], "tolist")))
_l_(80878)