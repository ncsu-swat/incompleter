# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from urllib.request import urlopen
    _l_(106872)

except ImportError:
    pass
try:
    from bs4 import BeautifulSoup
    _l_(106874)

except ImportError:
    pass
html = _c_(106876, _n_(106875, "urlopen", lambda: urlopen), 'https://en.wikipedia.org/wiki/Main_Page')
_l_(106877)
titles = _c_(106880, _a_(106879, _n_(106878, "bs", lambda: bs), "find_all"), ['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
_l_(106881)
_c_(106884, _n_(106882, "print", lambda: print), 'List all the header tags :', *_n_(106883, "titles", lambda: titles), sep='\n\n')
_l_(106885)