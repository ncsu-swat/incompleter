# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63287967/keep-getting-attributeerror-str-object-has-no-attribute-items
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
response = _c_(590066, _a_(590062, _n_(590061, "requests", lambda: requests), "request"), "GET", _n_(590063, "folder_url", lambda: folder_url), headers=_n_(590064, "headers", lambda: headers), data=_n_(590065, "payload", lambda: payload))
_l_(590067)
jsonResponse = _c_(590070, _a_(590069, _n_(590068, "response", lambda: response), "json"))
_l_(590071)

for key, value in _c_(590074, _a_(590073, _n_(590072, "jsonResponse", lambda: jsonResponse), "items")):
                _l_(590080)

                _c_(590078, _n_(590075, "print", lambda: print), _n_(590076, "key", lambda: key), ":", _n_(590077, "value", lambda: value))
                _l_(590079)

URL = _n_(590081, "jsonResponse", lambda: jsonResponse)["presignedUrl"]
_l_(590082)
processnum = _n_(590083, "jsonResponse", lambda: jsonResponse)["processId"]
_l_(590084)

assetupload = _c_(590089, _a_(590086, _n_(590085, "requests", lambda: requests), "request"), "PUT", _n_(590087, "URL", lambda: URL), headers='Content-Type: image/tiff', data=_n_(590088, "payload", lambda: payload))
_l_(590090)