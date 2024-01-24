# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61908463/scraping-website-with-python3-attributeerror-nonetype-object-has-no-attribu
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from urllib.request import urlopen
    _l_(654922)

except ImportError:
    pass
try:
    from bs4 import BeautifulSoup
    _l_(654924)

except ImportError:
    pass

html = 'https://www.bloomberg.com/quote/SPX:IND'    
_l_(654925)    
page = _c_(654928, _n_(654926, "urlopen", lambda: urlopen), _n_(654927, "html", lambda: html))    
_l_(654929)    
data = _c_(654932, _n_(654930, "BeautifulSoup", lambda: BeautifulSoup), _n_(654931, "page", lambda: page), 'html.parser')    
_l_(654933)    
name_box = _c_(654936, _a_(654935, _n_(654934, "data", lambda: data), "find"), 'h1', attrs={'class': 'companyName__99a4824b'}) 
_l_(654937) 
name = _c_(654941, _a_(654940, _a_(654939, _n_(654938, "name_box", lambda: name_box), "text"), "strip")) 
_l_(654942) 
_c_(654945, _n_(654943, "print", lambda: print), _n_(654944, "name", lambda: name))
_l_(654946)