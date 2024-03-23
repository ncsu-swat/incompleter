# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from urllib.request import urlopen
    _l_(97769)

except ImportError:
    pass
try:
    from bs4 import BeautifulSoup
    _l_(97771)

except ImportError:
    pass
bsObj = _c_(97774, _n_(97772, "BeautifulSoup", lambda: BeautifulSoup), _n_(97773, "html", lambda: html))
_l_(97775)
for link in _c_(97778, _a_(97777, _n_(97776, "bsObj", lambda: bsObj), "findAll"), 'a'):
    _l_(97787)

    if 'href' in _a_(97780, _n_(97779, "link", lambda: link), "attrs"):
        _l_(97786)

        _c_(97784, _n_(97781, "print", lambda: print), _a_(97783, _n_(97782, "link", lambda: link), "attrs")['href'])
        _l_(97785)