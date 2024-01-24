# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59074293/my-script-has-the-answe-typeerror-module-object-is-not-callable-how-i-solve
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import time
    _l_(569656)

except ImportError:
    pass
try:
    import serial
    _l_(569658)

except ImportError:
    pass

ser = _c_(569661, _a_(569660, _n_(569659, "serial", lambda: serial), "Serial"), port='/dev/ttyUSB0',
    baudrate = 9600,
    parity=0,
    stopbits=1,
    bytesize=8,
    timeout=1
)
_l_(569662)

while 1:
    _l_(569679)

    _c_(569665, _a_(569664, _n_(569663, "ser", lambda: ser), "write"), b'A')
    _l_(569666)
    x=_c_(569669, _a_(569668, _n_(569667, "ser", lambda: ser), "readline"))
    _l_(569670)
    _c_(569673, _n_(569671, "print", lambda: print), _n_(569672, "x", lambda: x))
    _l_(569674)
    _c_(569677, _a_(569676, _n_(569675, "time", lambda: time), "sleep"), 1)
    _l_(569678)