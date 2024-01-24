# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/47055600/how-to-convert-to-bytes-when-typeerror-cant-concat-bytes-to-str
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import http.client
    _l_(382404)

except ImportError:
    pass

conn = _c_(382407, _a_(382406, _a_(382405, http, "client"), "HTTPSConnection"), "exampleurl.com")
_l_(382408)

payload = {
    'FilterId': "63G8Tg4LWfWjW84Qy0usld5i0f",
    'name': "Test",
    'description': "Test1",
    'deadline': "2017-12-31",
    'exclusionRuleName': "Exclude",
    'disable': "true",
    'type': "Type1"
    }
_l_(382409)

headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'x-csrf-token': "wWjeFkMcbopci1TK2cibZ2hczI",
    'cache-control': "no-cache",
    'postman-token': "23c09c76-3b030-eea1-e16ffd48e9"
    }
_l_(382410)


_c_(382415, _a_(382412, _n_(382411, "conn", lambda: conn), "request"), "POST", "/api/campaign/create", _n_(382413, "payload", lambda: payload), _n_(382414, "headers", lambda: headers))
_l_(382416)


res = _c_(382419, _a_(382418, _n_(382417, "conn", lambda: conn), "getresponse"))
_l_(382420)
data = _c_(382423, _a_(382422, _n_(382421, "res", lambda: res), "read"))
_l_(382424)

_c_(382429, _n_(382425, "print", lambda: print), _c_(382428, _a_(382427, _n_(382426, "data", lambda: data), "decode"), "utf-8"))
_l_(382430)