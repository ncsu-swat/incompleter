# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61955009/typeerror-not-all-arguments-converted-during-string-formatting-data-upload-to
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import time
    _l_(705647)

except ImportError:
    pass
try:
    import requests
    _l_(705649)

except ImportError:
    pass

temp = [12,13,14,15,16,17,18,19,12,10]
_l_(705650)
humi = [67,68,69,50,56,57,59,59,45,48]
_l_(705651)

for x in _c_(705653, _n_(705652, "range", lambda: range), 10):
    _l_(705670)

    _c_(705656, _n_(705654, "print", lambda: print), 'Uploading sample',_n_(705655, "x", lambda: x),'...')
    _l_(705657)
    resp=_c_(705664, _a_(705659, _n_(705658, "requests", lambda: requests), "get"), 'https://api.thingspeak.com/update?api_key=WTJJF5W2CL8IGT19&field1=0' %(_n_(705660, "temp", lambda: temp)[_n_(705661, "x", lambda: x)],_n_(705662, "humi", lambda: humi)[_n_(705663, "x", lambda: x)]))
    _l_(705665)
    _c_(705668, _a_(705667, _n_(705666, "time", lambda: time), "sleep"), 20)
    _l_(705669)