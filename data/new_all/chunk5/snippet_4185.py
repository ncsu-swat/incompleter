# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61908463/scraping-website-with-python3-attributeerror-nonetype-object-has-no-attribu
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from urllib.request import urlopen
    _l_(700717)

except ImportError:
    pass
try:
    from bs4 import BeautifulSoup
    _l_(700719)

except ImportError:
    pass

html = 'https://www.bloomberg.com/quote/SPX:IND'    
_l_(700720)    
page = _c_(700723, _n_(700721, "urlopen", lambda: urlopen), _n_(700722, "html", lambda: html))    
_l_(700724)    
data = _c_(700727, _n_(700725, "BeautifulSoup", lambda: BeautifulSoup), _n_(700726, "page", lambda: page), 'html.parser')    
_l_(700728)    
name_box = _c_(700731, _a_(700730, _n_(700729, "data", lambda: data), "find"), 'h1', attrs={'class': 'companyName__99a4824b'}) 
_l_(700732) 
name = _c_(700736, _a_(700735, _a_(700734, _n_(700733, "name_box", lambda: name_box), "text"), "strip")) 
_l_(700737) 
_c_(700740, _n_(700738, "print", lambda: print), _n_(700739, "name", lambda: name))
_l_(700741)