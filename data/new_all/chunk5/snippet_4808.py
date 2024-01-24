# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/47718604/typeerror-during-datashader-aggregate-creation-between-python-3-5-and-3-6-enviro
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
agg = _c_(652802, _n_(652783, "method", lambda: method), _a_(652785, _n_(652784, "self", lambda: self), "df")[(_a_(652787, _n_(652786, "self", lambda: self), "df")['time_position'] >= _n_(652788, "time_start", lambda: time_start)) & (_a_(652790, _n_(652789, "self", lambda: self), "df")['time_position'] <= _n_(652791, "time_end", lambda: time_end))
                                 | _c_(652795, _a_(652794, _a_(652793, _n_(652792, "self", lambda: self), "df")['time_position'], "isnull"))], _n_(652796, "x_field", lambda: x_field), _n_(652797, "y_field", lambda: y_field), _c_(652801, _a_(652799, _n_(652798, "ds", lambda: ds), "count_cat"), _n_(652800, "agg_field", lambda: agg_field)))
_l_(652803)