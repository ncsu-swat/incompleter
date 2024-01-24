# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/6541767/python-urllib-error-attributeerror-bytes-object-has-no-attribute-read
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import urllib.request
    _l_(405934)

except ImportError:
    pass
try:
    import json
    _l_(405936)

except ImportError:
    pass

response = _c_(405941, _a_(405940, _c_(405939, _a_(405938, _a_(405937, urllib, "request"), "urlopen"), 'http://www.reddit.com/r/all/top/.json'), "read"))
_l_(405942)
jsonResponse = _c_(405946, _a_(405944, _n_(405943, "json", lambda: json), "load"), _n_(405945, "response", lambda: response))
_l_(405947)

for child in _n_(405948, "jsonResponse", lambda: jsonResponse)['data']['children']:
    _l_(405953)

    _c_(405951, _n_(405949, "print", lambda: print), _n_(405950, "child", lambda: child)['data']['title'])
    _l_(405952)