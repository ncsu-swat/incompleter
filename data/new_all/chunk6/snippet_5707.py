# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62947923/attributeerror-nonetype-object-has-no-attribute-contains
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import requests
    _l_(368593)

except ImportError:
    pass
try:
    from bs4 import BeautifulSoup
    _l_(368595)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(368597)

except ImportError:
    pass
try:
    import pdfkit
    _l_(368599)

except ImportError:
    pass
try:
    import re
    _l_(368601)

except ImportError:
    pass

URL = 'https://timesofindia.indiatimes.com/'    
_l_(368602)    

page = _c_(368606, _a_(368604, _n_(368603, "requests", lambda: requests), "get"), _n_(368605, "URL", lambda: URL))    
_l_(368607)    
soup = _c_(368611, _n_(368608, "BeautifulSoup", lambda: BeautifulSoup), _a_(368610, _n_(368609, "page", lambda: page), "content"), 'lxml')    
_l_(368612)    
page = _c_(368616, _a_(368614, _n_(368613, "requests", lambda: requests), "get"), _n_(368615, "URL", lambda: URL))    
_l_(368617)    
soup = _c_(368621, _n_(368618, "BeautifulSoup", lambda: BeautifulSoup), _a_(368620, _n_(368619, "page", lambda: page), "content"), 'lxml')    
_l_(368622)    
all_links=_c_(368624, _n_(368623, "set", lambda: set))    
_l_(368625)    

for link in _c_(368628, _a_(368627, _n_(368626, "soup", lambda: soup), "find_all"), 'a'):
    _l_(368636)

    _c_(368634, _a_(368630, _n_(368629, "all_links", lambda: all_links), "add"), _c_(368633, _a_(368632, _n_(368631, "link", lambda: link), "get"), 'href'))    
    _l_(368635)    

s = _c_(368639, _n_(368637, "list", lambda: list), _n_(368638, "all_links", lambda: all_links))     
_l_(368640)     
_c_(368643, _n_(368641, "print", lambda: print), _n_(368642, "s", lambda: s))    
_l_(368644)    
x=[_n_(368645, "i", lambda: i) for i in _n_(368646, "s", lambda: s) if _c_(368650, _a_(368648, _n_(368647, "i", lambda: i), "_contains_"), _n_(368649, "URL", lambda: URL))]    
_l_(368651)    
m=[]    
_l_(368652)    
find_words= ['cbse', 'first-day']    
_l_(368653)    
for s in _n_(368654, "x", lambda: x):
    _l_(368666)

    if _c_(368659, _n_(368655, "any", lambda: any), (_n_(368656, "f", lambda: f) in _n_(368657, "s", lambda: s) for f in _n_(368658, "find_words", lambda: find_words))):
        _l_(368665)

        _c_(368663, _a_(368661, _n_(368660, "m", lambda: m), "append"), _n_(368662, "s", lambda: s))    
        _l_(368664)    
_c_(368669, _n_(368667, "print", lambda: print), _n_(368668, "m", lambda: m))
_l_(368670)