# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61286342/python3-x-attributeerror-nonetype-object-has-no-attribute-get-a-one-scrip
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from bs4 import BeautifulSoup
    _l_(342733)

except ImportError:
    pass
filename = "F:\Test\ErrorFolder\ErrorFile.html"
_l_(342734)

with _c_(342737, _n_(342735, "open", lambda: open), _n_(342736, "filename", lambda: filename), "r") as f:
    _l_(342758)

    soup = _c_(342740, _n_(342738, "BeautifulSoup", lambda: BeautifulSoup), _n_(342739, "f", lambda: f), 'html.parser')
    _l_(342741)
    resources = _c_(342744, _a_(342743, _n_(342742, "soup", lambda: soup), "find"), ['ix:references', 'references'])
    _l_(342745)
    #print(resources)
    for s in _c_(342748, _a_(342747, _n_(342746, "resources", lambda: resources), "find_all"), ['link:schemaRef', 'schemaRef', 'schemaref', 'link:schemaref']):
        _l_(342757)

        x = _c_(342751, _a_(342750, _n_(342749, "s", lambda: s), "get"), 'xlink:href')
        _l_(342752)
        _c_(342755, _n_(342753, "print", lambda: print), _n_(342754, "x", lambda: x))
        _l_(342756)