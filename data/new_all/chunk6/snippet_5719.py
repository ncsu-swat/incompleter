# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61487693/nameerror-name-soup-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import requests
    _l_(359992)

except ImportError:
    pass
try:
    from bs4 import BeautifulSoup
    _l_(359994)

except ImportError:
    pass

url = 'https://www.amazon.ca/QuietComfort-Wireless-Headphones-Cancelling-Control/dp/B0756CYWWD/ref=sr_1_3?crid=11Q0SFC2UP92R&keywords=bose+quietcomfort+35&qid=1588098577&s=electronics&sprefix=bose+q%2Celectronics%2C160&sr=1-3'
_l_(359995)
r = _c_(359999, _a_(359997, _n_(359996, "requests", lambda: requests), "get"), _n_(359998, "url", lambda: url))
_l_(360000)
data = _c_(360004, _n_(360001, "BeautifulSoup", lambda: BeautifulSoup), _a_(360003, _n_(360002, "r", lambda: r), "text"), 'html.parser')
_l_(360005)
original_price = _c_(360008, _a_(360007, _n_(360006, "soup", lambda: soup), "find"), id = "priceblock_ourprice")
_l_(360009)
_c_(360012, _n_(360010, "print", lambda: print), _n_(360011, "original_price", lambda: original_price))
_l_(360013)