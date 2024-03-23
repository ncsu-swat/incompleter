# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from urllib.request import urlopen
    _l_(19463)

except ImportError:
    pass
try:
    from bs4 import BeautifulSoup
    _l_(19465)

except ImportError:
    pass
bs = _c_(19468, _n_(19466, "BeautifulSoup", lambda: BeautifulSoup), _n_(19467, "html", lambda: html), 'html.parser')
_l_(19469)
titles = _c_(19472, _a_(19471, _n_(19470, "bs", lambda: bs), "find_all"), ['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
_l_(19473)
_c_(19476, _n_(19474, "print", lambda: print), 'List all the header tags :', *_n_(19475, "titles", lambda: titles), sep='\n\n')
_l_(19477)