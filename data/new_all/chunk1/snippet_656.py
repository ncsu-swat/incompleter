# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68088826/python-writing-avro-timestamp-millis-datum-astimezonetz-timezones-utc-attribu
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
writer = _c_(390783, _a_(390781, _a_(390780, _n_(390779, "avro", lambda: avro), "io"), "DatumWriter"), _n_(390782, "schema", lambda: schema))
_l_(390784)
bytes_writer = _c_(390787, _a_(390786, _n_(390785, "io", lambda: io), "BytesIO"))
_l_(390788)
encoder = _c_(390793, _a_(390791, _a_(390790, _n_(390789, "avro", lambda: avro), "io"), "BinaryEncoder"), _n_(390792, "bytes_writer", lambda: bytes_writer))
_l_(390794)
_c_(390800, _a_(390796, _n_(390795, "writer", lambda: writer), "write"), _c_(390798, _n_(390797, "get_dict", lambda: get_dict)), _n_(390799, "encoder", lambda: encoder)) #----------Exception here
_l_(390801) #----------Exception here
raw_bytes = _c_(390804, _a_(390803, _n_(390802, "bytes_writer", lambda: bytes_writer), "getvalue"))
_l_(390805)