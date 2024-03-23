# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node(_n_(13239, "object", lambda: object)):
    _l_(13250)


    def __init__(self, data=None, next=None, prev=None):
        _l_(13249)

        _n_(13240, "self", lambda: self).data = _n_(13241, "data", lambda: data)
        _l_(13242)
        _n_(13243, "self", lambda: self).next = _n_(13244, "next", lambda: next)
        _l_(13245)
        _n_(13246, "self", lambda: self).prev = _n_(13247, "prev", lambda: prev)
        _l_(13248)

class doubly_linked_list(_n_(13251, "object", lambda: object)):
    _l_(13308)


    def __init__(self):
        _l_(13256)

        _n_(13252, "self", lambda: self).head = None
        _l_(13253)
        _n_(13254, "self", lambda: self).count = 0
        _l_(13255)

    def append_item(self, data):
        _l_(13284)

        new_item = _c_(13259, _n_(13257, "Node", lambda: Node), _n_(13258, "data", lambda: data), None, None)
        _l_(13260)
        if _a_(13262, _n_(13261, "self", lambda: self), "head") is None:
            _l_(13281)

            _n_(13263, "self", lambda: self).head = _n_(13264, "new_item", lambda: new_item)
            _l_(13265)
            _n_(13266, "self", lambda: self).tail = _a_(13268, _n_(13267, "self", lambda: self), "head")
            _l_(13269)
        else:
            _n_(13270, "new_item", lambda: new_item).prev = _a_(13272, _n_(13271, "self", lambda: self), "tail")
            _l_(13273)
            _a_(13275, _n_(13274, "self", lambda: self), "tail").next = _n_(13276, "new_item", lambda: new_item)
            _l_(13277)
            _n_(13278, "self", lambda: self).tail = _n_(13279, "new_item", lambda: new_item)
            _l_(13280)
        _n_(13282, "self", lambda: self).count += 1
        _l_(13283)

    def print_foward(self):
        _l_(13293)

        for node in _c_(13287, _a_(13286, _n_(13285, "self", lambda: self), "iter")):
            _l_(13292)

            _c_(13290, _n_(13288, "print", lambda: print), _n_(13289, "node", lambda: node))
            _l_(13291)

    def iter(self):
        _l_(13307)

        current = _a_(13295, _n_(13294, "self", lambda: self), "head")
        _l_(13296)
        while _n_(13297, "current", lambda: current):
            _l_(13306)

            item_val = _a_(13299, _n_(13298, "current", lambda: current), "data")
            _l_(13300)
            current = _a_(13302, _n_(13301, "current", lambda: current), "next")
            _l_(13303)
            yield _n_(13304, "item_val", lambda: item_val)
            _l_(13305)
items = _c_(13310, _n_(13309, "doubly_linked_list", lambda: doubly_linked_list))
_l_(13311)
_c_(13314, _a_(13313, _n_(13312, "items", lambda: items), "append_item"), 'PHP')
_l_(13315)
_c_(13318, _a_(13317, _n_(13316, "items", lambda: items), "append_item"), 'Python')
_l_(13319)
_c_(13322, _a_(13321, _n_(13320, "items", lambda: items), "append_item"), 'C#')
_l_(13323)
_c_(13326, _a_(13325, _n_(13324, "items", lambda: items), "append_item"), 'C++')
_l_(13327)
_c_(13330, _a_(13329, _n_(13328, "items", lambda: items), "append_item"), 'Java')
_l_(13331)
_c_(13333, _n_(13332, "print", lambda: print), 'Items in the Doubly linked list: ')
_l_(13334)
_c_(13337, _a_(13336, _n_(13335, "items", lambda: items), "print_foward"))
_l_(13338)