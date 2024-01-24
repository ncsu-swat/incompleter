# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65702068/error-attributeerror-nonetype-object-has-no-attribute-find
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
   import requests
   _l_(344393)

except ImportError:
   pass
try:
   import lxml
   _l_(344395)

except ImportError:
   pass
try:
   import bs4
   _l_(344397)

except ImportError:
   pass

title = ''
_l_(344398)
date = ''
_l_(344399)
text = ''
_l_(344400)
top = []
_l_(344401)
link = []  
_l_(344402)  


web_link = 'https://timesofindia.indiatimes.com/{}/'
_l_(344403)
web_link = _c_(344406, _a_(344405, _n_(344404, "web_link", lambda: web_link), "format"), 'india')
_l_(344407)
req = _c_(344411, _a_(344409, _n_(344408, "requests", lambda: requests), "get"), _n_(344410, "web_link", lambda: web_link))
_l_(344412)
soup = _c_(344417, _a_(344414, _n_(344413, "bs4", lambda: bs4), "BeautifulSoup"), _a_(344416, _n_(344415, "req", lambda: req), "text"), 'lxml')
_l_(344418)
topi = _c_(344421, _a_(344420, _n_(344419, "soup", lambda: soup), "find"), 'div', {'class':'main-content'})
_l_(344422)
topi = _c_(344425, _a_(344424, _n_(344423, "topi", lambda: topi), "find_all"), 'span', {'class':'w_tle'})
_l_(344426)
for i in _c_(344431, _n_(344427, "range", lambda: range), _c_(344430, _n_(344428, "len", lambda: len), _n_(344429, "topi", lambda: topi))):
   _l_(344444)

   top = _c_(344437, _a_(344436, _c_(344435, _a_(344434, _n_(344432, "topi", lambda: topi)[_n_(344433, "i", lambda: i)], "find"), 'a'), "get"), 'href')
   _l_(344438)
   _c_(344442, _a_(344440, _n_(344439, "link", lambda: link), "append"), 'https://timesofindia.indiatimes.com' + _n_(344441, "top", lambda: top))
   _l_(344443)
for i in _c_(344449, _n_(344445, "range", lambda: range), _c_(344448, _n_(344446, "len", lambda: len), _n_(344447, "link", lambda: link))):
   _l_(344470)

   rq = _c_(344454, _a_(344451, _n_(344450, "requests", lambda: requests), "get"), _n_(344452, "link", lambda: link)[_n_(344453, "i", lambda: i)])
   _l_(344455)
   sp = _c_(344460, _a_(344457, _n_(344456, "bs4", lambda: bs4), "BeautifulSoup"), _a_(344459, _n_(344458, "rq", lambda: rq), "text"), 'lxml')
   _l_(344461)
   title = _c_(344464, _a_(344463, _n_(344462, "sp", lambda: sp), "find"), 'div', {'class':'_2NFXP'})
   _l_(344465)
   title = _c_(344468, _a_(344467, _n_(344466, "title", lambda: title), "find"), 'h1',{'class':'_23498'})
   _l_(344469)