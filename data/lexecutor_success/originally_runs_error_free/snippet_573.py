# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/7999935/python-datetime-to-string-without-microsecond-component
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import datetime
    _l_(1546467)

except ImportError:
    pass

date_generated = _c_(1546471, _a_(1546470, _a_(1546469, _n_(1546468, "datetime", lambda: datetime), "datetime"), "now"))
_l_(1546472)
_c_(1546479, _a_(1546478, _c_(1546477, _a_(1546476, _c_(1546475, _a_(1546474, _n_(1546473, "date_generated", lambda: date_generated), "replace"), microsecond=0), "isoformat"), ' '), "partition"), '+')[0]
_l_(1546480)

