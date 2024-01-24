# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61955009/typeerror-not-all-arguments-converted-during-string-formatting-data-upload-to
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import time
    _l_(697611)

except ImportError:
    pass
try:
    import requests
    _l_(697613)

except ImportError:
    pass

temp = [12,13,14,15,16,17,18,19,12,10]
_l_(697614)
humi = [67,68,69,50,56,57,59,59,45,48]
_l_(697615)

for x in _c_(697617, _n_(697616, "range", lambda: range), 10):
    _l_(697634)

    _c_(697620, _n_(697618, "print", lambda: print), 'Uploading sample',_n_(697619, "x", lambda: x),'...')
    _l_(697621)
    resp=_c_(697628, _a_(697623, _n_(697622, "requests", lambda: requests), "get"), 'https://api.thingspeak.com/update?api_key=WTJJF5W2CL8IGT19&field1=0' %(_n_(697624, "temp", lambda: temp)[_n_(697625, "x", lambda: x)],_n_(697626, "humi", lambda: humi)[_n_(697627, "x", lambda: x)]))
    _l_(697629)
    _c_(697632, _a_(697631, _n_(697630, "time", lambda: time), "sleep"), 20)
    _l_(697633)