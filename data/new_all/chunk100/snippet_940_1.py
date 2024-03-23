# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(94666)

except ImportError:
    pass
student_data1 = _c_(94669, _a_(94668, _n_(94667, "pd", lambda: pd), "DataFrame"), {'student_id': ['S1', 'S2', 'S3', 'S4', 'S5'], 'name': ['Danniella Fenton', 'Ryder Storey', 'Bryce Jensen', 'Ed Bernal', 'Kwame Morin'], 'marks': [200, 210, 190, 222, 199]})
_l_(94670)
student_data2 = _c_(94673, _a_(94672, _n_(94671, "pd", lambda: pd), "DataFrame"), {'student_id': ['S4', 'S5', 'S6', 'S7', 'S8'], 'name': ['Scarlette Fisher', 'Carla Williamson', 'Dante Morse', 'Kaiser William', 'Madeeha Preston'], 'marks': [201, 200, 198, 219, 201]})
_l_(94674)
exam_data = _c_(94677, _a_(94676, _n_(94675, "pd", lambda: pd), "DataFrame"), {'student_id': ['S1', 'S2', 'S3', 'S4', 'S5', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13'], 'exam_id': [23, 45, 12, 67, 21, 55, 33, 14, 56, 83, 88, 12]})
_l_(94678)
_c_(94680, _n_(94679, "print", lambda: print), 'Original DataFrames:')
_l_(94681)
_c_(94684, _n_(94682, "print", lambda: print), _n_(94683, "student_data1", lambda: student_data1))
_l_(94685)
_c_(94688, _n_(94686, "print", lambda: print), _n_(94687, "student_data2", lambda: student_data2))
_l_(94689)
_c_(94692, _n_(94690, "print", lambda: print), _n_(94691, "exam_data", lambda: exam_data))
_l_(94693)
_c_(94695, _n_(94694, "print", lambda: print), '\nJoin first two said dataframes along rows:')
_l_(94696)
result_data = _c_(94701, _a_(94698, _n_(94697, "pd", lambda: pd), "concat"), [_n_(94699, "student_data1", lambda: student_data1), _n_(94700, "student_data2", lambda: student_data2)])
_l_(94702)
_c_(94705, _n_(94703, "print", lambda: print), _n_(94704, "result_data", lambda: result_data))
_l_(94706)
_c_(94708, _n_(94707, "print", lambda: print), '\nNow join the said result_data and df_exam_data along student_id:')
_l_(94709)
_c_(94712, _n_(94710, "print", lambda: print), _n_(94711, "final_merged_data", lambda: final_merged_data))
_l_(94713)