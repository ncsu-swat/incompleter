# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75637456/typeerror-a-bytes-like-object-is-required-not-str-python-3-bs4
# LIBRAIRIES

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import requests
    _l_(603291)

except ImportError:
    pass
try:
    from bs4 import BeautifulSoup
    _l_(603293)

except ImportError:
    pass
try:
    import csv
    _l_(603295)

except ImportError:
    pass


# SEARCH URL

url = 'https://www.atlas-monde.net/tous-les-pays/'
_l_(603296)
response = _c_(603300, _a_(603298, _n_(603297, "requests", lambda: requests), "get"), _n_(603299, "url", lambda: url))
_l_(603301)

# EXTRACT DATAS

if _a_(603303, _n_(603302, "response", lambda: response), "ok"):
    _l_(603320)

    soup = _c_(603307, _n_(603304, "BeautifulSoup", lambda: BeautifulSoup), _a_(603306, _n_(603305, "response", lambda: response), "text"), 'html.parser')
    _l_(603308)
    # items = soup.find_all(class_="sidebar")
    items = _c_(603311, _a_(603310, _n_(603309, "soup", lambda: soup), "find_all"), "td")
    _l_(603312)
    for i in _n_(603313, "items", lambda: items):
        _l_(603319)

        _c_(603317, _n_(603314, "print", lambda: print), _a_(603316, _n_(603315, "i", lambda: i), "string") + '\n')
        _l_(603318)


# CREATE DATAS FIELD

with _c_(603322, _n_(603321, "open", lambda: open), 'persons.csv', 'wb') as csvfile:
    _l_(603337)

    for item in _n_(603323, "items", lambda: items):
        _l_(603336)

        filewriter = _c_(603329, _a_(603325, _n_(603324, "csv", lambda: csv), "writer"), _n_(603326, "csvfile", lambda: csvfile), delimiter=',',
                                quotechar='|', quoting=_a_(603328, _n_(603327, "csv", lambda: csv), "QUOTE_MINIMAL"))
        _l_(603330)
        _c_(603334, _a_(603332, _n_(603331, "filewriter", lambda: filewriter), "writerow"), _n_(603333, "item", lambda: item))
        _l_(603335)