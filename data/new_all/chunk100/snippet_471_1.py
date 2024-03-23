# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(49546)

except ImportError:
    pass
df = _c_(49549, _a_(49548, _n_(49547, "pd", lambda: pd), "DataFrame"), {'school_code': ['s001', 's002', 's003', 's001', 's002', 's004'], 'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'], 'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'], 'date_of_birth': ['15/05/2002', '17/05/2002', '16/02/1999', '25/09/1998', '11/05/2002', '15/09/1997'], 'weight': [35, 32, 33, 30, 31, 32], 't_id': ['t1', 't2', 't3', 't4', 't5', 't6']})
_l_(49550)
_c_(49552, _n_(49551, "print", lambda: print), 'Original DataFrame:')
_l_(49553)
_c_(49556, _n_(49554, "print", lambda: print), _n_(49555, "df", lambda: df))
_l_(49557)
_c_(49559, _n_(49558, "print", lambda: print), "\nMultiIndex using columns 't_id', ‘school_code’ and 'class':")
_l_(49560)
_c_(49563, _n_(49561, "print", lambda: print), _n_(49562, "df1", lambda: df1))
_l_(49564)
_c_(49566, _n_(49565, "print", lambda: print), '\nConvert 1st and 3rd levels in the index frame into columns:')
_l_(49567)
df2 = _c_(49570, _a_(49569, _n_(49568, "df1", lambda: df1), "reset_index"), level=['t_id', 'class'])
_l_(49571)
_c_(49574, _n_(49572, "print", lambda: print), _n_(49573, "df2", lambda: df2))
_l_(49575)