# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/37633031/attributeerror-list-object-has-no-attribute-items
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import json
    _l_(674345)

except ImportError:
    pass
try:
    from urllib.request import urlopen, Request
    _l_(674347)

except ImportError:
    pass
try:
    from urllib.parse import urlencode
    _l_(674349)

except ImportError:
    pass

def sTrackTemperature():
    _l_(674369)

    "Constantly Show an Output of the Track Temperature"
    _l_(674350)
    sDataRaw = _c_(674354, _n_(674351, "urlopen", lambda: urlopen), _c_(674353, _n_(674352, "Request", lambda: Request), "https://api.samsara.com/v1/sensors/temperature?access_token=", 518, [2]))
    _l_(674355)
    sDataParse = _c_(674360, _a_(674359, _c_(674358, _a_(674357, _n_(674356, "sDataRaw", lambda: sDataRaw), "read")), "decode"), 'utf-8')
    _l_(674361)
    sDataJson = _c_(674365, _a_(674363, _n_(674362, "json", lambda: json), "loads"), _n_(674364, "sDataParse", lambda: sDataParse))
    _l_(674366)
    aux = _n_(674367, "sDataJson", lambda: sDataJson)
    _l_(674368)
    return aux
_c_(674375, _n_(674370, "print", lambda: print), _c_(674374, _n_(674371, "str", lambda: str), _c_(674373, _n_(674372, "sTrackTemperature", lambda: sTrackTemperature))))
_l_(674376)