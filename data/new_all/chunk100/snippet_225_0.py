# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(17515)

except ImportError:
    pass
df = _c_(17518, _a_(17517, _n_(17516, "pd", lambda: pd), "DataFrame"), {'school_code': ['s001', 's002', 's003', 's001', 's002', 's004'], 'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'], 'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'], 'date_of_birth': ['15/05/2002', '17/05/2002', '16/02/1999', '25/09/1998', '11/05/2002', '15/09/1997'], 'weight': [35, 37, 33, 30, 31, 32], 'tcode': ['t1', 't2', 't3', 't4', 't5', 't6']})
_l_(17519)
_c_(17521, _n_(17520, "print", lambda: print), 'Original DataFrame:')
_l_(17522)
_c_(17525, _n_(17523, "print", lambda: print), _n_(17524, "df", lambda: df))
_l_(17526)
_c_(17528, _n_(17527, "print", lambda: print), "\nCreate MultiIndex on 'tcode' and 'school_code':")
_l_(17529)
_c_(17532, _n_(17530, "print", lambda: print), _n_(17531, "df", lambda: df))
_l_(17533)
_c_(17535, _n_(17534, "print", lambda: print), "\nSelect rows(s) from 'tcode' column:")
_l_(17536)
_c_(17541, _n_(17537, "print", lambda: print), _c_(17540, _a_(17539, _n_(17538, "df", lambda: df), "query"), "tcode == 't2'"))
_l_(17542)
_c_(17544, _n_(17543, "print", lambda: print), "\nSelect rows(s) from 'school_code' column:")
_l_(17545)
_c_(17550, _n_(17546, "print", lambda: print), _c_(17549, _a_(17548, _n_(17547, "df", lambda: df), "query"), "school_code == 's001'"))
_l_(17551)
_c_(17553, _n_(17552, "print", lambda: print), "\nSelect rows(s) from 'tcode' and 'scode' columns:")
_l_(17554)
_c_(17559, _n_(17555, "print", lambda: print), _c_(17558, _a_(17557, _n_(17556, "df", lambda: df), "query"), "tcode == 't1'" and "school_code == 's001'"))
_l_(17560)