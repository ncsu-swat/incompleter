# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/37633031/attributeerror-list-object-has-no-attribute-items
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import json
    _l_(664304)

except ImportError:
    pass
try:
    from urllib.request import urlopen, Request
    _l_(664306)

except ImportError:
    pass
try:
    from urllib.parse import urlencode
    _l_(664308)

except ImportError:
    pass

def sTrackTemperature():
    _l_(664330)

    "Constantly Show an Output of the Track Temperature"
    _l_(664309)
    SENSOR = {'SENSOR': '2'}
    _l_(664310)
    sDataRaw = _c_(664315, _n_(664311, "urlopen", lambda: urlopen), _c_(664314, _n_(664312, "Request", lambda: Request), "https://api.samsara.com/v1/sensors/temperature?access_token=****************", 518, _n_(664313, "SENSOR", lambda: SENSOR)['SENSOR']))
    _l_(664316)
    sDataParse = _c_(664321, _a_(664320, _c_(664319, _a_(664318, _n_(664317, "sDataRaw", lambda: sDataRaw), "read")), "decode"), 'utf-8')
    _l_(664322)
    sDataJson = _c_(664326, _a_(664324, _n_(664323, "json", lambda: json), "loads"), _n_(664325, "sDataParse", lambda: sDataParse))
    _l_(664327)
    aux = _n_(664328, "sDataJson", lambda: sDataJson)
    _l_(664329)
    return aux
_c_(664336, _n_(664331, "print", lambda: print), _c_(664335, _n_(664332, "str", lambda: str), _c_(664334, _n_(664333, "sTrackTemperature", lambda: sTrackTemperature))))
_l_(664337)