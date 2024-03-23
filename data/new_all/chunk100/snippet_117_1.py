# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(6014)

except ImportError:
    pass
_c_(6017, _a_(6016, _n_(6015, "pd", lambda: pd), "set_option"), 'display.max_rows', None)
_l_(6018)
df = _c_(6021, _a_(6020, _n_(6019, "pd", lambda: pd), "DataFrame"), {'school_code': ['s001', 's002', 's003', 's001', 's002', 's001'], 'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'], 'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'], 'date_Of_Birth ': ['15/05/2002', '17/05/2002', '16/02/1999', '25/09/1998', '11/05/2002', '15/09/1997'], 'age': [12, 12, 13, 13, 14, 12], 'height': [173, 192, 186, 167, 151, 159], 'weight': [35, 32, 33, 30, 31, 32], 'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']}, index=['S1', 'S2', 'S3', 'S4', 'S5', 'S6'])
_l_(6022)
_c_(6024, _n_(6023, "print", lambda: print), 'Original DataFrame:')
_l_(6025)
_c_(6028, _n_(6026, "print", lambda: print), _n_(6027, "df", lambda: df))
_l_(6029)
_c_(6031, _n_(6030, "print", lambda: print), '\nGroup by with multiple aggregations:')
_l_(6032)
_c_(6035, _n_(6033, "print", lambda: print), _n_(6034, "result", lambda: result))
_l_(6036)