# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/30760728/python-3-urllib-produces-typeerror-post-data-should-be-bytes-or-an-iterable-of
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import urllib.request, urllib.error, urllib.parse
    _l_(419511)

except ImportError:
    pass

url = "https://www.customdomain.com"
_l_(419512)
d = _c_(419514, _n_(419513, "dict", lambda: dict), parameter1="value1", parameter2="value2")
_l_(419515)

req = _c_(419523, _a_(419517, _a_(419516, urllib, "request"), "Request"), _n_(419518, "url", lambda: url), data=_c_(419522, _a_(419520, _a_(419519, urllib, "parse"), "urlencode"), _n_(419521, "d", lambda: d)))
_l_(419524)
f = _c_(419528, _a_(419526, _a_(419525, urllib, "request"), "urlopen"), _n_(419527, "req", lambda: req))
_l_(419529)
resp = _c_(419532, _a_(419531, _n_(419530, "f", lambda: f), "read"))
_l_(419533)