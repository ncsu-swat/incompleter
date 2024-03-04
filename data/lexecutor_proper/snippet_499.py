# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/2150739/iso-time-iso-8601-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
tz = _c_(63309, _a_(63304, _n_(63303, "str", lambda: str), "format"), '{0:+06.2f}', _c_(63308, _n_(63305, "float", lambda: float), _a_(63307, _n_(63306, "time", lambda: time), "altzone")) / 3600)
_l_(63310)

tz = _c_(63317, _a_(63312, _n_(63311, "str", lambda: str), "format"), '{0:+06.2f}', -_c_(63316, _n_(63313, "float", lambda: float), _a_(63315, _n_(63314, "time", lambda: time), "altzone")) / 3600)
_l_(63318)

