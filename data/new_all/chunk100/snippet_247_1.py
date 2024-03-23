# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from urllib.request import urlopen
    _l_(19448)

except ImportError:
    pass
try:
    from bs4 import BeautifulSoup
    _l_(19450)

except ImportError:
    pass
html = _c_(19452, _n_(19451, "urlopen", lambda: urlopen), 'https://en.wikipedia.org/wiki/Main_Page')
_l_(19453)
titles = _c_(19456, _a_(19455, _n_(19454, "bs", lambda: bs), "find_all"), ['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
_l_(19457)
_c_(19460, _n_(19458, "print", lambda: print), 'List all the header tags :', *_n_(19459, "titles", lambda: titles), sep='\n\n')
_l_(19461)