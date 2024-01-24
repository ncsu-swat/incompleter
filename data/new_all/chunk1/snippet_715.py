# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50104197/pandas-erratically-returning-typeerror-cannot-do-slice-indexing-on-class-panda
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
col_names = ['Col_' + _c_(396695, _n_(396693, "str", lambda: str), _n_(396694, "i", lambda: i)) for i in _c_(396698, _n_(396696, "range", lambda: range), 1, _n_(396697, "max_col_nr", lambda: max_col_nr))]
_l_(396699)

df = _c_(396704, _a_(396701, _n_(396700, "pd", lambda: pd), "read_csv"), _n_(396702, "myFile", lambda: myFile), sep = '\t', names = _n_(396703, "col_names", lambda: col_names))
_l_(396705)
df2 = _c_(396708, _a_(396707, _n_(396706, "df", lambda: df), "set_index"), "Col_2", drop = False)
_l_(396709)
df3 = (_a_(396711, _n_(396710, "df2", lambda: df2), "loc")[310:400,"Col_4"])
_l_(396712)
US_Av = _c_(396719, _n_(396713, "int", lambda: int), _c_(396718, _n_(396714, "round", lambda: round), _c_(396717, _a_(396716, _n_(396715, "df4", lambda: df4), "mean"))))
_l_(396720)