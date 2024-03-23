# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from urllib.request import urlopen
    _l_(19433)

except ImportError:
    pass
try:
    from bs4 import BeautifulSoup
    _l_(19435)

except ImportError:
    pass
html = _c_(19437, _n_(19436, "urlopen", lambda: urlopen), 'https://en.wikipedia.org/wiki/Main_Page')
_l_(19438)
bs = _c_(19441, _n_(19439, "BeautifulSoup", lambda: BeautifulSoup), _n_(19440, "html", lambda: html), 'html.parser')
_l_(19442)
_c_(19445, _n_(19443, "print", lambda: print), 'List all the header tags :', *_n_(19444, "titles", lambda: titles), sep='\n\n')
_l_(19446)