# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76716939/request-getpage-typeerror-cannot
# -*- coding: utf-8 -*-

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from twisted.web.client import ProxyAgent
    _l_(616830)

except ImportError:
    pass
try:
    from twisted.web import client
    _l_(616832)

except ImportError:
    pass

url="http://www.opensubtitles.org/libs/suggest.php?format=json2&SubLanguageID=null&MovieName=red"
_l_(616833)

headers= {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
          'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
          'Upgrade-Insecure-Requests': '1',
          'Content-Type': 'application/x-www-form-urlencoded',
          'Referer': _n_(616834, "url", lambda: url),
          'Connection': 'keep-alive',
          'Accept-Encoding':'gzip, deflate'}
_l_(616835)

def downloadChunks():
    _l_(616846)


    d = _c_(616840, _a_(616837, _n_(616836, "client", lambda: client), "getPage"), _n_(616838, "url", lambda: url), contextFactory=None, method="GET", headers=_n_(616839, "headers", lambda: headers))
    _l_(616841)
    _c_(616844, _n_(616842, "print", lambda: print), _n_(616843, "d", lambda: d))
    _l_(616845)
 
_c_(616848, _n_(616847, "downloadChunks", lambda: downloadChunks))
_l_(616849)