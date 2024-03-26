# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(105151)

except ImportError:
    pass
try:
    import numpy as np
    _l_(105153)

except ImportError:
    pass
_c_(105155, _n_(105154, "print", lambda: print), 'Original DataFrame:')
_l_(105156)
_c_(105159, _n_(105157, "print", lambda: print), _n_(105158, "df", lambda: df))
_l_(105160)
index = _a_(105162, _n_(105161, "df", lambda: df)['weight'], "index")[_c_(105167, _a_(105164, _n_(105163, "df", lambda: df)['weight'], "apply"), _a_(105166, _n_(105165, "np", lambda: np), "isnan"))]
_l_(105168)
df_index = _c_(105173, _a_(105172, _a_(105171, _a_(105170, _n_(105169, "df", lambda: df), "index"), "values"), "tolist"))
_l_(105174)
_c_(105176, _n_(105175, "print", lambda: print), "\nInteger index of rows with missing data in 'weight' column of the said dataframe:")
_l_(105177)
_c_(105184, _n_(105178, "print", lambda: print), [_c_(105182, _a_(105180, _n_(105179, "df_index", lambda: df_index), "index"), _n_(105181, "i", lambda: i)) for i in _n_(105183, "index", lambda: index)])
_l_(105185)