# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(85485)

except ImportError:
    pass
student_data1 = _c_(85488, _a_(85487, _n_(85486, "pd", lambda: pd), "DataFrame"), {'student_id': ['S1', 'S2', 'S3', 'S4', 'S5'], 'name': ['Danniella Fenton', 'Ryder Storey', 'Bryce Jensen', 'Ed Bernal', 'Kwame Morin'], 'marks': [200, 210, 190, 222, 199]})
_l_(85489)
_c_(85491, _n_(85490, "print", lambda: print), 'Original DataFrames:')
_l_(85492)
_c_(85495, _n_(85493, "print", lambda: print), _n_(85494, "student_data1", lambda: student_data1))
_l_(85496)
_c_(85499, _n_(85497, "print", lambda: print), _n_(85498, "student_data2", lambda: student_data2))
_l_(85500)
merged_data = _c_(85505, _a_(85502, _n_(85501, "pd", lambda: pd), "merge"), _n_(85503, "student_data1", lambda: student_data1), _n_(85504, "student_data2", lambda: student_data2), on='student_id', how='outer')
_l_(85506)
_c_(85508, _n_(85507, "print", lambda: print), 'Merged data (outer join):')
_l_(85509)
_c_(85512, _n_(85510, "print", lambda: print), _n_(85511, "merged_data", lambda: merged_data))
_l_(85513)