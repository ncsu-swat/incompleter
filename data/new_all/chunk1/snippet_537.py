# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56744083/attributeerror-str-object-has-no-attribute-descendants-error-when-using-bea
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from bs4 import BeautifulSoup, SoupStrainer
    _l_(396618)

except ImportError:
    pass
try:
    import requests
    _l_(396620)

except ImportError:
    pass

url = "https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3210001601"
_l_(396621)
page = _c_(396625, _a_(396623, _n_(396622, "requests", lambda: requests), "get"), _n_(396624, "url", lambda: url))
_l_(396626)
data = _a_(396628, _n_(396627, "page", lambda: page), "text")
_l_(396629)
soup = _n_(396630, "BeautifulSoup", lambda: BeautifulSoup)
_l_(396631)
_c_(396634, _a_(396633, _n_(396632, "soup", lambda: soup), "find_all"), 'h1')
_l_(396635)

_c_(396638, _n_(396636, "print", lambda: print), _n_(396637, "text", lambda: text))
_l_(396639)