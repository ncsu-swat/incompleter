# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(53032)

except ImportError:
    pass
_c_(53034, _n_(53033, "print", lambda: print), 'Create an Int64Index:')
_l_(53035)
df_i64 = _c_(53038, _a_(53037, _n_(53036, "pd", lambda: pd), "DataFrame"), {'school_code': ['s001', 's002', 's003', 's001', 's002', 's004'], 'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'], 'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'], 'date_Of_Birth': ['15/05/2002', '17/05/2002', '16/02/1999', '25/09/1998', '11/05/2002', '15/09/1997'], 'weight': [35, 32, 33, 30, 31, 32], 'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']}, index=[1, 2, 3, 4, 5, 6])
_l_(53039)
_c_(53042, _n_(53040, "print", lambda: print), _n_(53041, "df_i64", lambda: df_i64))
_l_(53043)
_c_(53045, _n_(53044, "print", lambda: print), '\nView the Index:')
_l_(53046)
_c_(53050, _n_(53047, "print", lambda: print), _a_(53049, _n_(53048, "df_i64", lambda: df_i64), "index"))
_l_(53051)
_c_(53053, _n_(53052, "print", lambda: print), '\nFloating-point labels using Float64Index:')
_l_(53054)
_c_(53057, _n_(53055, "print", lambda: print), _n_(53056, "df_f64", lambda: df_f64))
_l_(53058)
_c_(53060, _n_(53059, "print", lambda: print), '\nView the Index:')
_l_(53061)
_c_(53065, _n_(53062, "print", lambda: print), _a_(53064, _n_(53063, "df_f64", lambda: df_f64), "index"))
_l_(53066)