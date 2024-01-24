# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75357239/python-error-attributeerror-int-object-has-no-attribute-find
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
contents = _c_(621512, _a_(621511, _c_(621510, _a_(621509, _n_(621508, "soup", lambda: soup), "find"), 'table'), "find_all"), 'a')
_l_(621513)


for i in _n_(621514, "contents", lambda: contents):
        _l_(621540)

        _c_(621516, _n_(621515, "print", lambda: print), "---------------------------")
        _l_(621517)
        link = _c_(621522, _a_(621521, _c_(621520, _a_(621519, _n_(621518, "i", lambda: i), "find"), "td", class_= "cafecoffee"), "find_all"), "a")[0]
        _l_(621523)
        _c_(621525, _n_(621524, "print", lambda: print), "link :")
        _l_(621526)
        _c_(621529, _n_(621527, "print", lambda: print), "naver.com" + _n_(621528, "link", lambda: link))
        _l_(621530)

        title = _c_(621533, _a_(621532, _n_(621531, "i", lambda: i), "find"), "td")
        _l_(621534)
        _c_(621538, _n_(621535, "print", lambda: print), "title:",_a_(621537, _n_(621536, "title", lambda: title), "text"))
        _l_(621539)