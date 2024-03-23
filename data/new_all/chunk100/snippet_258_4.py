# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node(_n_(20587, "object", lambda: object)):
    _l_(20598)


    def __init__(self, data=None, next=None, prev=None):
        _l_(20597)

        _n_(20588, "self", lambda: self).data = _n_(20589, "data", lambda: data)
        _l_(20590)
        _n_(20591, "self", lambda: self).next = _n_(20592, "next", lambda: next)
        _l_(20593)
        _n_(20594, "self", lambda: self).prev = _n_(20595, "prev", lambda: prev)
        _l_(20596)

class doubly_linked_list(_n_(20599, "object", lambda: object)):
    _l_(20631)


    def __init__(self):
        _l_(20606)

        _n_(20600, "self", lambda: self).head = None
        _l_(20601)
        _n_(20602, "self", lambda: self).tail = None
        _l_(20603)
        _n_(20604, "self", lambda: self).count = 0
        _l_(20605)

    def append_item(self, data):
        _l_(20630)

        new_item = _c_(20609, _n_(20607, "Node", lambda: Node), _n_(20608, "data", lambda: data), None, None)
        _l_(20610)
        if _a_(20612, _n_(20611, "self", lambda: self), "head") is None:
            _l_(20627)

            _n_(20613, "self", lambda: self).head = _n_(20614, "new_item", lambda: new_item)
            _l_(20615)
        else:
            _n_(20616, "new_item", lambda: new_item).prev = _a_(20618, _n_(20617, "self", lambda: self), "tail")
            _l_(20619)
            _a_(20621, _n_(20620, "self", lambda: self), "tail").next = _n_(20622, "new_item", lambda: new_item)
            _l_(20623)
            _n_(20624, "self", lambda: self).tail = _n_(20625, "new_item", lambda: new_item)
            _l_(20626)
        _n_(20628, "self", lambda: self).count += 1
        _l_(20629)
items = _c_(20633, _n_(20632, "doubly_linked_list", lambda: doubly_linked_list))
_l_(20634)
_c_(20637, _a_(20636, _n_(20635, "items", lambda: items), "append_item"), 'PHP')
_l_(20638)
_c_(20641, _a_(20640, _n_(20639, "items", lambda: items), "append_item"), 'Python')
_l_(20642)
_c_(20645, _a_(20644, _n_(20643, "items", lambda: items), "append_item"), 'C#')
_l_(20646)
_c_(20649, _a_(20648, _n_(20647, "items", lambda: items), "append_item"), 'C++')
_l_(20650)
_c_(20653, _a_(20652, _n_(20651, "items", lambda: items), "append_item"), 'Java')
_l_(20654)
_c_(20657, _a_(20656, _n_(20655, "items", lambda: items), "append_item"), 'SQL')
_l_(20658)
_c_(20662, _n_(20659, "print", lambda: print), 'Number of items of the  Doubly linked list:', _a_(20661, _n_(20660, "items", lambda: items), "count"))
_l_(20663)