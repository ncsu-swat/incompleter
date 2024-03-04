# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/2474015/getting-the-index-of-the-returned-max-or-min-item-using-max-min-on-a-list
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
min_value = _c_(62854, _n_(62852, "min", lambda: min), _n_(62853, "values", lambda: values))
_l_(62855)
indexes_with_min_value = [_n_(62856, "i", lambda: i) for i in _c_(62861, _n_(62857, "range", lambda: range), 0,_c_(62860, _n_(62858, "len", lambda: len), _n_(62859, "values", lambda: values))) if _n_(62862, "values", lambda: values)[_n_(62863, "i", lambda: i)] == _n_(62864, "min_value", lambda: min_value)]
_l_(62865)

choosen = _n_(62866, "indexes_with_min_value", lambda: indexes_with_min_value)[0]
_l_(62867)

