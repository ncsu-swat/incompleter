# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/30760728/python-3-urllib-produces-typeerror-post-data-should-be-bytes-or-an-iterable-of
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import urllib2
    _l_(411221)

except ImportError:
    pass
try:
    import urllib
    _l_(411223)

except ImportError:
    pass

url = "https://www.customdomain.com"
_l_(411224)
d = _c_(411226, _n_(411225, "dict", lambda: dict), parameter1="value1", parameter2="value2")
_l_(411227)

req = _c_(411235, _a_(411229, _n_(411228, "urllib2", lambda: urllib2), "Request"), _n_(411230, "url", lambda: url), data=_c_(411234, _a_(411232, _n_(411231, "urllib", lambda: urllib), "urlencode"), _n_(411233, "d", lambda: d)))
_l_(411236)
f = _c_(411240, _a_(411238, _n_(411237, "urllib2", lambda: urllib2), "urlopen"), _n_(411239, "req", lambda: req))
_l_(411241)
resp = _c_(411244, _a_(411243, _n_(411242, "f", lambda: f), "read"))
_l_(411245)