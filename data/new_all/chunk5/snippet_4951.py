# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/37633031/attributeerror-list-object-has-no-attribute-items
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import json
    _l_(693221)

except ImportError:
    pass
try:
    from urllib.request import urlopen, Request
    _l_(693223)

except ImportError:
    pass
try:
    from urllib.parse import urlencode
    _l_(693225)

except ImportError:
    pass

def sTrackTemperature():
    _l_(693245)

    "Constantly Show an Output of the Track Temperature"
    _l_(693226)
    sDataRaw = _c_(693230, _n_(693227, "urlopen", lambda: urlopen), _c_(693229, _n_(693228, "Request", lambda: Request), "https://api.samsara.com/v1/sensors/temperature?access_token=", 518, [2]))
    _l_(693231)
    sDataParse = _c_(693236, _a_(693235, _c_(693234, _a_(693233, _n_(693232, "sDataRaw", lambda: sDataRaw), "read")), "decode"), 'utf-8')
    _l_(693237)
    sDataJson = _c_(693241, _a_(693239, _n_(693238, "json", lambda: json), "loads"), _n_(693240, "sDataParse", lambda: sDataParse))
    _l_(693242)
    aux = _n_(693243, "sDataJson", lambda: sDataJson)
    _l_(693244)
    return aux
_c_(693251, _n_(693246, "print", lambda: print), _c_(693250, _n_(693247, "str", lambda: str), _c_(693249, _n_(693248, "sTrackTemperature", lambda: sTrackTemperature))))
_l_(693252)