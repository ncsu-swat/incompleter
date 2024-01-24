# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59065312/i-am-getting-attributeerror-nonetype-object-has-no-attribute-find-all
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import requests
    _l_(698318)

except ImportError:
    pass
try:
    from requests_html import HTMLSession
    _l_(698320)

except ImportError:
    pass
try:
    from bs4 import BeautifulSoup
    _l_(698322)

except ImportError:
    pass
try:
    import mysql.connector
    _l_(698324)

except ImportError:
    pass

page = _c_(698327, _a_(698326, _n_(698325, "requests", lambda: requests), "get"), "https://www.adelaideairport.com.au/flight-information/flight-search/")
_l_(698328)
soup = _c_(698332, _n_(698329, "BeautifulSoup", lambda: BeautifulSoup), _a_(698331, _n_(698330, "page", lambda: page), "content"), 'html.parser')
_l_(698333)
flights = _c_(698336, _a_(698335, _n_(698334, "soup", lambda: soup), "find"), id="SearchResultFlightListTable")
_l_(698337)
flight_items = _c_(698340, _a_(698339, _n_(698338, "flights", lambda: flights), "find_all"), class_="row")
_l_(698341)
flight = _n_(698342, "flight_items", lambda: flight_items)[0]
_l_(698343)
_c_(698348, _n_(698344, "print", lambda: print), _c_(698347, _a_(698346, _n_(698345, "flight", lambda: flight), "prettify")))
_l_(698349)