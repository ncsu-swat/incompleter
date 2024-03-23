# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(68292)

except ImportError:
    pass
_c_(68295, _a_(68294, _n_(68293, "pd", lambda: pd), "set_option"), 'display.max_rows', None)
_l_(68296)
student_data = _c_(68299, _a_(68298, _n_(68297, "pd", lambda: pd), "DataFrame"), {'school_code': ['s001', 's002', 's003', 's001', 's002', 's004'], 'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'], 'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'], 'date_Of_Birth ': ['15/05/2002', '17/05/2002', '16/02/1999', '25/09/1998', '11/05/2002', '15/09/1997'], 'age': [12, 12, 13, 13, 14, 12], 'height': [173, 192, 186, 167, 151, 159], 'weight': [35, 32, 33, 30, 31, 32], 'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']}, index=['S1', 'S2', 'S3', 'S4', 'S5', 'S6'])
_l_(68300)
_c_(68302, _n_(68301, "print", lambda: print), 'Original DataFrame:')
_l_(68303)
_c_(68306, _n_(68304, "print", lambda: print), _n_(68305, "student_data", lambda: student_data))
_l_(68307)
_c_(68309, _n_(68308, "print", lambda: print), '\nSplit the said data on school_code wise:')
_l_(68310)
_c_(68312, _n_(68311, "print", lambda: print), 'Size of the grouped data - single column')
_l_(68313)
_c_(68318, _n_(68314, "print", lambda: print), _c_(68317, _a_(68316, _n_(68315, "grouped_single", lambda: grouped_single), "size")))
_l_(68319)
_c_(68321, _n_(68320, "print", lambda: print), '\nSplit the said data on school_code and class wise:')
_l_(68322)
grouped_mul = _c_(68325, _a_(68324, _n_(68323, "student_data", lambda: student_data), "groupby"), ['school_code', 'class'])
_l_(68326)
_c_(68328, _n_(68327, "print", lambda: print), 'Size of the grouped data - multiple columns:')
_l_(68329)
_c_(68334, _n_(68330, "print", lambda: print), _c_(68333, _a_(68332, _n_(68331, "grouped_mul", lambda: grouped_mul), "size")))
_l_(68335)