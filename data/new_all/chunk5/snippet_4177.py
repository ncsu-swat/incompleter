# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61983027/typeerror-list-indices-must-be-integers-or-slices-not-str-why-list-indexes-are
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import requests
    _l_(702842)

except ImportError:
    pass
try:
    from bs4 import BeautifulSoup
    _l_(702844)

except ImportError:
    pass
try:
    import urllib.request
    _l_(702846)

except ImportError:
    pass
try:
    import re
    _l_(702848)

except ImportError:
    pass

with _c_(702850, _n_(702849, "open", lambda: open), 'crawlingweb.csv')as f:
    _l_(702860)

    content=_c_(702853, _a_(702852, _n_(702851, "f", lambda: f), "readlines"))
    _l_(702854)
    content=[_c_(702857, _a_(702856, _n_(702855, "x", lambda: x), "strip")) for x in _n_(702858, "content", lambda: content)]
    _l_(702859)

for i in _n_(702861, "content", lambda: content):
    _l_(702899)

    _c_(702867, _a_(702866, _c_(702865, _a_(702864, _n_(702862, "content", lambda: content)[_n_(702863, "i", lambda: i)], "replace"), '[', ''), "replace"), ']', '')
    _l_(702868)
    req = _c_(702873, _a_(702870, _n_(702869, "requests", lambda: requests), "get"), _n_(702871, "content", lambda: content)[_n_(702872, "i", lambda: i)])
    _l_(702874)
    html = _a_(702876, _n_(702875, "req", lambda: req), "text")
    _l_(702877)
    data = _c_(702883, _a_(702882, _c_(702881, _a_(702879, _n_(702878, "re", lambda: re), "sub"), '[^0-9a-zA-Z\\s\\.\\,]', '', string=_n_(702880, "html", lambda: html)), "lower"))
    _l_(702884)
    data = _c_(702888, _a_(702886, _n_(702885, "re", lambda: re), "sub"), '<[^>]*>', '', string=_n_(702887, "html", lambda: html))
    _l_(702889)
    data = _c_(702893, _a_(702891, _n_(702890, "re", lambda: re), "sub"), '[^ ㄱ-ㅣ가-힣]+', '', string=_n_(702892, "html", lambda: html))
    _l_(702894)
    _c_(702897, _n_(702895, "print", lambda: print), _n_(702896, "data", lambda: data))
    _l_(702898)