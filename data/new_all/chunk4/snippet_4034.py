# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63840124/error-while-using-beautifulsoup-in-python-attribute-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from bs4 import BeautifulSoup
    _l_(581588)

except ImportError:
    pass
try:
    import urllib.request
    _l_(581590)

except ImportError:
    pass

with _c_(581592, _n_(581591, "open", lambda: open), 'websites_mn.txt') as f:
    _l_(581597)

    txtdata = _c_(581595, _a_(581594, _n_(581593, "f", lambda: f), "readlines"))
    _l_(581596)

for raw_url in _n_(581598, "txtdata", lambda: txtdata):
    _l_(581629)

    raw_url = _c_(581601, _a_(581600, _n_(581599, "raw_url", lambda: raw_url), "strip"), '\n')
    _l_(581602)
    url = _c_(581606, _a_(581604, _a_(581603, urllib, "request"), "urlopen"), _n_(581605, "raw_url", lambda: raw_url))
    _l_(581607)
    content = _c_(581610, _a_(581609, _n_(581608, "url", lambda: url), "read"))
    _l_(581611)
    soup = _c_(581614, _n_(581612, "BeautifulSoup", lambda: BeautifulSoup), _n_(581613, "content", lambda: content), 'lxml')
    _l_(581615)
    table = _c_(581618, _a_(581617, _n_(581616, "soup", lambda: soup), "findAll"), 'div',attrs={"class":"journal-content-article"})
    _l_(581619)
    for x in _n_(581620, "table", lambda: table):
        _l_(581628)

        _c_(581626, _n_(581621, "print", lambda: print), _a_(581625, _c_(581624, _a_(581623, _n_(581622, "x", lambda: x), "find"), 'p'), "text"))
        _l_(581627)