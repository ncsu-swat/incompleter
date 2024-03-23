# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(16163)

except ImportError:
    pass
try:
    import numpy as np
    _l_(16165)

except ImportError:
    pass
_c_(16167, _n_(16166, "print", lambda: print), 'Original DataFrame:')
_l_(16168)
_c_(16171, _n_(16169, "print", lambda: print), _n_(16170, "df", lambda: df))
_l_(16172)
index = _a_(16174, _n_(16173, "df", lambda: df)['weight'], "index")[_c_(16179, _a_(16176, _n_(16175, "df", lambda: df)['weight'], "apply"), _a_(16178, _n_(16177, "np", lambda: np), "isnan"))]
_l_(16180)
df_index = _c_(16185, _a_(16184, _a_(16183, _a_(16182, _n_(16181, "df", lambda: df), "index"), "values"), "tolist"))
_l_(16186)
_c_(16188, _n_(16187, "print", lambda: print), "\nInteger index of rows with missing data in 'weight' column of the said dataframe:")
_l_(16189)
_c_(16196, _n_(16190, "print", lambda: print), [_c_(16194, _a_(16192, _n_(16191, "df_index", lambda: df_index), "index"), _n_(16193, "i", lambda: i)) for i in _n_(16195, "index", lambda: index)])
_l_(16197)