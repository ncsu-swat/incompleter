# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51829791/typeerror-unicode-strings-are-not-supported-please-encode-to-bytes-%c3%bf
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from Adafruit_Thermal import *
    _l_(660837)

except ImportError:
    pass

printer = _c_(660839, _n_(660838, "Adafruit_Thermal", lambda: Adafruit_Thermal), "/dev/serial0", 19200, timeout=5)    
_l_(660840)    