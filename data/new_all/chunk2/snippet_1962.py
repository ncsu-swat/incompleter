# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75174299/pyflink-sliding-window-on-a-datastream-fails-with-attributeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
input_stream = _c_(430715, _a_(430713, _a_(430712, _n_(430711, "self", lambda: self), "table_env"), "to_data_stream"), _n_(430714, "flat_table", lambda: flat_table))
_l_(430716)
result_stream = _c_(430760, _a_(430730, _c_(430729, _a_(430721, _c_(430720, _a_(430718, _n_(430717, "input_stream", lambda: input_stream), "key_by"), _n_(430719, "get_key", lambda: get_key)), "window"), _c_(430728, _a_(430723, _n_(430722, "CountSlidingWindowAssigner", lambda: CountSlidingWindowAssigner), "of"), _a_(430725, _n_(430724, "self", lambda: self), "window_size"), _a_(430727, _n_(430726, "self", lambda: self), "window_slide"))), "apply"), _c_(430732, _n_(430731, "MyWindowFunction", lambda: MyWindowFunction)),
           output_type=_c_(430759, _a_(430734, _n_(430733, "Types", lambda: Types), "TUPLE"), [_c_(430737, _a_(430736, _n_(430735, "Types", lambda: Types), "STRING")), _c_(430740, _a_(430739, _n_(430738, "Types", lambda: Types), "STRING")), _c_(430743, _a_(430742, _n_(430741, "Types", lambda: Types), "STRING")), _c_(430746, _a_(430745, _n_(430744, "Types", lambda: Types), "STRING")), _c_(430749, _a_(430748, _n_(430747, "Types", lambda: Types), "STRING")), _c_(430752, _a_(430751, _n_(430750, "Types", lambda: Types), "FLOAT")), _c_(430755, _a_(430754, _n_(430753, "Types", lambda: Types), "FLOAT")), _c_(430758, _a_(430757, _n_(430756, "Types", lambda: Types), "FLOAT"))]))
_l_(430761)