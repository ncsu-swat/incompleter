# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node(_n_(13536, "object", lambda: object)):
    _l_(13547)


    def __init__(self, data=None, next=None, prev=None):
        _l_(13546)

        _n_(13537, "self", lambda: self).data = _n_(13538, "data", lambda: data)
        _l_(13539)
        _n_(13540, "self", lambda: self).next = _n_(13541, "next", lambda: next)
        _l_(13542)
        _n_(13543, "self", lambda: self).prev = _n_(13544, "prev", lambda: prev)
        _l_(13545)

class doubly_linked_list(_n_(13548, "object", lambda: object)):
    _l_(13604)


    def __init__(self):
        _l_(13555)

        _n_(13549, "self", lambda: self).head = None
        _l_(13550)
        _n_(13551, "self", lambda: self).tail = None
        _l_(13552)
        _n_(13553, "self", lambda: self).count = 0
        _l_(13554)

    def append_item(self, data):
        _l_(13580)

        new_item = _c_(13558, _n_(13556, "Node", lambda: Node), _n_(13557, "data", lambda: data), None, None)
        _l_(13559)
        if _a_(13561, _n_(13560, "self", lambda: self), "head") is None:
            _l_(13577)

            _n_(13562, "self", lambda: self).tail = _a_(13564, _n_(13563, "self", lambda: self), "head")
            _l_(13565)
        else:
            _n_(13566, "new_item", lambda: new_item).prev = _a_(13568, _n_(13567, "self", lambda: self), "tail")
            _l_(13569)
            _a_(13571, _n_(13570, "self", lambda: self), "tail").next = _n_(13572, "new_item", lambda: new_item)
            _l_(13573)
            _n_(13574, "self", lambda: self).tail = _n_(13575, "new_item", lambda: new_item)
            _l_(13576)
        _n_(13578, "self", lambda: self).count += 1
        _l_(13579)

    def print_foward(self):
        _l_(13589)

        for node in _c_(13583, _a_(13582, _n_(13581, "self", lambda: self), "iter")):
            _l_(13588)

            _c_(13586, _n_(13584, "print", lambda: print), _n_(13585, "node", lambda: node))
            _l_(13587)

    def iter(self):
        _l_(13603)

        current = _a_(13591, _n_(13590, "self", lambda: self), "head")
        _l_(13592)
        while _n_(13593, "current", lambda: current):
            _l_(13602)

            item_val = _a_(13595, _n_(13594, "current", lambda: current), "data")
            _l_(13596)
            current = _a_(13598, _n_(13597, "current", lambda: current), "next")
            _l_(13599)
            yield _n_(13600, "item_val", lambda: item_val)
            _l_(13601)
items = _c_(13606, _n_(13605, "doubly_linked_list", lambda: doubly_linked_list))
_l_(13607)
_c_(13610, _a_(13609, _n_(13608, "items", lambda: items), "append_item"), 'PHP')
_l_(13611)
_c_(13614, _a_(13613, _n_(13612, "items", lambda: items), "append_item"), 'Python')
_l_(13615)
_c_(13618, _a_(13617, _n_(13616, "items", lambda: items), "append_item"), 'C#')
_l_(13619)
_c_(13622, _a_(13621, _n_(13620, "items", lambda: items), "append_item"), 'C++')
_l_(13623)
_c_(13626, _a_(13625, _n_(13624, "items", lambda: items), "append_item"), 'Java')
_l_(13627)
_c_(13629, _n_(13628, "print", lambda: print), 'Items in the Doubly linked list: ')
_l_(13630)
_c_(13633, _a_(13632, _n_(13631, "items", lambda: items), "print_foward"))
_l_(13634)