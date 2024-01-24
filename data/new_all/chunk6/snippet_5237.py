# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51087973/attribute-error-none-type-object-has-no-attribute-get-text
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import urllib.request
    _l_(357592)

except ImportError:
    pass
try:
    from bs4 import BeautifulSoup
    _l_(357594)

except ImportError:
    pass
try:
    import pymysql.cursors
    _l_(357596)

except ImportError:
    pass

a = _c_(357598, _n_(357597, "input", lambda: input), 'enter the item to be searched :')
_l_(357599)
a = _c_(357602, _a_(357601, _n_(357600, "a", lambda: a), "replace"), " ","")
_l_(357603)

html = _c_(357607, _a_(357605, _a_(357604, urllib, "request"), "urlopen"), "https://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords="+_n_(357606, "a", lambda: a))
_l_(357608)

bsObj = _c_(357611, _n_(357609, "BeautifulSoup", lambda: BeautifulSoup), _n_(357610, "html", lambda: html),'lxml')
_l_(357612)
recordList = _c_(357615, _a_(357614, _n_(357613, "bsObj", lambda: bsObj), "findAll"), 'a', class_='a-link-normal a-text-normal')
_l_(357616)

connection = _c_(357621, _a_(357618, _n_(357617, "pymysql", lambda: pymysql), "connect"), host='localhost',
                         user='root',
                         password='',
                         db='shopping',
                         charset='utf8mb4',
                         cursorclass=_a_(357620, _a_(357619, pymysql, "cursors"), "DictCursor"))
_l_(357622)

try:
    _l_(357671)

    with _c_(357625, _a_(357624, _n_(357623, "connection", lambda: connection), "cursor")) as cursor:
        _l_(357661)

        for record in _n_(357626, "recordList", lambda: recordList):
            _l_(357660)

            name = _c_(357633, _a_(357632, _c_(357631, _a_(357630, _c_(357629, _a_(357628, _n_(357627, "record", lambda: record), "find"), "h2", {"class": "a-size-small a-color-base s-inline  s-access-title  a-text-normal", }), "get_text")), "strip"))
            _l_(357634)
            sale_price = _c_(357641, _a_(357640, _c_(357639, _a_(357638, _c_(357637, _a_(357636, _n_(357635, "record", lambda: record), "find"), "span", {"class": "currencyINR"}), "get_text")), "strip"))
            _l_(357642)
            category = _c_(357649, _a_(357648, _c_(357647, _a_(357646, _c_(357645, _a_(357644, _n_(357643, "record", lambda: record), "find"), "span", {"class": "a-color-base a-text-bold"}), "get_text")), "strip"))
            _l_(357650)
            sql = "INSERT INTO `amazon` (`name`, `sale_price`, `category`) VALUES (%s, %s, %s)"
            _l_(357651)
            _c_(357658, _a_(357653, _n_(357652, "cursor", lambda: cursor), "execute"), _n_(357654, "sql", lambda: sql), (_n_(357655, "name", lambda: name), _n_(357656, "sale_price", lambda: sale_price), _n_(357657, "category", lambda: category)))
            _l_(357659)
    _c_(357664, _a_(357663, _n_(357662, "connection", lambda: connection), "commit"))
    _l_(357665)
finally:
    _l_(357670)

    _c_(357668, _a_(357667, _n_(357666, "connection", lambda: connection), "close"))
    _l_(357669)