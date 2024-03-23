# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(49515)

except ImportError:
    pass
df = _c_(49518, _a_(49517, _n_(49516, "pd", lambda: pd), "DataFrame"), {'school_code': ['s001', 's002', 's003', 's001', 's002', 's004'], 'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'], 'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'], 'date_of_birth': ['15/05/2002', '17/05/2002', '16/02/1999', '25/09/1998', '11/05/2002', '15/09/1997'], 'weight': [35, 32, 33, 30, 31, 32], 't_id': ['t1', 't2', 't3', 't4', 't5', 't6']})
_l_(49519)
_c_(49521, _n_(49520, "print", lambda: print), 'Original DataFrame:')
_l_(49522)
_c_(49525, _n_(49523, "print", lambda: print), _n_(49524, "df", lambda: df))
_l_(49526)
_c_(49528, _n_(49527, "print", lambda: print), "\nMultiIndex using columns 't_id', ‘school_code’ and 'class':")
_l_(49529)
df1 = _c_(49532, _a_(49531, _n_(49530, "df", lambda: df), "set_index"), ['t_id', 'school_code', 'class'])
_l_(49533)
_c_(49536, _n_(49534, "print", lambda: print), _n_(49535, "df1", lambda: df1))
_l_(49537)
_c_(49539, _n_(49538, "print", lambda: print), '\nConvert 1st and 3rd levels in the index frame into columns:')
_l_(49540)
_c_(49543, _n_(49541, "print", lambda: print), _n_(49542, "df2", lambda: df2))
_l_(49544)