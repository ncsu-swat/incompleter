# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node(_n_(20664, "object", lambda: object)):
    _l_(20675)


    def __init__(self, data=None, next=None, prev=None):
        _l_(20674)

        _n_(20665, "self", lambda: self).data = _n_(20666, "data", lambda: data)
        _l_(20667)
        _n_(20668, "self", lambda: self).next = _n_(20669, "next", lambda: next)
        _l_(20670)
        _n_(20671, "self", lambda: self).prev = _n_(20672, "prev", lambda: prev)
        _l_(20673)

class doubly_linked_list(_n_(20676, "object", lambda: object)):
    _l_(20710)


    def __init__(self):
        _l_(20681)

        _n_(20677, "self", lambda: self).tail = None
        _l_(20678)
        _n_(20679, "self", lambda: self).count = 0
        _l_(20680)

    def append_item(self, data):
        _l_(20709)

        new_item = _c_(20684, _n_(20682, "Node", lambda: Node), _n_(20683, "data", lambda: data), None, None)
        _l_(20685)
        if _a_(20687, _n_(20686, "self", lambda: self), "head") is None:
            _l_(20706)

            _n_(20688, "self", lambda: self).head = _n_(20689, "new_item", lambda: new_item)
            _l_(20690)
            _n_(20691, "self", lambda: self).tail = _a_(20693, _n_(20692, "self", lambda: self), "head")
            _l_(20694)
        else:
            _n_(20695, "new_item", lambda: new_item).prev = _a_(20697, _n_(20696, "self", lambda: self), "tail")
            _l_(20698)
            _a_(20700, _n_(20699, "self", lambda: self), "tail").next = _n_(20701, "new_item", lambda: new_item)
            _l_(20702)
            _n_(20703, "self", lambda: self).tail = _n_(20704, "new_item", lambda: new_item)
            _l_(20705)
        _n_(20707, "self", lambda: self).count += 1
        _l_(20708)
items = _c_(20712, _n_(20711, "doubly_linked_list", lambda: doubly_linked_list))
_l_(20713)
_c_(20716, _a_(20715, _n_(20714, "items", lambda: items), "append_item"), 'PHP')
_l_(20717)
_c_(20720, _a_(20719, _n_(20718, "items", lambda: items), "append_item"), 'Python')
_l_(20721)
_c_(20724, _a_(20723, _n_(20722, "items", lambda: items), "append_item"), 'C#')
_l_(20725)
_c_(20728, _a_(20727, _n_(20726, "items", lambda: items), "append_item"), 'C++')
_l_(20729)
_c_(20732, _a_(20731, _n_(20730, "items", lambda: items), "append_item"), 'Java')
_l_(20733)
_c_(20736, _a_(20735, _n_(20734, "items", lambda: items), "append_item"), 'SQL')
_l_(20737)
_c_(20741, _n_(20738, "print", lambda: print), 'Number of items of the  Doubly linked list:', _a_(20740, _n_(20739, "items", lambda: items), "count"))
_l_(20742)