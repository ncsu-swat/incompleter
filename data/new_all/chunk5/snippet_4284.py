# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60261686/attributeerror-list-object-has-no-attribute-timeout
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import bs4 as bs
    _l_(650622)

except ImportError:
    pass
try:
    import urllib.request
    _l_(650624)

except ImportError:
    pass
try:
    import urllib.parse
    _l_(650626)

except ImportError:
    pass
try:
    import re
    _l_(650628)

except ImportError:
    pass
try:
    import nltk
    _l_(650630)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(650632)

except ImportError:
    pass
try:
    from pandas import DataFrame
    _l_(650634)

except ImportError:
    pass


_c_(650637, _a_(650636, _n_(650635, "nltk", lambda: nltk), "download"), 'stopwords')
_l_(650638)
try:
    import heapq
    _l_(650640)

except ImportError:
    pass

listofurls = _c_(650643, _a_(650642, _n_(650641, "pd", lambda: pd), "read_csv"), "C:/Users/Sajid Hasan Sifat/Desktop/global one/GO-url.csv") 
_l_(650644) 
urls = _c_(650647, _n_(650645, "DataFrame", lambda: DataFrame), _n_(650646, "listofurls", lambda: listofurls), columns = ['urls'])
_l_(650648)
url_list = _c_(650652, _a_(650651, _a_(650650, _n_(650649, "urls", lambda: urls), "values"), "tolist"))
_l_(650653)
_c_(650656, _n_(650654, "print", lambda: print), _n_(650655, "url_list", lambda: url_list)[0])
_l_(650657)

req = _c_(650661, _a_(650659, _a_(650658, urllib, "request"), "Request"), _n_(650660, "url_list", lambda: url_list)[0])    
_l_(650662)    
_c_(650665, _n_(650663, "print", lambda: print), _n_(650664, "req", lambda: req)) 
_l_(650666) 
sourceData = _c_(650670, _a_(650668, _a_(650667, urllib, "request"), "urlopen"), _n_(650669, "url_list", lambda: url_list)[0]) 
_l_(650671) 

source = _c_(650674, _a_(650673, _n_(650672, "sourceData", lambda: sourceData), "read"))
_l_(650675)
soup = _c_(650679, _a_(650677, _n_(650676, "bs", lambda: bs), "BeautifulSoup"), _n_(650678, "source", lambda: source))
_l_(650680)