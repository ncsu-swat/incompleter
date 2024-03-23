# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(41796)

except ImportError:
    pass
_c_(41798, _n_(41797, "print", lambda: print), 'Original Data Series:')
_l_(41799)
_c_(41802, _n_(41800, "print", lambda: print), _n_(41801, "s", lambda: s))
_l_(41803)
s = _c_(41806, _a_(41805, _n_(41804, "s", lambda: s), "reindex"), index=['B', 'A', 'C', 'D', 'E'])
_l_(41807)
_c_(41809, _n_(41808, "print", lambda: print), 'Data Series after changing the order of index:')
_l_(41810)
_c_(41813, _n_(41811, "print", lambda: print), _n_(41812, "s", lambda: s))
_l_(41814)