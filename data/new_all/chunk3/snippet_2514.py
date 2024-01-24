# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73877049/attributeerror-nonetype-object-has-no-attribute-find-beautifulsoup
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from bs4 import BeautifulSoup
    _l_(557575)

except ImportError:
    pass
try:
    import requests
    _l_(557577)

except ImportError:
    pass

def cryptoPrice(crypto):
    _l_(557601)

    url = "https://www.google.com/search?q=" + _n_(557578, "crypto", lambda: crypto) + "price"
    _l_(557579)

    req = _c_(557583, _a_(557581, _n_(557580, "requests", lambda: requests), "get"), _n_(557582, "url", lambda: url))
    _l_(557584)

    soupObject = _c_(557588, _n_(557585, "BeautifulSoup", lambda: BeautifulSoup), _a_(557587, _n_(557586, "req", lambda: req), "text"), 'html.parser')
    _l_(557589)
    element = _a_(557597, _c_(557596, _a_(557595, _c_(557594, _a_(557593, _c_(557592, _a_(557591, _n_(557590, "soupObject", lambda: soupObject), "find"), "div", {"class": "card-section PZPZlf"}), "find"), "div"), "find"), "span", {"class": 'pclqee'}), "text")
    _l_(557598)
    aux = _n_(557599, "element", lambda: element)
    _l_(557600)

    return aux


price = _c_(557603, _n_(557602, "cryptoPrice", lambda: cryptoPrice), 'bitcoin')
_l_(557604)
_c_(557607, _n_(557605, "print", lambda: print), _n_(557606, "price", lambda: price))
_l_(557608)