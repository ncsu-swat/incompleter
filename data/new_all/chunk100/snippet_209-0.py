# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(105117)

except ImportError:
    pass
try:
    import numpy as np
    _l_(105119)

except ImportError:
    pass
df = _c_(105122, _a_(105121, _n_(105120, "pd", lambda: pd), "DataFrame"), {'school_code': ['s001', 's002', 's003', 's001', 's002', 's004'], 'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'], 'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'], 'date_of_birth': ['15/05/2002', '17/05/2002', '16/02/1999', '25/09/1998', '11/05/2002', '15/09/1997'], 'weight': [35, None, 33, 30, 31, None]}, index=['t1', 't2', 't3', 't4', 't5', 't6'])
_l_(105123)
_c_(105125, _n_(105124, "print", lambda: print), 'Original DataFrame:')
_l_(105126)
_c_(105129, _n_(105127, "print", lambda: print), _n_(105128, "df", lambda: df))
_l_(105130)
index = _a_(105132, _n_(105131, "df", lambda: df)['weight'], "index")[_c_(105137, _a_(105134, _n_(105133, "df", lambda: df)['weight'], "apply"), _a_(105136, _n_(105135, "np", lambda: np), "isnan"))]
_l_(105138)
_c_(105140, _n_(105139, "print", lambda: print), "\nInteger index of rows with missing data in 'weight' column of the said dataframe:")
_l_(105141)
_c_(105148, _n_(105142, "print", lambda: print), [_c_(105146, _a_(105144, _n_(105143, "df_index", lambda: df_index), "index"), _n_(105145, "i", lambda: i)) for i in _n_(105147, "index", lambda: index)])
_l_(105149)