# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(117654)

except ImportError:
    pass
df = _c_(117657, _a_(117656, _n_(117655, "pd", lambda: pd), "DataFrame"), {'school_code': ['s001', 's002', 's003', 's001', 's002', 's004'], 'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'], 'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'], 'date_of_birth': ['15/05/2002', '17/05/2002', '16/02/1999', '25/09/1998', '11/05/2002', '15/09/1997'], 'weight': [35, 32, 33, 30, 31, 32], 't_id': ['t1', 't2', 't3', 't4', 't5', 't6']})
_l_(117658)
_c_(117660, _n_(117659, "print", lambda: print), 'Original DataFrame:')
_l_(117661)
_c_(117664, _n_(117662, "print", lambda: print), _n_(117663, "df", lambda: df))
_l_(117665)
_c_(117667, _n_(117666, "print", lambda: print), "\nMultiIndex using columns 't_id', ‘school_code’ and 'class':")
_l_(117668)
df1 = _c_(117671, _a_(117670, _n_(117669, "df", lambda: df), "set_index"), ['t_id', 'school_code', 'class'])
_l_(117672)
_c_(117675, _n_(117673, "print", lambda: print), _n_(117674, "df1", lambda: df1))
_l_(117676)
_c_(117678, _n_(117677, "print", lambda: print), '\nConvert 1st and 3rd levels in the index frame into columns:')
_l_(117679)
_c_(117682, _n_(117680, "print", lambda: print), _n_(117681, "df2", lambda: df2))
_l_(117683)