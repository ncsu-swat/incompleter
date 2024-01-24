# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74097041/attributeerror-list-object-has-no-attribute-decode-im-getting-this-error-w
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import csv
    _l_(468793)

except ImportError:
    pass
try:
    import requests
    _l_(468795)

except ImportError:
    pass
try:
    from bs4 import BeautifulSoup
    _l_(468797)

except ImportError:
    pass
try:
    import wget
    _l_(468799)

except ImportError:
    pass
with _c_(468801, _n_(468800, "open", lambda: open), '__memes_magic_thumbnails.csv', newline='') as csvfile:
    _l_(468809)

    data = _c_(468807, _n_(468802, "list", lambda: list), _c_(468806, _a_(468804, _n_(468803, "csv", lambda: csv), "reader"), _n_(468805, "csvfile", lambda: csvfile)))
    _l_(468808)
_c_(468812, _n_(468810, "print", lambda: print), _n_(468811, "data", lambda: data))
_l_(468813)
k=0
_l_(468814)
for link in _n_(468815, "data", lambda: data):
    _l_(468826)

    _c_(468818, _n_(468816, "print", lambda: print), _n_(468817, "k", lambda: k))
    _l_(468819)
    
    _c_(468823, _a_(468821, _n_(468820, "wget", lambda: wget), "download"), _n_(468822, "link", lambda: link) , "vid/logo.jpg")
    _l_(468824)
    k+=1
    _l_(468825)

_c_(468828, _n_(468827, "print", lambda: print), "succes")
_l_(468829)