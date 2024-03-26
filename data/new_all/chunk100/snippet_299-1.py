# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(109198)

except ImportError:
    pass
_c_(109201, _a_(109200, _n_(109199, "pd", lambda: pd), "set_option"), 'display.max_rows', None)
_l_(109202)
student_data = _c_(109205, _a_(109204, _n_(109203, "pd", lambda: pd), "DataFrame"), {'school_code': ['s001', 's002', 's003', 's001', 's002', 's004'], 'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'], 'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'], 'date_Of_Birth ': ['15/05/2002', '17/05/2002', '16/02/1999', '25/09/1998', '11/05/2002', '15/09/1997'], 'age': [12, 12, 13, 13, 14, 12], 'height': [173, 192, 186, 167, 151, 159], 'weight': [35, 32, 33, 30, 31, 32], 'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']}, index=['S1', 'S2', 'S3', 'S4', 'S5', 'S6'])
_l_(109206)
_c_(109208, _n_(109207, "print", lambda: print), 'Original DataFrame:')
_l_(109209)
_c_(109212, _n_(109210, "print", lambda: print), _n_(109211, "student_data", lambda: student_data))
_l_(109213)
_c_(109215, _n_(109214, "print", lambda: print), '\nSplit the said data on school_code wise:')
_l_(109216)
_c_(109218, _n_(109217, "print", lambda: print), "Call school code 's001':")
_l_(109219)
_c_(109224, _n_(109220, "print", lambda: print), _c_(109223, _a_(109222, _n_(109221, "grouped", lambda: grouped), "get_group"), 's001'))
_l_(109225)
_c_(109227, _n_(109226, "print", lambda: print), "\nCall school code 's004':")
_l_(109228)
_c_(109233, _n_(109229, "print", lambda: print), _c_(109232, _a_(109231, _n_(109230, "grouped", lambda: grouped), "get_group"), 's004'))
_l_(109234)