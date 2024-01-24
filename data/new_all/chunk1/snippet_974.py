# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60649173/numpy-typeerror-ufunc-bitwise-and-not-supported-for-the-input-types
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
condition = [((_n_(386724, "df_merge", lambda: df_merge)['column1'] == 'a') & (_n_(386725, "df_merge", lambda: df_merge)['column2'] == _c_(386729, _a_(386727, _n_(386726, "df_merge", lambda: df_merge)['column2'], "isin"), _n_(386728, "bb", lambda: bb)))),((_n_(386730, "df_merge", lambda: df_merge)['column1'] == 'c') & (_n_(386731, "df_merge", lambda: df_merge)['column2'] == _c_(386735, _a_(386733, _n_(386732, "df_merge", lambda: df_merge)['column2'], "isin"), _n_(386734, "dd", lambda: dd)))), ((_n_(386736, "df_merge", lambda: df_merge)['column1'] == 'e') & (_n_(386737, "df_merge", lambda: df_merge)['column2'] == _c_(386741, _a_(386739, _n_(386738, "df_merge", lambda: df_merge)['column2'], "isin"), _n_(386740, "ff", lambda: ff))))]
_l_(386742)

choices1 = [(_c_(386746, _a_(386744, _n_(386743, "np", lambda: np), "where"), _n_(386745, "df_merge", lambda: df_merge)['column3'] >= 1, 'should not have, ','correct') & _c_(386750, _a_(386748, _n_(386747, "np", lambda: np), "where"), _n_(386749, "df_merge", lambda: df_merge)['column4'] >= 0.45, 'should not have, ','correct'))]
_l_(386751)

_n_(386752, "df_merge", lambda: df_merge)['Reason'] = _c_(386757, _a_(386754, _n_(386753, "np", lambda: np), "select"), _n_(386755, "condition", lambda: condition), _n_(386756, "choices1", lambda: choices1), default='correct')
_l_(386758)