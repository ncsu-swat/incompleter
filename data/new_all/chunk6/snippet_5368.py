# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61286342/python3-x-attributeerror-nonetype-object-has-no-attribute-get-a-one-scrip
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from bs4 import BeautifulSoup
    _l_(339838)

except ImportError:
    pass
filename = "F:\Test\ErrorFolder\ErrorFile.html"
_l_(339839)

with _c_(339842, _n_(339840, "open", lambda: open), _n_(339841, "filename", lambda: filename), "r") as f:
    _l_(339863)

    soup = _c_(339845, _n_(339843, "BeautifulSoup", lambda: BeautifulSoup), _n_(339844, "f", lambda: f), 'html.parser')
    _l_(339846)
    resources = _c_(339849, _a_(339848, _n_(339847, "soup", lambda: soup), "find"), ['ix:references', 'references'])
    _l_(339850)
    #print(resources)
    for s in _c_(339853, _a_(339852, _n_(339851, "resources", lambda: resources), "find_all"), ['link:schemaRef', 'schemaRef', 'schemaref', 'link:schemaref']):
        _l_(339862)

        x = _c_(339856, _a_(339855, _n_(339854, "s", lambda: s), "get"), 'xlink:href')
        _l_(339857)
        _c_(339860, _n_(339858, "print", lambda: print), _n_(339859, "x", lambda: x))
        _l_(339861)