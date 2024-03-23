# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(68202)

except ImportError:
    pass
_c_(68205, _a_(68204, _n_(68203, "pd", lambda: pd), "set_option"), 'display.max_rows', None)
_l_(68206)
student_data = _c_(68209, _a_(68208, _n_(68207, "pd", lambda: pd), "DataFrame"), {'school_code': ['s001', 's002', 's003', 's001', 's002', 's004'], 'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'], 'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'], 'date_Of_Birth ': ['15/05/2002', '17/05/2002', '16/02/1999', '25/09/1998', '11/05/2002', '15/09/1997'], 'age': [12, 12, 13, 13, 14, 12], 'height': [173, 192, 186, 167, 151, 159], 'weight': [35, 32, 33, 30, 31, 32], 'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']}, index=['S1', 'S2', 'S3', 'S4', 'S5', 'S6'])
_l_(68210)
_c_(68212, _n_(68211, "print", lambda: print), 'Original DataFrame:')
_l_(68213)
_c_(68216, _n_(68214, "print", lambda: print), _n_(68215, "student_data", lambda: student_data))
_l_(68217)
_c_(68219, _n_(68218, "print", lambda: print), '\nSplit the said data on school_code wise:')
_l_(68220)
grouped_single = _c_(68223, _a_(68222, _n_(68221, "student_data", lambda: student_data), "groupby"), ['school_code'])
_l_(68224)
_c_(68226, _n_(68225, "print", lambda: print), 'Size of the grouped data - single column')
_l_(68227)
_c_(68232, _n_(68228, "print", lambda: print), _c_(68231, _a_(68230, _n_(68229, "grouped_single", lambda: grouped_single), "size")))
_l_(68233)
_c_(68235, _n_(68234, "print", lambda: print), '\nSplit the said data on school_code and class wise:')
_l_(68236)
_c_(68238, _n_(68237, "print", lambda: print), 'Size of the grouped data - multiple columns:')
_l_(68239)
_c_(68244, _n_(68240, "print", lambda: print), _c_(68243, _a_(68242, _n_(68241, "grouped_mul", lambda: grouped_mul), "size")))
_l_(68245)