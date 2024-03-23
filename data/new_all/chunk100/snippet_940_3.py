# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(94766)

except ImportError:
    pass
student_data1 = _c_(94769, _a_(94768, _n_(94767, "pd", lambda: pd), "DataFrame"), {'student_id': ['S1', 'S2', 'S3', 'S4', 'S5'], 'name': ['Danniella Fenton', 'Ryder Storey', 'Bryce Jensen', 'Ed Bernal', 'Kwame Morin'], 'marks': [200, 210, 190, 222, 199]})
_l_(94770)
student_data2 = _c_(94773, _a_(94772, _n_(94771, "pd", lambda: pd), "DataFrame"), {'student_id': ['S4', 'S5', 'S6', 'S7', 'S8'], 'name': ['Scarlette Fisher', 'Carla Williamson', 'Dante Morse', 'Kaiser William', 'Madeeha Preston'], 'marks': [201, 200, 198, 219, 201]})
_l_(94774)
exam_data = _c_(94777, _a_(94776, _n_(94775, "pd", lambda: pd), "DataFrame"), {'student_id': ['S1', 'S2', 'S3', 'S4', 'S5', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13'], 'exam_id': [23, 45, 12, 67, 21, 55, 33, 14, 56, 83, 88, 12]})
_l_(94778)
_c_(94780, _n_(94779, "print", lambda: print), 'Original DataFrames:')
_l_(94781)
_c_(94784, _n_(94782, "print", lambda: print), _n_(94783, "student_data1", lambda: student_data1))
_l_(94785)
_c_(94788, _n_(94786, "print", lambda: print), _n_(94787, "student_data2", lambda: student_data2))
_l_(94789)
_c_(94792, _n_(94790, "print", lambda: print), _n_(94791, "exam_data", lambda: exam_data))
_l_(94793)
_c_(94795, _n_(94794, "print", lambda: print), '\nJoin first two said dataframes along rows:')
_l_(94796)
_c_(94799, _n_(94797, "print", lambda: print), _n_(94798, "result_data", lambda: result_data))
_l_(94800)
_c_(94802, _n_(94801, "print", lambda: print), '\nNow join the said result_data and df_exam_data along student_id:')
_l_(94803)
final_merged_data = _c_(94808, _a_(94805, _n_(94804, "pd", lambda: pd), "merge"), _n_(94806, "result_data", lambda: result_data), _n_(94807, "exam_data", lambda: exam_data), on='student_id')
_l_(94809)
_c_(94812, _n_(94810, "print", lambda: print), _n_(94811, "final_merged_data", lambda: final_merged_data))
_l_(94813)