# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64014172/beautifulsoup-attributeerror-when-using-find-all-on-multiple-tables
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import requests
    _l_(455678)

except ImportError:
    pass
try:
    from bs4 import BeautifulSoup
    _l_(455680)

except ImportError:
    pass

url = 'https://en.wikipedia.org/wiki/2020%E2%80%9321_Top_14_season'
_l_(455681)
response = _c_(455685, _a_(455683, _n_(455682, "requests", lambda: requests), "get"), _n_(455684, "url", lambda: url))
_l_(455686)
html = _a_(455688, _n_(455687, "response", lambda: response), "content")
_l_(455689)

soup = _c_(455692, _n_(455690, "BeautifulSoup", lambda: BeautifulSoup), _n_(455691, "html", lambda: html), 'html.parser')
_l_(455693)
match = _c_(455696, _a_(455695, _n_(455694, "soup", lambda: soup), "find_all"), '.vevent summary')
_l_(455697)

#for table in match.find_all('table'):
for data in _c_(455700, _a_(455699, _n_(455698, "match", lambda: match), "find_all"), 'tbody'):
    _l_(455716)

    for row in _c_(455703, _a_(455702, _n_(455701, "data", lambda: data), "find"), 'tr'):
        _l_(455715)

        for cell in _c_(455706, _a_(455705, _n_(455704, "row", lambda: row), "find"), 'td'):
            _l_(455714)

            _c_(455712, _n_(455707, "print", lambda: print), _c_(455711, _a_(455710, _a_(455709, _n_(455708, "cell", lambda: cell), "text"), "replace"), '&nbsp;', ''))
            _l_(455713)