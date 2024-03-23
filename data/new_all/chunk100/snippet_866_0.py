# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(85455)

except ImportError:
    pass
student_data2 = _c_(85458, _a_(85457, _n_(85456, "pd", lambda: pd), "DataFrame"), {'student_id': ['S4', 'S5', 'S6', 'S7', 'S8'], 'name': ['Scarlette Fisher', 'Carla Williamson', 'Dante Morse', 'Kaiser William', 'Madeeha Preston'], 'marks': [201, 200, 198, 219, 201]})
_l_(85459)
_c_(85461, _n_(85460, "print", lambda: print), 'Original DataFrames:')
_l_(85462)
_c_(85465, _n_(85463, "print", lambda: print), _n_(85464, "student_data1", lambda: student_data1))
_l_(85466)
_c_(85469, _n_(85467, "print", lambda: print), _n_(85468, "student_data2", lambda: student_data2))
_l_(85470)
merged_data = _c_(85475, _a_(85472, _n_(85471, "pd", lambda: pd), "merge"), _n_(85473, "student_data1", lambda: student_data1), _n_(85474, "student_data2", lambda: student_data2), on='student_id', how='outer')
_l_(85476)
_c_(85478, _n_(85477, "print", lambda: print), 'Merged data (outer join):')
_l_(85479)
_c_(85482, _n_(85480, "print", lambda: print), _n_(85481, "merged_data", lambda: merged_data))
_l_(85483)