# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/52169355/bs4-attributeerror-nonetype-object-has-no-attribute-text
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import bs4 as bs
    _l_(548572)

except ImportError:
    pass
try:
    import urllib.request
    _l_(548574)

except ImportError:
    pass
try:
    import csv
    _l_(548576)

except ImportError:
    pass

with _c_(548578, _n_(548577, "open", lambda: open), 'C:/Users/******/Desktop/urls.csv', 'r') as f:
    _l_(548645)

    reader = _c_(548582, _a_(548580, _n_(548579, "csv", lambda: csv), "reader"), _n_(548581, "f", lambda: f))
    _l_(548583)
    pages = _c_(548586, _n_(548584, "list", lambda: list), _n_(548585, "reader", lambda: reader))
    _l_(548587)
    for i in _c_(548589, _n_(548588, "range", lambda: range), 0,300):
        _l_(548644)

        page = _c_(548596, _a_(548590, '', "join"), _c_(548595, _n_(548591, "map", lambda: map), _n_(548592, "str", lambda: str), _n_(548593, "pages", lambda: pages)[_n_(548594, "i", lambda: i)]))
        _l_(548597)
        _c_(548602, _n_(548598, "print", lambda: print), 'Working on ' + _c_(548601, _n_(548599, "str", lambda: str), _n_(548600, "i", lambda: i))+ "...")
        _l_(548603)
        sauce = _c_(548609, _a_(548608, _c_(548607, _a_(548605, _a_(548604, urllib, "request"), "urlopen"), _n_(548606, "page", lambda: page)), "read"))
        _l_(548610)
        soup =_c_(548614, _a_(548612, _n_(548611, "bs", lambda: bs), "BeautifulSoup"), _n_(548613, "sauce", lambda: sauce),'lxml')
        _l_(548615)
        textoffer = _a_(548621, _c_(548620, _a_(548619, _a_(548618, _a_(548617, _n_(548616, "soup", lambda: soup), "body"), "div"), "find"), 'div',class_='jobsearch-JobComponent-description icl-u-xs-mt--md'), "text")
        _l_(548622)
        file = _c_(548627, _n_(548623, "open", lambda: open), _c_(548626, _n_(548624, "str", lambda: str), _n_(548625, "i", lambda: i))+ '.txt','w')
        _l_(548628)
        _c_(548632, _a_(548630, _n_(548629, "file", lambda: file), "write"), _n_(548631, "textoffer", lambda: textoffer))
        _l_(548633)
        _c_(548636, _a_(548635, _n_(548634, "file", lambda: file), "close"))
        _l_(548637)
        _c_(548642, _n_(548638, "print", lambda: print), _c_(548641, _n_(548639, "str", lambda: str), _n_(548640, "i", lambda: i)) + " Done!")
        _l_(548643)