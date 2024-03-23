# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(94815)

except ImportError:
    pass
student_data2 = _c_(94818, _a_(94817, _n_(94816, "pd", lambda: pd), "DataFrame"), {'student_id': ['S4', 'S5', 'S6', 'S7', 'S8'], 'name': ['Scarlette Fisher', 'Carla Williamson', 'Dante Morse', 'Kaiser William', 'Madeeha Preston'], 'marks': [201, 200, 198, 219, 201]})
_l_(94819)
exam_data = _c_(94822, _a_(94821, _n_(94820, "pd", lambda: pd), "DataFrame"), {'student_id': ['S1', 'S2', 'S3', 'S4', 'S5', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13'], 'exam_id': [23, 45, 12, 67, 21, 55, 33, 14, 56, 83, 88, 12]})
_l_(94823)
_c_(94825, _n_(94824, "print", lambda: print), 'Original DataFrames:')
_l_(94826)
_c_(94829, _n_(94827, "print", lambda: print), _n_(94828, "student_data1", lambda: student_data1))
_l_(94830)
_c_(94833, _n_(94831, "print", lambda: print), _n_(94832, "student_data2", lambda: student_data2))
_l_(94834)
_c_(94837, _n_(94835, "print", lambda: print), _n_(94836, "exam_data", lambda: exam_data))
_l_(94838)
_c_(94840, _n_(94839, "print", lambda: print), '\nJoin first two said dataframes along rows:')
_l_(94841)
result_data = _c_(94846, _a_(94843, _n_(94842, "pd", lambda: pd), "concat"), [_n_(94844, "student_data1", lambda: student_data1), _n_(94845, "student_data2", lambda: student_data2)])
_l_(94847)
_c_(94850, _n_(94848, "print", lambda: print), _n_(94849, "result_data", lambda: result_data))
_l_(94851)
_c_(94853, _n_(94852, "print", lambda: print), '\nNow join the said result_data and df_exam_data along student_id:')
_l_(94854)
final_merged_data = _c_(94859, _a_(94856, _n_(94855, "pd", lambda: pd), "merge"), _n_(94857, "result_data", lambda: result_data), _n_(94858, "exam_data", lambda: exam_data), on='student_id')
_l_(94860)
_c_(94863, _n_(94861, "print", lambda: print), _n_(94862, "final_merged_data", lambda: final_merged_data))
_l_(94864)