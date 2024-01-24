# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61983027/typeerror-list-indices-must-be-integers-or-slices-not-str-why-list-indexes-are
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import requests
    _l_(677934)

except ImportError:
    pass
try:
    from bs4 import BeautifulSoup
    _l_(677936)

except ImportError:
    pass
try:
    import urllib.request
    _l_(677938)

except ImportError:
    pass
try:
    import re
    _l_(677940)

except ImportError:
    pass

with _c_(677942, _n_(677941, "open", lambda: open), 'crawlingweb.csv')as f:
    _l_(677958)

    content=_c_(677945, _a_(677944, _n_(677943, "f", lambda: f), "readlines"))
    _l_(677946)
    content=[_c_(677949, _a_(677948, _n_(677947, "x", lambda: x), "strip")) for x in _n_(677950, "content", lambda: content)]
    _l_(677951)
    _c_(677956, _a_(677955, _c_(677954, _a_(677953, _n_(677952, "content", lambda: content)[183], "replace"), '[',''), "replace"), ']','')
    _l_(677957)

req = _c_(677962, _a_(677960, _n_(677959, "requests", lambda: requests), "get"), _n_(677961, "content", lambda: content)[183])
_l_(677963)
html = _a_(677965, _n_(677964, "req", lambda: req), "text")
_l_(677966)

data = _c_(677972, _a_(677971, _c_(677970, _a_(677968, _n_(677967, "re", lambda: re), "sub"), '[^0-9a-zA-Z\\s\\.\\,]', '', string=_n_(677969, "html", lambda: html)), "lower"))
_l_(677973)
data = _c_(677977, _a_(677975, _n_(677974, "re", lambda: re), "sub"), '<[^>]*>','',string=_n_(677976, "html", lambda: html))
_l_(677978)
data = _c_(677982, _a_(677980, _n_(677979, "re", lambda: re), "sub"), '[^ ㄱ-ㅣ가-힣]+','',string=_n_(677981, "html", lambda: html))
_l_(677983)
_c_(677986, _n_(677984, "print", lambda: print), _n_(677985, "data", lambda: data))
_l_(677987)