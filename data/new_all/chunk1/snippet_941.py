# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72849402/api-error-typeerror-string-indices-must-be-integers
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import json
    _l_(395716)

except ImportError:
    pass
try:
    import requests
    _l_(395718)

except ImportError:
    pass
try:
    import configuration
    _l_(395720)

except ImportError:
    pass
url = 'https://client.blutudlut.xyz/api/application/servers'
_l_(395721)
headers = {
    "Authorization": "Bearer "+ _a_(395723, _n_(395722, "configuration", lambda: configuration), "pterodactyl_admin_api"),
    "Accept": "application/json",
    "Content-Type": "application/json",
}
_l_(395724)

response = _c_(395729, _a_(395726, _n_(395725, "requests", lambda: requests), "request"), 'GET', _n_(395727, "url", lambda: url), headers=_n_(395728, "headers", lambda: headers))
_l_(395730)
_c_(395734, _n_(395731, "print", lambda: print), _a_(395733, _n_(395732, "response", lambda: response), "text"))
_l_(395735)
json_str = _c_(395740, _a_(395737, _n_(395736, "json", lambda: json), "dumps"), _a_(395739, _n_(395738, "response", lambda: response), "text"))
_l_(395741)
resp = _c_(395745, _a_(395743, _n_(395742, "json", lambda: json), "loads"), _n_(395744, "json_str", lambda: json_str))
_l_(395746)
_c_(395749, _n_(395747, "print", lambda: print), _n_(395748, "resp", lambda: resp))
_l_(395750)
_c_(395753, _n_(395751, "print", lambda: print), _n_(395752, "resp", lambda: resp)['data'])
_l_(395754)