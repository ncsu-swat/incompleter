# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54735075/typeerror-a-bytes-like-object-is-required-not-str-when-using-rest-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import requests, base64
    _l_(422297)

except ImportError:
    pass

usrPass = "user:pass"
_l_(422298)
b64Val = _c_(422302, _a_(422300, _n_(422299, "base64", lambda: base64), "b64encode"), _n_(422301, "usrPass", lambda: usrPass))
_l_(422303)
api_URL = 'api-url'
_l_(422304)
r=_c_(422310, _a_(422306, _n_(422305, "requests", lambda: requests), "post"), _n_(422307, "api_URL", lambda: api_URL), 
                headers={"Authorization": "Basic %s" % _n_(422308, "b64Val", lambda: b64Val)},
                data=_n_(422309, "payload", lambda: payload))
_l_(422311)