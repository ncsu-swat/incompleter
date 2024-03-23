# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node(_n_(20509, "object", lambda: object)):
    _l_(20520)


    def __init__(self, data=None, next=None, prev=None):
        _l_(20519)

        _n_(20510, "self", lambda: self).data = _n_(20511, "data", lambda: data)
        _l_(20512)
        _n_(20513, "self", lambda: self).next = _n_(20514, "next", lambda: next)
        _l_(20515)
        _n_(20516, "self", lambda: self).prev = _n_(20517, "prev", lambda: prev)
        _l_(20518)

class doubly_linked_list(_n_(20521, "object", lambda: object)):
    _l_(20554)


    def __init__(self):
        _l_(20528)

        _n_(20522, "self", lambda: self).head = None
        _l_(20523)
        _n_(20524, "self", lambda: self).tail = None
        _l_(20525)
        _n_(20526, "self", lambda: self).count = 0
        _l_(20527)

    def append_item(self, data):
        _l_(20553)

        new_item = _c_(20531, _n_(20529, "Node", lambda: Node), _n_(20530, "data", lambda: data), None, None)
        _l_(20532)
        if _a_(20534, _n_(20533, "self", lambda: self), "head") is None:
            _l_(20550)

            _n_(20535, "self", lambda: self).tail = _a_(20537, _n_(20536, "self", lambda: self), "head")
            _l_(20538)
        else:
            _n_(20539, "new_item", lambda: new_item).prev = _a_(20541, _n_(20540, "self", lambda: self), "tail")
            _l_(20542)
            _a_(20544, _n_(20543, "self", lambda: self), "tail").next = _n_(20545, "new_item", lambda: new_item)
            _l_(20546)
            _n_(20547, "self", lambda: self).tail = _n_(20548, "new_item", lambda: new_item)
            _l_(20549)
        _n_(20551, "self", lambda: self).count += 1
        _l_(20552)
items = _c_(20556, _n_(20555, "doubly_linked_list", lambda: doubly_linked_list))
_l_(20557)
_c_(20560, _a_(20559, _n_(20558, "items", lambda: items), "append_item"), 'PHP')
_l_(20561)
_c_(20564, _a_(20563, _n_(20562, "items", lambda: items), "append_item"), 'Python')
_l_(20565)
_c_(20568, _a_(20567, _n_(20566, "items", lambda: items), "append_item"), 'C#')
_l_(20569)
_c_(20572, _a_(20571, _n_(20570, "items", lambda: items), "append_item"), 'C++')
_l_(20573)
_c_(20576, _a_(20575, _n_(20574, "items", lambda: items), "append_item"), 'Java')
_l_(20577)
_c_(20580, _a_(20579, _n_(20578, "items", lambda: items), "append_item"), 'SQL')
_l_(20581)
_c_(20585, _n_(20582, "print", lambda: print), 'Number of items of the  Doubly linked list:', _a_(20584, _n_(20583, "items", lambda: items), "count"))
_l_(20586)