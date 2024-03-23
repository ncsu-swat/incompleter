# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(25489)

except ImportError:
    pass
_c_(25492, _a_(25491, _n_(25490, "pd", lambda: pd), "set_option"), 'display.max_rows', None)
_l_(25493)
student_data = _c_(25496, _a_(25495, _n_(25494, "pd", lambda: pd), "DataFrame"), {'school_code': ['s001', 's002', 's003', 's001', 's002', 's004'], 'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'], 'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'], 'date_Of_Birth ': ['15/05/2002', '17/05/2002', '16/02/1999', '25/09/1998', '11/05/2002', '15/09/1997'], 'age': [12, 12, 13, 13, 14, 12], 'height': [173, 192, 186, 167, 151, 159], 'weight': [35, 32, 33, 30, 31, 32], 'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']}, index=['S1', 'S2', 'S3', 'S4', 'S5', 'S6'])
_l_(25497)
_c_(25499, _n_(25498, "print", lambda: print), 'Original DataFrame:')
_l_(25500)
_c_(25503, _n_(25501, "print", lambda: print), _n_(25502, "student_data", lambda: student_data))
_l_(25504)
_c_(25506, _n_(25505, "print", lambda: print), '\nSplit the said data on school_code wise:')
_l_(25507)
_c_(25509, _n_(25508, "print", lambda: print), "Call school code 's001':")
_l_(25510)
_c_(25515, _n_(25511, "print", lambda: print), _c_(25514, _a_(25513, _n_(25512, "grouped", lambda: grouped), "get_group"), 's001'))
_l_(25516)
_c_(25518, _n_(25517, "print", lambda: print), "\nCall school code 's004':")
_l_(25519)
_c_(25524, _n_(25520, "print", lambda: print), _c_(25523, _a_(25522, _n_(25521, "grouped", lambda: grouped), "get_group"), 's004'))
_l_(25525)