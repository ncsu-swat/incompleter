# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69848907/beautifulsoup-attributeerror-nonetype-object-has-no-attribute-text
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
res = _c_(645587, _a_(645586, _n_(645585, "requests", lambda: requests), "get"), 'https://www.babynamesdirect.com/baby-names/indian/boy/trending')
_l_(645588)
soup = _c_(645592, _n_(645589, "BeautifulSoup", lambda: BeautifulSoup), _a_(645591, _n_(645590, "res", lambda: res), "text"), 'html5lib')
_l_(645593)
ul  = _c_(645598, _a_(645597, _c_(645596, _a_(645595, _n_(645594, "soup", lambda: soup), "find"), 'div', class_ = 'ntb boy'), "find_all"), 'li')
_l_(645599)
names = [_a_(645602, _a_(645601, _n_(645600, "name", lambda: name), "dt"), "text") for name in _n_(645603, "ul", lambda: ul)]
_l_(645604)
_c_(645607, _n_(645605, "print", lambda: print), _n_(645606, "names", lambda: names))
_l_(645608)