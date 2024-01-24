# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72708057/typeerror-unsupported-operand-types-for-float-and-datetimearray
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
start_date = r'12/12/1984'
_l_(361471)
end_date = r'12/12/1986'
_l_(361472)

date1 = _c_(361482, _a_(361474, _n_(361473, "time", lambda: time), "mktime"), _c_(361481, _a_(361480, _c_(361479, _a_(361477, _a_(361476, _n_(361475, "datetime", lambda: datetime), "datetime"), "strptime"), _n_(361478, "start_date", lambda: start_date), "%m/%d/%Y"), "timetuple")))
_l_(361483)
date2 = _c_(361493, _a_(361485, _n_(361484, "time", lambda: time), "mktime"), _c_(361492, _a_(361491, _c_(361490, _a_(361488, _a_(361487, _n_(361486, "datetime", lambda: datetime), "datetime"), "strptime"), _n_(361489, "end_date", lambda: end_date), "%m/%d/%Y"), "timetuple")))
_l_(361494)

df = _n_(361495, "df", lambda: df)[_n_(361496, "df", lambda: df)['CreatedDate'] > _n_(361497, "date1", lambda: date1) & _n_(361498, "df", lambda: df)['CreatedDate'] <= _n_(361499, "date2", lambda: date2) ]
_l_(361500)