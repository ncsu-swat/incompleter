# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(94615)

except ImportError:
    pass
student_data1 = _c_(94618, _a_(94617, _n_(94616, "pd", lambda: pd), "DataFrame"), {'student_id': ['S1', 'S2', 'S3', 'S4', 'S5'], 'name': ['Danniella Fenton', 'Ryder Storey', 'Bryce Jensen', 'Ed Bernal', 'Kwame Morin'], 'marks': [200, 210, 190, 222, 199]})
_l_(94619)
student_data2 = _c_(94622, _a_(94621, _n_(94620, "pd", lambda: pd), "DataFrame"), {'student_id': ['S4', 'S5', 'S6', 'S7', 'S8'], 'name': ['Scarlette Fisher', 'Carla Williamson', 'Dante Morse', 'Kaiser William', 'Madeeha Preston'], 'marks': [201, 200, 198, 219, 201]})
_l_(94623)
_c_(94625, _n_(94624, "print", lambda: print), 'Original DataFrames:')
_l_(94626)
_c_(94629, _n_(94627, "print", lambda: print), _n_(94628, "student_data1", lambda: student_data1))
_l_(94630)
_c_(94633, _n_(94631, "print", lambda: print), _n_(94632, "student_data2", lambda: student_data2))
_l_(94634)
_c_(94637, _n_(94635, "print", lambda: print), _n_(94636, "exam_data", lambda: exam_data))
_l_(94638)
_c_(94640, _n_(94639, "print", lambda: print), '\nJoin first two said dataframes along rows:')
_l_(94641)
result_data = _c_(94646, _a_(94643, _n_(94642, "pd", lambda: pd), "concat"), [_n_(94644, "student_data1", lambda: student_data1), _n_(94645, "student_data2", lambda: student_data2)])
_l_(94647)
_c_(94650, _n_(94648, "print", lambda: print), _n_(94649, "result_data", lambda: result_data))
_l_(94651)
_c_(94653, _n_(94652, "print", lambda: print), '\nNow join the said result_data and df_exam_data along student_id:')
_l_(94654)
final_merged_data = _c_(94659, _a_(94656, _n_(94655, "pd", lambda: pd), "merge"), _n_(94657, "result_data", lambda: result_data), _n_(94658, "exam_data", lambda: exam_data), on='student_id')
_l_(94660)
_c_(94663, _n_(94661, "print", lambda: print), _n_(94662, "final_merged_data", lambda: final_merged_data))
_l_(94664)