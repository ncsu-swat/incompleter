# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from urllib.request import urlopen
    _l_(97750)

except ImportError:
    pass
try:
    from bs4 import BeautifulSoup
    _l_(97752)

except ImportError:
    pass
html = _c_(97754, _n_(97753, "urlopen", lambda: urlopen), 'https://en.wikipedia.org/wiki/Python')
_l_(97755)
for link in _c_(97758, _a_(97757, _n_(97756, "bsObj", lambda: bsObj), "findAll"), 'a'):
    _l_(97767)

    if 'href' in _a_(97760, _n_(97759, "link", lambda: link), "attrs"):
        _l_(97766)

        _c_(97764, _n_(97761, "print", lambda: print), _a_(97763, _n_(97762, "link", lambda: link), "attrs")['href'])
        _l_(97765)