# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(16199)

except ImportError:
    pass
try:
    import numpy as np
    _l_(16201)

except ImportError:
    pass
df = _c_(16204, _a_(16203, _n_(16202, "pd", lambda: pd), "DataFrame"), {'school_code': ['s001', 's002', 's003', 's001', 's002', 's004'], 'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'], 'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'], 'date_of_birth': ['15/05/2002', '17/05/2002', '16/02/1999', '25/09/1998', '11/05/2002', '15/09/1997'], 'weight': [35, None, 33, 30, 31, None]}, index=['t1', 't2', 't3', 't4', 't5', 't6'])
_l_(16205)
_c_(16207, _n_(16206, "print", lambda: print), 'Original DataFrame:')
_l_(16208)
_c_(16211, _n_(16209, "print", lambda: print), _n_(16210, "df", lambda: df))
_l_(16212)
index = _a_(16214, _n_(16213, "df", lambda: df)['weight'], "index")[_c_(16219, _a_(16216, _n_(16215, "df", lambda: df)['weight'], "apply"), _a_(16218, _n_(16217, "np", lambda: np), "isnan"))]
_l_(16220)
_c_(16222, _n_(16221, "print", lambda: print), "\nInteger index of rows with missing data in 'weight' column of the said dataframe:")
_l_(16223)
_c_(16230, _n_(16224, "print", lambda: print), [_c_(16228, _a_(16226, _n_(16225, "df_index", lambda: df_index), "index"), _n_(16227, "i", lambda: i)) for i in _n_(16229, "index", lambda: index)])
_l_(16231)