# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(25527)

except ImportError:
    pass
_c_(25530, _a_(25529, _n_(25528, "pd", lambda: pd), "set_option"), 'display.max_rows', None)
_l_(25531)
_c_(25533, _n_(25532, "print", lambda: print), 'Original DataFrame:')
_l_(25534)
_c_(25537, _n_(25535, "print", lambda: print), _n_(25536, "student_data", lambda: student_data))
_l_(25538)
_c_(25540, _n_(25539, "print", lambda: print), '\nSplit the said data on school_code wise:')
_l_(25541)
grouped = _c_(25544, _a_(25543, _n_(25542, "student_data", lambda: student_data), "groupby"), ['school_code'])
_l_(25545)
_c_(25547, _n_(25546, "print", lambda: print), "Call school code 's001':")
_l_(25548)
_c_(25553, _n_(25549, "print", lambda: print), _c_(25552, _a_(25551, _n_(25550, "grouped", lambda: grouped), "get_group"), 's001'))
_l_(25554)
_c_(25556, _n_(25555, "print", lambda: print), "\nCall school code 's004':")
_l_(25557)
_c_(25562, _n_(25558, "print", lambda: print), _c_(25561, _a_(25560, _n_(25559, "grouped", lambda: grouped), "get_group"), 's004'))
_l_(25563)