# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(115316)

except ImportError:
    pass
try:
    import numpy as np
    _l_(115318)

except ImportError:
    pass
_c_(115321, _a_(115320, _n_(115319, "pd", lambda: pd), "set_option"), 'display.max_rows', None)
_l_(115322)
_c_(115324, _n_(115323, "print", lambda: print), 'Original Orders DataFrame:')
_l_(115325)
_c_(115328, _n_(115326, "print", lambda: print), _n_(115327, "df", lambda: df))
_l_(115329)
_c_(115331, _n_(115330, "print", lambda: print), '\nTotal number of missing values of the said DataFrame:')
_l_(115332)
result = _c_(115339, _a_(115338, _c_(115337, _a_(115336, _c_(115335, _a_(115334, _n_(115333, "df", lambda: df), "isna")), "sum")), "sum"))
_l_(115340)
_c_(115343, _n_(115341, "print", lambda: print), _n_(115342, "result", lambda: result))
_l_(115344)