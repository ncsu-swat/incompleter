# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(85416)

except ImportError:
    pass
df = _c_(85419, _a_(85418, _n_(85417, "pd", lambda: pd), "DataFrame"), {'school_code': ['s001', 's002', 's003', 's001', 's002', 's004'], 'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'], 'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'], 'date_Of_Birth': ['15/05/2002', '17/05/2002', '16/02/1999', '25/09/1998', '11/05/2002', '15/09/1997'], 'weight': [35, 32, 33, 30, 31, 32], 'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']}, index=['t1', 't2', 't3', 't4', 't5', 't6'])
_l_(85420)
_c_(85422, _n_(85421, "print", lambda: print), 'Original DataFrame:')
_l_(85423)
_c_(85426, _n_(85424, "print", lambda: print), _n_(85425, "df", lambda: df))
_l_(85427)
_c_(85429, _n_(85428, "print", lambda: print), '\nSaid DataFrame with a title or name of the index column:')
_l_(85430)
_c_(85433, _n_(85431, "print", lambda: print), _n_(85432, "df", lambda: df))
_l_(85434)