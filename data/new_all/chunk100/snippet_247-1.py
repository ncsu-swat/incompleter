# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from urllib.request import urlopen
    _l_(106856)

except ImportError:
    pass
try:
    from bs4 import BeautifulSoup
    _l_(106858)

except ImportError:
    pass
bs = _c_(106861, _n_(106859, "BeautifulSoup", lambda: BeautifulSoup), _n_(106860, "html", lambda: html), 'html.parser')
_l_(106862)
titles = _c_(106865, _a_(106864, _n_(106863, "bs", lambda: bs), "find_all"), ['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
_l_(106866)
_c_(106869, _n_(106867, "print", lambda: print), 'List all the header tags :', *_n_(106868, "titles", lambda: titles), sep='\n\n')
_l_(106870)