# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64024003/typeerror-nonetype-object-is-not-subscriptable-with-bs4
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sys
    _l_(448627)

except ImportError:
    pass
try:
    from bs4 import BeautifulSoup as Soup
    _l_(448629)

except ImportError:
    pass

file ="temp.xml"
_l_(448630)
handler = _c_(448635, _a_(448634, _c_(448633, _n_(448631, "open", lambda: open), _n_(448632, "file", lambda: file)), "read"))
_l_(448636)
soup = _c_(448639, _n_(448637, "Soup", lambda: Soup), _n_(448638, "handler", lambda: handler),features="lxml")
_l_(448640)

for vHost in _c_(448645, _a_(448644, _c_(448643, _a_(448642, _n_(448641, "soup", lambda: soup), "find"), 'virtualhost'), "find_all"), 'name', string='example.com'):
    _l_(448659)

    _c_(448649, _n_(448646, "print", lambda: print), _a_(448648, _n_(448647, "vHost", lambda: vHost), "parent"))#display the right level
    _l_(448650)#display the right level
    temp=_a_(448653, _a_(448652, _n_(448651, "vHost", lambda: vHost), "parent"), "virtualhost")['id']
    _l_(448654)
    _c_(448657, _n_(448655, "print", lambda: print), _n_(448656, "temp", lambda: temp))
    _l_(448658)