# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73888842/error-on-code-typeerror-not-supported-between-instances-of-nonetype-and
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import RPi.GPIO as GPIO
    _l_(634420)

except ImportError:
    pass
try:
    import Adafruit_DHT
    _l_(634422)

except ImportError:
    pass
try:
    import time
    _l_(634424)

except ImportError:
    pass

_c_(634427, _a_(634426, _n_(634425, "GPIO", lambda: GPIO), "setwarnings"), False)
_l_(634428)
_c_(634433, _a_(634430, _n_(634429, "GPIO", lambda: GPIO), "setmode"), _a_(634432, _n_(634431, "GPIO", lambda: GPIO), "BCM"))
_l_(634434)
_c_(634439, _a_(634436, _n_(634435, "GPIO", lambda: GPIO), "setup"), 22, _a_(634438, _n_(634437, "GPIO", lambda: GPIO), "OUT"))
_l_(634440)


SENSOR_DHT = _a_(634442, _n_(634441, "Adafruit_DHT", lambda: Adafruit_DHT), "DHT22")
_l_(634443)
PIN_DHT = 17
_l_(634444)
PIN_LED = 22
_l_(634445)


while True:
    _l_(634483)

    humedad, temperatura = _c_(634450, _a_(634447, _n_(634446, "Adafruit_DHT", lambda: Adafruit_DHT), "read"), _n_(634448, "SENSOR_DHT", lambda: SENSOR_DHT), _n_(634449, "PIN_DHT", lambda: PIN_DHT))
    _l_(634451)
    if _n_(634452, "humedad", lambda: humedad) is not None and _n_(634453, "temperatura", lambda: temperatura) is not None:
        _l_(634468)

        _c_(634459, _n_(634454, "print", lambda: print), _c_(634458, _a_(634455, "Temp={0:0.1f}%C Hum={1:0.1f}%", "format"), _n_(634456, "temperatura", lambda: temperatura), _n_(634457, "humedad", lambda: humedad)))
        _l_(634460)
        _c_(634463, _n_(634461, "print", lambda: print), _n_(634462, "temperatura", lambda: temperatura))
        _l_(634464)
    else:
        _c_(634466, _n_(634465, "print", lambda: print), "Falla en la lectura. Revisar el circuito");
        _l_(634467)
    _c_(634471, _a_(634470, _n_(634469, "time", lambda: time), "sleep"), 0.5);
    _l_(634472)
    

    if _n_(634473, "temperatura", lambda: temperatura) > 28:
        _l_(634482)

        _c_(634476, _a_(634475, _n_(634474, "GPIO", lambda: GPIO), "output"), 22,1)
        _l_(634477)
    else:
        _c_(634480, _a_(634479, _n_(634478, "GPIO", lambda: GPIO), "output"), 22,0)
        _l_(634481)