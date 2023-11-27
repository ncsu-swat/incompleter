# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/645312/what-is-the-quickest-way-to-http-get-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from nap.url import Url
    _l_(1543276)

except ImportError:
    pass
api = _c_(1543278, _n_(1543277, "Url", lambda: Url), 'https://api.github.com')
_l_(1543279)

gists = _c_(1543282, _a_(1543281, _n_(1543280, "api", lambda: api), "join"), 'gists')
_l_(1543283)
response = _c_(1543286, _a_(1543285, _n_(1543284, "gists", lambda: gists), "get"), params={'since': '2014-05-01T00:00:00Z'})
_l_(1543287)
_c_(1543292, _n_(1543288, "print", lambda: print), _c_(1543291, _a_(1543290, _n_(1543289, "response", lambda: response), "json")))
_l_(1543293)

