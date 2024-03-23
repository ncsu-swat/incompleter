# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(16131)

except ImportError:
    pass
try:
    import numpy as np
    _l_(16133)

except ImportError:
    pass
df = _c_(16136, _a_(16135, _n_(16134, "pd", lambda: pd), "DataFrame"), {'school_code': ['s001', 's002', 's003', 's001', 's002', 's004'], 'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'], 'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'], 'date_of_birth': ['15/05/2002', '17/05/2002', '16/02/1999', '25/09/1998', '11/05/2002', '15/09/1997'], 'weight': [35, None, 33, 30, 31, None]}, index=['t1', 't2', 't3', 't4', 't5', 't6'])
_l_(16137)
_c_(16139, _n_(16138, "print", lambda: print), 'Original DataFrame:')
_l_(16140)
_c_(16143, _n_(16141, "print", lambda: print), _n_(16142, "df", lambda: df))
_l_(16144)
df_index = _c_(16149, _a_(16148, _a_(16147, _a_(16146, _n_(16145, "df", lambda: df), "index"), "values"), "tolist"))
_l_(16150)
_c_(16152, _n_(16151, "print", lambda: print), "\nInteger index of rows with missing data in 'weight' column of the said dataframe:")
_l_(16153)
_c_(16160, _n_(16154, "print", lambda: print), [_c_(16158, _a_(16156, _n_(16155, "df_index", lambda: df_index), "index"), _n_(16157, "i", lambda: i)) for i in _n_(16159, "index", lambda: index)])
_l_(16161)