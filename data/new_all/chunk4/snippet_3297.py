# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75106915/error-pyflink-fn-execution-coder-impl-fast-intcoderimpl-encode-to-stream-typee
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
ds = _c_(615922, _a_(615920, _n_(615919, "stream_env", lambda: stream_env), "add_source"), _n_(615921, "kafka_source", lambda: kafka_source), 'Kafka_Source')
_l_(615923)

ds = _c_(615933, _a_(615932, _c_(615931, _a_(615925, _n_(615924, "ds", lambda: ds), "map"), _n_(615926, "transform_user_event_data", lambda: transform_user_event_data),
            _c_(615930, _a_(615929, _c_(615928, _n_(615927, "BaseEventSchema", lambda: BaseEventSchema)), "get_type_info"))), "name"), 'Transform_Data')
_l_(615934)

# ds.print()

_c_(615939, _a_(615936, _n_(615935, "stream_env", lambda: stream_env), "execute"), _a_(615938, _n_(615937, "cfg", lambda: cfg), "JOB_NAME"))   
_l_(615940)   