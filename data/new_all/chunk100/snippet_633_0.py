# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(65717)

except ImportError:
    pass
_c_(65720, _a_(65719, _n_(65718, "pd", lambda: pd), "set_option"), 'display.max_rows', None)
_l_(65721)
student_data = _c_(65724, _a_(65723, _n_(65722, "pd", lambda: pd), "DataFrame"), {'school_code': ['s001', 's002', 's003', 's001', 's002', 's004'], 'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'], 'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'], 'date_Of_Birth ': ['15/05/2002', '17/05/2002', '16/02/1999', '25/09/1998', '11/05/2002', '15/09/1997'], 'age': [12, 12, 13, 13, 14, 12], 'height': [173, 192, 186, 167, 151, 159], 'weight': [35, 32, 33, 30, 31, 32], 'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']}, index=['S1', 'S2', 'S3', 'S4', 'S5', 'S6'])
_l_(65725)
_c_(65727, _n_(65726, "print", lambda: print), 'Original DataFrame:')
_l_(65728)
_c_(65731, _n_(65729, "print", lambda: print), _n_(65730, "student_data", lambda: student_data))
_l_(65732)
_c_(65734, _n_(65733, "print", lambda: print), '\nCast grouping as a list:')
_l_(65735)
_c_(65740, _n_(65736, "print", lambda: print), _c_(65739, _n_(65737, "list", lambda: list), _n_(65738, "result", lambda: result)))
_l_(65741)