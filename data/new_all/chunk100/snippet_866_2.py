# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(85515)

except ImportError:
    pass
student_data1 = _c_(85518, _a_(85517, _n_(85516, "pd", lambda: pd), "DataFrame"), {'student_id': ['S1', 'S2', 'S3', 'S4', 'S5'], 'name': ['Danniella Fenton', 'Ryder Storey', 'Bryce Jensen', 'Ed Bernal', 'Kwame Morin'], 'marks': [200, 210, 190, 222, 199]})
_l_(85519)
student_data2 = _c_(85522, _a_(85521, _n_(85520, "pd", lambda: pd), "DataFrame"), {'student_id': ['S4', 'S5', 'S6', 'S7', 'S8'], 'name': ['Scarlette Fisher', 'Carla Williamson', 'Dante Morse', 'Kaiser William', 'Madeeha Preston'], 'marks': [201, 200, 198, 219, 201]})
_l_(85523)
_c_(85525, _n_(85524, "print", lambda: print), 'Original DataFrames:')
_l_(85526)
_c_(85529, _n_(85527, "print", lambda: print), _n_(85528, "student_data1", lambda: student_data1))
_l_(85530)
_c_(85533, _n_(85531, "print", lambda: print), _n_(85532, "student_data2", lambda: student_data2))
_l_(85534)
_c_(85536, _n_(85535, "print", lambda: print), 'Merged data (outer join):')
_l_(85537)
_c_(85540, _n_(85538, "print", lambda: print), _n_(85539, "merged_data", lambda: merged_data))
_l_(85541)