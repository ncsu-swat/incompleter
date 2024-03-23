# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node(_n_(24405, "object", lambda: object)):
    _l_(24416)


    def __init__(self, data=None, next=None, prev=None):
        _l_(24415)

        _n_(24406, "self", lambda: self).data = _n_(24407, "data", lambda: data)
        _l_(24408)
        _n_(24409, "self", lambda: self).next = _n_(24410, "next", lambda: next)
        _l_(24411)
        _n_(24412, "self", lambda: self).prev = _n_(24413, "prev", lambda: prev)
        _l_(24414)

class doubly_linked_list(_n_(24417, "object", lambda: object)):
    _l_(24487)


    def __init__(self):
        _l_(24424)

        _n_(24418, "self", lambda: self).head = None
        _l_(24419)
        _n_(24420, "self", lambda: self).tail = None
        _l_(24421)
        _n_(24422, "self", lambda: self).count = 0
        _l_(24423)

    def append_item(self, data):
        _l_(24452)

        new_item = _c_(24427, _n_(24425, "Node", lambda: Node), _n_(24426, "data", lambda: data), None, None)
        _l_(24428)
        if _a_(24430, _n_(24429, "self", lambda: self), "head") is None:
            _l_(24449)

            _n_(24431, "self", lambda: self).head = _n_(24432, "new_item", lambda: new_item)
            _l_(24433)
            _n_(24434, "self", lambda: self).tail = _a_(24436, _n_(24435, "self", lambda: self), "head")
            _l_(24437)
        else:
            _n_(24438, "new_item", lambda: new_item).prev = _a_(24440, _n_(24439, "self", lambda: self), "tail")
            _l_(24441)
            _a_(24443, _n_(24442, "self", lambda: self), "tail").next = _n_(24444, "new_item", lambda: new_item)
            _l_(24445)
            _n_(24446, "self", lambda: self).tail = _n_(24447, "new_item", lambda: new_item)
            _l_(24448)
        _n_(24450, "self", lambda: self).count += 1
        _l_(24451)

    def print_foward(self):
        _l_(24461)

        for node in _c_(24455, _a_(24454, _n_(24453, "self", lambda: self), "iter")):
            _l_(24460)

            _c_(24458, _n_(24456, "print", lambda: print), _n_(24457, "node", lambda: node))
            _l_(24459)

    def print_backward(self):
        _l_(24472)

        current = _a_(24463, _n_(24462, "self", lambda: self), "tail")
        _l_(24464)
        while _n_(24465, "current", lambda: current):
            _l_(24471)

            _c_(24469, _n_(24466, "print", lambda: print), _a_(24468, _n_(24467, "current", lambda: current), "data"))
            _l_(24470)

    def iter(self):
        _l_(24486)

        current = _a_(24474, _n_(24473, "self", lambda: self), "head")
        _l_(24475)
        while _n_(24476, "current", lambda: current):
            _l_(24485)

            item_val = _a_(24478, _n_(24477, "current", lambda: current), "data")
            _l_(24479)
            current = _a_(24481, _n_(24480, "current", lambda: current), "next")
            _l_(24482)
            yield _n_(24483, "item_val", lambda: item_val)
            _l_(24484)
items = _c_(24489, _n_(24488, "doubly_linked_list", lambda: doubly_linked_list))
_l_(24490)
_c_(24493, _a_(24492, _n_(24491, "items", lambda: items), "append_item"), 'PHP')
_l_(24494)
_c_(24497, _a_(24496, _n_(24495, "items", lambda: items), "append_item"), 'Python')
_l_(24498)
_c_(24501, _a_(24500, _n_(24499, "items", lambda: items), "append_item"), 'C#')
_l_(24502)
_c_(24505, _a_(24504, _n_(24503, "items", lambda: items), "append_item"), 'C++')
_l_(24506)
_c_(24509, _a_(24508, _n_(24507, "items", lambda: items), "append_item"), 'Java')
_l_(24510)
_c_(24512, _n_(24511, "print", lambda: print), 'Print Items in the Doubly linked backwards:')
_l_(24513)
_c_(24516, _a_(24515, _n_(24514, "items", lambda: items), "print_backward"))
_l_(24517)