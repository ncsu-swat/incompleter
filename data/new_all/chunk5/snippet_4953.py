# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73760092/why-do-i-get-an-empty-list-while-scraping-website-and-end-in-type-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import requests
    _l_(669108)

except ImportError:
    pass
try:
    from bs4 import  BeautifulSoup
    _l_(669110)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(669112)

except ImportError:
    pass
try:
    from urllib import response
    _l_(669114)

except ImportError:
    pass


kitapurl = "https://1000kitap.com/alintilar"
_l_(669115)

response = _c_(669119, _a_(669117, _n_(669116, "requests", lambda: requests), "get"), _n_(669118, "kitapurl", lambda: kitapurl))
_l_(669120)
soup = _c_(669124, _n_(669121, "BeautifulSoup", lambda: BeautifulSoup), _a_(669123, _n_(669122, "response", lambda: response), "content"),"html.parser")
_l_(669125)
gelen_ana_veri= _c_(669128, _a_(669127, _n_(669126, "soup", lambda: soup), "find_all"), 'meta',attrs={'property':'og:description'})['content']
_l_(669129)
_c_(669132, _n_(669130, "print", lambda: print), _n_(669131, "gelen_ana_veri", lambda: gelen_ana_veri))
_l_(669133)