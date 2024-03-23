# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(36839)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(36841)

except ImportError:
    pass
_c_(36843, _n_(36842, "print", lambda: print), 'Original Numpy array:')
_l_(36844)
_c_(36847, _n_(36845, "print", lambda: print), _n_(36846, "np_array", lambda: np_array))
_l_(36848)
_c_(36853, _n_(36849, "print", lambda: print), 'Type: ', _c_(36852, _n_(36850, "type", lambda: type), _n_(36851, "np_array", lambda: np_array)))
_l_(36854)
df = _c_(36861, _a_(36856, _n_(36855, "pd", lambda: pd), "DataFrame"), _c_(36860, _a_(36859, _a_(36858, _n_(36857, "np", lambda: np), "random"), "rand"), 12, 3), columns=['A', 'B', 'C'])
_l_(36862)
_c_(36864, _n_(36863, "print", lambda: print), "\nPanda's DataFrame: ")
_l_(36865)
_c_(36868, _n_(36866, "print", lambda: print), _n_(36867, "df", lambda: df))
_l_(36869)
_c_(36874, _n_(36870, "print", lambda: print), 'Type: ', _c_(36873, _n_(36871, "type", lambda: type), _n_(36872, "df", lambda: df)))
_l_(36875)