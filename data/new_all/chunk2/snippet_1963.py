# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75174299/pyflink-sliding-window-on-a-datastream-fails-with-attributeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
input_stream = _c_(427009, _a_(427007, _a_(427006, _n_(427005, "self", lambda: self), "table_env"), "to_data_stream"), _n_(427008, "flat_table", lambda: flat_table))
_l_(427010)
result_stream = _c_(427053, _a_(427023, _c_(427022, _a_(427015, _c_(427014, _a_(427012, _n_(427011, "input_stream", lambda: input_stream), "key_by"), _n_(427013, "get_key", lambda: get_key)), "window"), _c_(427021, _n_(427016, "CountSlidingWindowAssigner", lambda: CountSlidingWindowAssigner), _a_(427018, _n_(427017, "self", lambda: self), "window_size"), _a_(427020, _n_(427019, "self", lambda: self), "window_slide"))), "apply"), _c_(427025, _n_(427024, "CTATThresholds", lambda: CTATThresholds)),
           result_type=_c_(427052, _a_(427027, _n_(427026, "Types", lambda: Types), "TUPLE"), [_c_(427030, _a_(427029, _n_(427028, "Types", lambda: Types), "STRING")), _c_(427033, _a_(427032, _n_(427031, "Types", lambda: Types), "STRING")), _c_(427036, _a_(427035, _n_(427034, "Types", lambda: Types), "STRING")), _c_(427039, _a_(427038, _n_(427037, "Types", lambda: Types), "STRING")),
                                    _c_(427042, _a_(427041, _n_(427040, "Types", lambda: Types), "STRING")), _c_(427045, _a_(427044, _n_(427043, "Types", lambda: Types), "FLOAT")), _c_(427048, _a_(427047, _n_(427046, "Types", lambda: Types), "FLOAT")), _c_(427051, _a_(427050, _n_(427049, "Types", lambda: Types), "FLOAT"))]))
_l_(427054)