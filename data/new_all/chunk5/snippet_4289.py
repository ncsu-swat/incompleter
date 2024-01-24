# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60261686/attributeerror-list-object-has-no-attribute-timeout
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import bs4 as bs
    _l_(687913)

except ImportError:
    pass
try:
    import urllib.request
    _l_(687915)

except ImportError:
    pass
try:
    import urllib.parse
    _l_(687917)

except ImportError:
    pass
try:
    import re
    _l_(687919)

except ImportError:
    pass
try:
    import nltk
    _l_(687921)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(687923)

except ImportError:
    pass
try:
    from pandas import DataFrame
    _l_(687925)

except ImportError:
    pass


_c_(687928, _a_(687927, _n_(687926, "nltk", lambda: nltk), "download"), 'stopwords')
_l_(687929)
try:
    import heapq
    _l_(687931)

except ImportError:
    pass

listofurls = _c_(687934, _a_(687933, _n_(687932, "pd", lambda: pd), "read_csv"), "C:/Users/Sajid Hasan Sifat/Desktop/global one/GO-url.csv") 
_l_(687935) 
urls = _c_(687938, _n_(687936, "DataFrame", lambda: DataFrame), _n_(687937, "listofurls", lambda: listofurls), columns = ['urls'])
_l_(687939)
url_list = _c_(687943, _a_(687942, _a_(687941, _n_(687940, "urls", lambda: urls), "values"), "tolist"))
_l_(687944)
_c_(687947, _n_(687945, "print", lambda: print), _n_(687946, "url_list", lambda: url_list)[0])
_l_(687948)

req = _c_(687952, _a_(687950, _a_(687949, urllib, "request"), "Request"), _n_(687951, "url_list", lambda: url_list)[0])    
_l_(687953)    
_c_(687956, _n_(687954, "print", lambda: print), _n_(687955, "req", lambda: req)) 
_l_(687957) 
sourceData = _c_(687961, _a_(687959, _a_(687958, urllib, "request"), "urlopen"), _n_(687960, "url_list", lambda: url_list)[0]) 
_l_(687962) 

source = _c_(687965, _a_(687964, _n_(687963, "sourceData", lambda: sourceData), "read"))
_l_(687966)
soup = _c_(687970, _a_(687968, _n_(687967, "bs", lambda: bs), "BeautifulSoup"), _n_(687969, "source", lambda: source))
_l_(687971)