# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(52516)

except ImportError:
    pass
try:
    import numpy as np
    _l_(52518)

except ImportError:
    pass
_c_(52521, _a_(52520, _n_(52519, "pd", lambda: pd), "set_option"), 'display.max_rows', None)
_l_(52522)
_c_(52524, _n_(52523, "print", lambda: print), 'Original Orders DataFrame:')
_l_(52525)
_c_(52528, _n_(52526, "print", lambda: print), _n_(52527, "df", lambda: df))
_l_(52529)
_c_(52531, _n_(52530, "print", lambda: print), '\nReplace NaNs with a single constant value:')
_l_(52532)
result = _c_(52535, _a_(52534, _n_(52533, "df", lambda: df)['ord_no'], "fillna"), 0, inplace=False)
_l_(52536)
_c_(52539, _n_(52537, "print", lambda: print), _n_(52538, "result", lambda: result))
_l_(52540)