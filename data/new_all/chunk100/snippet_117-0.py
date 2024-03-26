# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(101063)

except ImportError:
    pass
_c_(101066, _a_(101065, _n_(101064, "pd", lambda: pd), "set_option"), 'display.max_rows', None)
_l_(101067)
df = _c_(101070, _a_(101069, _n_(101068, "pd", lambda: pd), "DataFrame"), {'school_code': ['s001', 's002', 's003', 's001', 's002', 's001'], 'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'], 'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'], 'date_Of_Birth ': ['15/05/2002', '17/05/2002', '16/02/1999', '25/09/1998', '11/05/2002', '15/09/1997'], 'age': [12, 12, 13, 13, 14, 12], 'height': [173, 192, 186, 167, 151, 159], 'weight': [35, 32, 33, 30, 31, 32], 'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']}, index=['S1', 'S2', 'S3', 'S4', 'S5', 'S6'])
_l_(101071)
_c_(101073, _n_(101072, "print", lambda: print), 'Original DataFrame:')
_l_(101074)
_c_(101077, _n_(101075, "print", lambda: print), _n_(101076, "df", lambda: df))
_l_(101078)
_c_(101080, _n_(101079, "print", lambda: print), '\nGroup by with multiple aggregations:')
_l_(101081)
_c_(101084, _n_(101082, "print", lambda: print), _n_(101083, "result", lambda: result))
_l_(101085)