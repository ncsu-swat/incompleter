# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61286342/python3-x-attributeerror-nonetype-object-has-no-attribute-get-a-one-scrip
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from bs4 import BeautifulSoup
    _l_(353891)

except ImportError:
    pass
filename = "F:\Test\ErrorFolder\ErrorFile.html"
_l_(353892)

with _c_(353895, _n_(353893, "open", lambda: open), _n_(353894, "filename", lambda: filename), "r") as f:
    _l_(353916)

    soup = _c_(353898, _n_(353896, "BeautifulSoup", lambda: BeautifulSoup), _n_(353897, "f", lambda: f), 'html.parser')
    _l_(353899)
    resources = _c_(353902, _a_(353901, _n_(353900, "soup", lambda: soup), "find"), ['ix:references', 'references'])
    _l_(353903)
    #print(resources)
    for s in _c_(353906, _a_(353905, _n_(353904, "resources", lambda: resources), "find_all"), ['link:schemaRef', 'schemaRef', 'schemaref', 'link:schemaref']):
        _l_(353915)

        x = _c_(353909, _a_(353908, _n_(353907, "s", lambda: s), "get"), 'xlink:href')
        _l_(353910)
        _c_(353913, _n_(353911, "print", lambda: print), _n_(353912, "x", lambda: x))
        _l_(353914)