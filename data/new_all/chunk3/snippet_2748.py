# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64491101/i-can-not-scrape-google-news-with-beautiful-soup-i-am-getting-the-errortypeerr
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from bs4 import BeautifulSoup
    _l_(574266)

except ImportError:
    pass
try:
    from urllib.request import urlopen
    _l_(574268)

except ImportError:
    pass

page_info=_c_(574270, _n_(574269, "urlopen", lambda: urlopen), 'https://news.google.com')
_l_(574271)
soup=_c_(574274, _n_(574272, "BeautifulSoup", lambda: BeautifulSoup), _n_(574273, "page_info", lambda: page_info),'html.parser')
_l_(574275)
headlines=_c_(574278, _a_(574277, _n_(574276, "soup", lambda: soup), "findall"), 'div',{'jscontroller':'d0DtYd'})
_l_(574279)
for head in _n_(574280, "headlines", lambda: headlines):
    _l_(574293)

    headline=_c_(574287, _a_(574286, _c_(574285, _a_(574284, _c_(574283, _a_(574282, _n_(574281, "head", lambda: head), "find"), 'h3'), "find"), 'a'), "get_text"))
    _l_(574288)
    _c_(574291, _n_(574289, "print", lambda: print), _n_(574290, "headline", lambda: headline))
    _l_(574292)