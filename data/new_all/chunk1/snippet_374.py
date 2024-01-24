# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/47847807/typeerror-expected-string-or-bytes-like-object-while-filtering-the-nested-list
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
pattern = _c_(377602, _a_(377601, _n_(377600, "re", lambda: re), "compile"), r'\W+')
_l_(377603)
newlist = _c_(377610, _n_(377604, "list", lambda: list), _c_(377609, _n_(377605, "filter", lambda: filter), _a_(377607, _n_(377606, "pattern", lambda: pattern), "search"), _n_(377608, "list", lambda: list)))
_l_(377611)
_c_(377614, _n_(377612, "print", lambda: print), _n_(377613, "newlist", lambda: newlist))
_l_(377615)