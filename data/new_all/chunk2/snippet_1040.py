# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50798940/beautifulsoup-and-regexp-attribute-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import requests
    _l_(442043)

except ImportError:
    pass
try:
    from bs4 import BeautifulSoup
    _l_(442045)

except ImportError:
    pass
try:
    import re
    _l_(442047)

except ImportError:
    pass

url = 'https://inventaris.onroerenderfgoed.be/erfgoedobjecten/4778'
_l_(442048)
page = _c_(442052, _a_(442050, _n_(442049, "requests", lambda: requests), "get"), _n_(442051, "url", lambda: url))
_l_(442053)

soup = _c_(442057, _n_(442054, "BeautifulSoup", lambda: BeautifulSoup), _a_(442056, _n_(442055, "page", lambda: page), "text"), 'html.parser')
_l_(442058)
text = _c_(442061, _a_(442060, _n_(442059, "soup", lambda: soup), "prettify"))
_l_(442062)

##block
p = _c_(442067, _a_(442064, _n_(442063, "re", lambda: re), "compile"), '(?s)(?<=(Typologie))(.*?)(?=(</a>))', _a_(442066, _n_(442065, "re", lambda: re), "VERBOSE"))
_l_(442068)
block = _c_(442074, _a_(442073, _c_(442072, _a_(442070, _n_(442069, "p", lambda: p), "search"), _n_(442071, "text", lambda: text)), "group"), 2)
_l_(442075)


##typo_url
p = _c_(442080, _a_(442077, _n_(442076, "re", lambda: re), "compile"), '(?s)(?<=(href=\"))(.*?)(?=(\">))', _a_(442079, _n_(442078, "re", lambda: re), "VERBOSE"))
_l_(442081)
typo_url = _c_(442087, _a_(442086, _c_(442085, _a_(442083, _n_(442082, "p", lambda: p), "search"), _n_(442084, "block", lambda: block)), "group"), 2)
_l_(442088)


## typo_name
p = _c_(442093, _a_(442090, _n_(442089, "re", lambda: re), "compile"), '\b(\w+)(\W*?)$', _a_(442092, _n_(442091, "re", lambda: re), "VERBOSE"))
_l_(442094)
typo_name = _c_(442100, _a_(442099, _c_(442098, _a_(442096, _n_(442095, "p", lambda: p), "search"), _n_(442097, "block", lambda: block)), "group"), 1)
_l_(442101)