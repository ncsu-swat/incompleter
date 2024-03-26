# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(105187)

except ImportError:
    pass
try:
    import numpy as np
    _l_(105189)

except ImportError:
    pass
df = _c_(105192, _a_(105191, _n_(105190, "pd", lambda: pd), "DataFrame"), {'school_code': ['s001', 's002', 's003', 's001', 's002', 's004'], 'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'], 'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'], 'date_of_birth': ['15/05/2002', '17/05/2002', '16/02/1999', '25/09/1998', '11/05/2002', '15/09/1997'], 'weight': [35, None, 33, 30, 31, None]}, index=['t1', 't2', 't3', 't4', 't5', 't6'])
_l_(105193)
_c_(105195, _n_(105194, "print", lambda: print), 'Original DataFrame:')
_l_(105196)
_c_(105199, _n_(105197, "print", lambda: print), _n_(105198, "df", lambda: df))
_l_(105200)
df_index = _c_(105205, _a_(105204, _a_(105203, _a_(105202, _n_(105201, "df", lambda: df), "index"), "values"), "tolist"))
_l_(105206)
_c_(105208, _n_(105207, "print", lambda: print), "\nInteger index of rows with missing data in 'weight' column of the said dataframe:")
_l_(105209)
_c_(105216, _n_(105210, "print", lambda: print), [_c_(105214, _a_(105212, _n_(105211, "df_index", lambda: df_index), "index"), _n_(105213, "i", lambda: i)) for i in _n_(105215, "index", lambda: index)])
_l_(105217)