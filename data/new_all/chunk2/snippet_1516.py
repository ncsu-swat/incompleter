# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/47380110/python-attribute-error-nonetype-object-has-no-attribute-find-all
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from bs4 import BeautifulSoup
    _l_(421303)

except ImportError:
    pass
try:
    from urllib.request import urlopen
    _l_(421305)

except ImportError:
    pass
url='https://simple.wikipedia.org/wiki/List_of_U.S._states'
_l_(421306)
web=_c_(421309, _n_(421307, "urlopen", lambda: urlopen), _n_(421308, "url", lambda: url))
_l_(421310)
source=_c_(421313, _n_(421311, "BeautifulSoup", lambda: BeautifulSoup), _n_(421312, "web", lambda: web), 'html.parser')
_l_(421314)
table=_c_(421317, _a_(421316, _n_(421315, "source", lambda: source), "find"), 'table', {'class': 'wikitable sortable jquery-tablesorter'})
_l_(421318)
abbs=_c_(421321, _a_(421320, _n_(421319, "table", lambda: table), "find_all"), 'b')
_l_(421322)
_c_(421327, _n_(421323, "print", lambda: print), _c_(421326, _a_(421325, _n_(421324, "abbs", lambda: abbs), "get_text")))
_l_(421328)