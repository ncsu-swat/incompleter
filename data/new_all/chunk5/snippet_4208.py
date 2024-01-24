# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61632870/raspberrypi-typeerror-unsupported-format-string-passed-to-nonetype-format
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sys
    _l_(667928)

except ImportError:
    pass
try:
    import Adafruit_DHT
    _l_(667930)

except ImportError:
    pass
try:
    import time
    _l_(667932)

except ImportError:
    pass

while True:
    _l_(667944)


    humidity, temperature = _c_(667935, _a_(667934, _n_(667933, "Adafruit_DHT", lambda: Adafruit_DHT), "read_retry"), 11, 4)
    _l_(667936)

    _c_(667942, _n_(667937, "print", lambda: print), _c_(667941, _a_(667938, 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %', "format"), _n_(667939, "temperature", lambda: temperature), _n_(667940, "humidity", lambda: humidity)))
    _l_(667943)
   # print()
_c_(667947, _a_(667946, _n_(667945, "time", lambda: time), "sleep"), 1)
_l_(667948)