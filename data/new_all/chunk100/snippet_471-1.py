# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(117623)

except ImportError:
    pass
df = _c_(117626, _a_(117625, _n_(117624, "pd", lambda: pd), "DataFrame"), {'school_code': ['s001', 's002', 's003', 's001', 's002', 's004'], 'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'], 'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'], 'date_of_birth': ['15/05/2002', '17/05/2002', '16/02/1999', '25/09/1998', '11/05/2002', '15/09/1997'], 'weight': [35, 32, 33, 30, 31, 32], 't_id': ['t1', 't2', 't3', 't4', 't5', 't6']})
_l_(117627)
_c_(117629, _n_(117628, "print", lambda: print), 'Original DataFrame:')
_l_(117630)
_c_(117633, _n_(117631, "print", lambda: print), _n_(117632, "df", lambda: df))
_l_(117634)
_c_(117636, _n_(117635, "print", lambda: print), "\nMultiIndex using columns 't_id', ‘school_code’ and 'class':")
_l_(117637)
_c_(117640, _n_(117638, "print", lambda: print), _n_(117639, "df1", lambda: df1))
_l_(117641)
_c_(117643, _n_(117642, "print", lambda: print), '\nConvert 1st and 3rd levels in the index frame into columns:')
_l_(117644)
df2 = _c_(117647, _a_(117646, _n_(117645, "df1", lambda: df1), "reset_index"), level=['t_id', 'class'])
_l_(117648)
_c_(117651, _n_(117649, "print", lambda: print), _n_(117650, "df2", lambda: df2))
_l_(117652)