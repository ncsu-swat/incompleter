# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from urllib.request import urlopen
    _l_(106841)

except ImportError:
    pass
try:
    from bs4 import BeautifulSoup
    _l_(106843)

except ImportError:
    pass
html = _c_(106845, _n_(106844, "urlopen", lambda: urlopen), 'https://en.wikipedia.org/wiki/Main_Page')
_l_(106846)
bs = _c_(106849, _n_(106847, "BeautifulSoup", lambda: BeautifulSoup), _n_(106848, "html", lambda: html), 'html.parser')
_l_(106850)
_c_(106853, _n_(106851, "print", lambda: print), 'List all the header tags :', *_n_(106852, "titles", lambda: titles), sep='\n\n')
_l_(106854)