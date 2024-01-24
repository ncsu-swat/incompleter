# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/47718604/typeerror-during-datashader-aggregate-creation-between-python-3-5-and-3-6-enviro
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
agg = _c_(683354, _n_(683335, "method", lambda: method), _a_(683337, _n_(683336, "self", lambda: self), "df")[(_a_(683339, _n_(683338, "self", lambda: self), "df")['time_position'] >= _n_(683340, "time_start", lambda: time_start)) & (_a_(683342, _n_(683341, "self", lambda: self), "df")['time_position'] <= _n_(683343, "time_end", lambda: time_end))
                                 | _c_(683347, _a_(683346, _a_(683345, _n_(683344, "self", lambda: self), "df")['time_position'], "isnull"))], _n_(683348, "x_field", lambda: x_field), _n_(683349, "y_field", lambda: y_field), _c_(683353, _a_(683351, _n_(683350, "ds", lambda: ds), "count_cat"), _n_(683352, "agg_field", lambda: agg_field)))
_l_(683355)