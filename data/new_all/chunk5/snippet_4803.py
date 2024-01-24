# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/47718604/typeerror-during-datashader-aggregate-creation-between-python-3-5-and-3-6-enviro
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
agg = _c_(671434, _n_(671415, "method", lambda: method), _a_(671417, _n_(671416, "self", lambda: self), "df")[(_a_(671419, _n_(671418, "self", lambda: self), "df")['time_position'] >= _n_(671420, "time_start", lambda: time_start)) & (_a_(671422, _n_(671421, "self", lambda: self), "df")['time_position'] <= _n_(671423, "time_end", lambda: time_end))
                                 | _c_(671427, _a_(671426, _a_(671425, _n_(671424, "self", lambda: self), "df")['time_position'], "isnull"))], _n_(671428, "x_field", lambda: x_field), _n_(671429, "y_field", lambda: y_field), _c_(671433, _a_(671431, _n_(671430, "ds", lambda: ds), "count_cat"), _n_(671432, "agg_field", lambda: agg_field)))
_l_(671435)