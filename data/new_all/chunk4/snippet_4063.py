# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63287967/keep-getting-attributeerror-str-object-has-no-attribute-items
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
response = _c_(626764, _a_(626760, _n_(626759, "requests", lambda: requests), "request"), "GET", _n_(626761, "folder_url", lambda: folder_url), headers=_n_(626762, "headers", lambda: headers), data=_n_(626763, "payload", lambda: payload))
_l_(626765)
jsonResponse = _c_(626768, _a_(626767, _n_(626766, "response", lambda: response), "json"))
_l_(626769)

for key, value in _c_(626772, _a_(626771, _n_(626770, "jsonResponse", lambda: jsonResponse), "items")):
                _l_(626778)

                _c_(626776, _n_(626773, "print", lambda: print), _n_(626774, "key", lambda: key), ":", _n_(626775, "value", lambda: value))
                _l_(626777)

URL = _n_(626779, "jsonResponse", lambda: jsonResponse)["presignedUrl"]
_l_(626780)
processnum = _n_(626781, "jsonResponse", lambda: jsonResponse)["processId"]
_l_(626782)

assetupload = _c_(626787, _a_(626784, _n_(626783, "requests", lambda: requests), "request"), "PUT", _n_(626785, "URL", lambda: URL), headers='Content-Type: image/tiff', data=_n_(626786, "payload", lambda: payload))
_l_(626788)