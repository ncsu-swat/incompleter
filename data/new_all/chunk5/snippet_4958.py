# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/37633031/attributeerror-list-object-has-no-attribute-items
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import json
    _l_(649673)

except ImportError:
    pass
try:
    from urllib.request import urlopen, Request
    _l_(649675)

except ImportError:
    pass
try:
    from urllib.parse import urlencode
    _l_(649677)

except ImportError:
    pass

def sTrackTemperature():
    _l_(649699)

    "Constantly Show an Output of the Track Temperature"
    _l_(649678)
    SENSOR = {'SENSOR': '2'}
    _l_(649679)
    sDataRaw = _c_(649684, _n_(649680, "urlopen", lambda: urlopen), _c_(649683, _n_(649681, "Request", lambda: Request), "https://api.samsara.com/v1/sensors/temperature?access_token=****************", 518, _n_(649682, "SENSOR", lambda: SENSOR)['SENSOR']))
    _l_(649685)
    sDataParse = _c_(649690, _a_(649689, _c_(649688, _a_(649687, _n_(649686, "sDataRaw", lambda: sDataRaw), "read")), "decode"), 'utf-8')
    _l_(649691)
    sDataJson = _c_(649695, _a_(649693, _n_(649692, "json", lambda: json), "loads"), _n_(649694, "sDataParse", lambda: sDataParse))
    _l_(649696)
    aux = _n_(649697, "sDataJson", lambda: sDataJson)
    _l_(649698)
    return aux
_c_(649705, _n_(649700, "print", lambda: print), _c_(649704, _n_(649701, "str", lambda: str), _c_(649703, _n_(649702, "sTrackTemperature", lambda: sTrackTemperature))))
_l_(649706)