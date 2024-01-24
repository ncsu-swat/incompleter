# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63840124/error-while-using-beautifulsoup-in-python-attribute-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from bs4 import BeautifulSoup
    _l_(582381)

except ImportError:
    pass
try:
    import urllib.request
    _l_(582383)

except ImportError:
    pass

with _c_(582385, _n_(582384, "open", lambda: open), 'websites_mn.txt') as f:
    _l_(582390)

    txtdata = _c_(582388, _a_(582387, _n_(582386, "f", lambda: f), "readlines"))
    _l_(582389)

for raw_url in _n_(582391, "txtdata", lambda: txtdata):
    _l_(582422)

    raw_url = _c_(582394, _a_(582393, _n_(582392, "raw_url", lambda: raw_url), "strip"), '\n')
    _l_(582395)
    url = _c_(582399, _a_(582397, _a_(582396, urllib, "request"), "urlopen"), _n_(582398, "raw_url", lambda: raw_url))
    _l_(582400)
    content = _c_(582403, _a_(582402, _n_(582401, "url", lambda: url), "read"))
    _l_(582404)
    soup = _c_(582407, _n_(582405, "BeautifulSoup", lambda: BeautifulSoup), _n_(582406, "content", lambda: content), 'lxml')
    _l_(582408)
    table = _c_(582411, _a_(582410, _n_(582409, "soup", lambda: soup), "findAll"), 'div',attrs={"class":"journal-content-article"})
    _l_(582412)
    for x in _n_(582413, "table", lambda: table):
        _l_(582421)

        _c_(582419, _n_(582414, "print", lambda: print), _a_(582418, _c_(582417, _a_(582416, _n_(582415, "x", lambda: x), "find"), 'p'), "text"))
        _l_(582420)