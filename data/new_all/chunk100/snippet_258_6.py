# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node(_n_(20743, "object", lambda: object)):
    _l_(20751)


    def __init__(self, data=None, next=None, prev=None):
        _l_(20750)

        _n_(20744, "self", lambda: self).data = _n_(20745, "data", lambda: data)
        _l_(20746)
        _n_(20747, "self", lambda: self).prev = _n_(20748, "prev", lambda: prev)
        _l_(20749)

class doubly_linked_list(_n_(20752, "object", lambda: object)):
    _l_(20788)


    def __init__(self):
        _l_(20759)

        _n_(20753, "self", lambda: self).head = None
        _l_(20754)
        _n_(20755, "self", lambda: self).tail = None
        _l_(20756)
        _n_(20757, "self", lambda: self).count = 0
        _l_(20758)

    def append_item(self, data):
        _l_(20787)

        new_item = _c_(20762, _n_(20760, "Node", lambda: Node), _n_(20761, "data", lambda: data), None, None)
        _l_(20763)
        if _a_(20765, _n_(20764, "self", lambda: self), "head") is None:
            _l_(20784)

            _n_(20766, "self", lambda: self).head = _n_(20767, "new_item", lambda: new_item)
            _l_(20768)
            _n_(20769, "self", lambda: self).tail = _a_(20771, _n_(20770, "self", lambda: self), "head")
            _l_(20772)
        else:
            _n_(20773, "new_item", lambda: new_item).prev = _a_(20775, _n_(20774, "self", lambda: self), "tail")
            _l_(20776)
            _a_(20778, _n_(20777, "self", lambda: self), "tail").next = _n_(20779, "new_item", lambda: new_item)
            _l_(20780)
            _n_(20781, "self", lambda: self).tail = _n_(20782, "new_item", lambda: new_item)
            _l_(20783)
        _n_(20785, "self", lambda: self).count += 1
        _l_(20786)
items = _c_(20790, _n_(20789, "doubly_linked_list", lambda: doubly_linked_list))
_l_(20791)
_c_(20794, _a_(20793, _n_(20792, "items", lambda: items), "append_item"), 'PHP')
_l_(20795)
_c_(20798, _a_(20797, _n_(20796, "items", lambda: items), "append_item"), 'Python')
_l_(20799)
_c_(20802, _a_(20801, _n_(20800, "items", lambda: items), "append_item"), 'C#')
_l_(20803)
_c_(20806, _a_(20805, _n_(20804, "items", lambda: items), "append_item"), 'C++')
_l_(20807)
_c_(20810, _a_(20809, _n_(20808, "items", lambda: items), "append_item"), 'Java')
_l_(20811)
_c_(20814, _a_(20813, _n_(20812, "items", lambda: items), "append_item"), 'SQL')
_l_(20815)
_c_(20819, _n_(20816, "print", lambda: print), 'Number of items of the  Doubly linked list:', _a_(20818, _n_(20817, "items", lambda: items), "count"))
_l_(20820)