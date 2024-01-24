# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57599957/attributeerror-serialbus-object-has-no-attribute-can
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from can.interfaces import serial
    _l_(656104)

except ImportError:
    pass
try:
    import random
    _l_(656106)

except ImportError:
    pass
try:
    import time
    _l_(656108)

except ImportError:
    pass
try:
    import datetime
    _l_(656110)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(656112)

except ImportError:
    pass

ser= _c_(656118, _a_(656117, _a_(656116, _a_(656115, _a_(656114, _n_(656113, "can", lambda: can), "interfaces"), "serial"), "serial_can"), "SerialBus"), 'COM5',115200,timeout=None,rtscts=0)
_l_(656119)

for i in _c_(656121, _n_(656120, "range", lambda: range), 100) :
    _l_(656134)

    s= _c_(656128, _a_(656127, _a_(656126, _a_(656125, _a_(656124, _a_(656123, _n_(656122, "ser", lambda: ser), "can"), "interfaces"), "serial"), "SerialBus"), "_recv_internal"), timeout=None)
    _l_(656129)
    _c_(656132, _n_(656130, "print", lambda: print), _n_(656131, "s", lambda: s))
    _l_(656133)