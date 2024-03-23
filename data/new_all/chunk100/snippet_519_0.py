# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(52996)

except ImportError:
    pass
_c_(52998, _n_(52997, "print", lambda: print), 'Create an Int64Index:')
_l_(52999)
_c_(53002, _n_(53000, "print", lambda: print), _n_(53001, "df_i64", lambda: df_i64))
_l_(53003)
_c_(53005, _n_(53004, "print", lambda: print), '\nView the Index:')
_l_(53006)
_c_(53010, _n_(53007, "print", lambda: print), _a_(53009, _n_(53008, "df_i64", lambda: df_i64), "index"))
_l_(53011)
_c_(53013, _n_(53012, "print", lambda: print), '\nFloating-point labels using Float64Index:')
_l_(53014)
df_f64 = _c_(53017, _a_(53016, _n_(53015, "pd", lambda: pd), "DataFrame"), {'school_code': ['s001', 's002', 's003', 's001', 's002', 's004'], 'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'], 'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'], 'date_Of_Birth ': ['15/05/2002', '17/05/2002', '16/02/1999', '25/09/1998', '11/05/2002', '15/09/1997'], 'weight': [35, 32, 33, 30, 31, 32], 'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']}, index=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6])
_l_(53018)
_c_(53021, _n_(53019, "print", lambda: print), _n_(53020, "df_f64", lambda: df_f64))
_l_(53022)
_c_(53024, _n_(53023, "print", lambda: print), '\nView the Index:')
_l_(53025)
_c_(53029, _n_(53026, "print", lambda: print), _a_(53028, _n_(53027, "df_f64", lambda: df_f64), "index"))
_l_(53030)