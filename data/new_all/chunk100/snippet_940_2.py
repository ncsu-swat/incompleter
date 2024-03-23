# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(94715)

except ImportError:
    pass
student_data1 = _c_(94718, _a_(94717, _n_(94716, "pd", lambda: pd), "DataFrame"), {'student_id': ['S1', 'S2', 'S3', 'S4', 'S5'], 'name': ['Danniella Fenton', 'Ryder Storey', 'Bryce Jensen', 'Ed Bernal', 'Kwame Morin'], 'marks': [200, 210, 190, 222, 199]})
_l_(94719)
exam_data = _c_(94722, _a_(94721, _n_(94720, "pd", lambda: pd), "DataFrame"), {'student_id': ['S1', 'S2', 'S3', 'S4', 'S5', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13'], 'exam_id': [23, 45, 12, 67, 21, 55, 33, 14, 56, 83, 88, 12]})
_l_(94723)
_c_(94725, _n_(94724, "print", lambda: print), 'Original DataFrames:')
_l_(94726)
_c_(94729, _n_(94727, "print", lambda: print), _n_(94728, "student_data1", lambda: student_data1))
_l_(94730)
_c_(94733, _n_(94731, "print", lambda: print), _n_(94732, "student_data2", lambda: student_data2))
_l_(94734)
_c_(94737, _n_(94735, "print", lambda: print), _n_(94736, "exam_data", lambda: exam_data))
_l_(94738)
_c_(94740, _n_(94739, "print", lambda: print), '\nJoin first two said dataframes along rows:')
_l_(94741)
result_data = _c_(94746, _a_(94743, _n_(94742, "pd", lambda: pd), "concat"), [_n_(94744, "student_data1", lambda: student_data1), _n_(94745, "student_data2", lambda: student_data2)])
_l_(94747)
_c_(94750, _n_(94748, "print", lambda: print), _n_(94749, "result_data", lambda: result_data))
_l_(94751)
_c_(94753, _n_(94752, "print", lambda: print), '\nNow join the said result_data and df_exam_data along student_id:')
_l_(94754)
final_merged_data = _c_(94759, _a_(94756, _n_(94755, "pd", lambda: pd), "merge"), _n_(94757, "result_data", lambda: result_data), _n_(94758, "exam_data", lambda: exam_data), on='student_id')
_l_(94760)
_c_(94763, _n_(94761, "print", lambda: print), _n_(94762, "final_merged_data", lambda: final_merged_data))
_l_(94764)