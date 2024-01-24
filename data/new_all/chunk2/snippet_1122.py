# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50416692/typeerror-request-missing-1-required-positional-argument-url
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import urllib3
    _l_(452649)

except ImportError:
    pass

http = _c_(452652, _a_(452651, _n_(452650, "urllib3", lambda: urllib3), "PoolManager"), 10)
_l_(452653)
url = 'https://www.desertessence.com/sitemap.xml'
_l_(452654)

pagedata = _a_(452659, _c_(452658, _a_(452656, _n_(452655, "http", lambda: http), "request"), _n_(452657, "url", lambda: url)), "data")
_l_(452660)