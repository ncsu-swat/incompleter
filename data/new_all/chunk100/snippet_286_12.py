# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node(_n_(23501, "object", lambda: object)):
    _l_(23512)


    def __init__(self, data=None, next=None, prev=None):
        _l_(23511)

        _n_(23502, "self", lambda: self).data = _n_(23503, "data", lambda: data)
        _l_(23504)
        _n_(23505, "self", lambda: self).next = _n_(23506, "next", lambda: next)
        _l_(23507)
        _n_(23508, "self", lambda: self).prev = _n_(23509, "prev", lambda: prev)
        _l_(23510)

class doubly_linked_list(_n_(23513, "object", lambda: object)):
    _l_(23584)


    def __init__(self):
        _l_(23518)

        _n_(23514, "self", lambda: self).head = None
        _l_(23515)
        _n_(23516, "self", lambda: self).count = 0
        _l_(23517)

    def append_item(self, data):
        _l_(23546)

        new_item = _c_(23521, _n_(23519, "Node", lambda: Node), _n_(23520, "data", lambda: data), None, None)
        _l_(23522)
        if _a_(23524, _n_(23523, "self", lambda: self), "head") is None:
            _l_(23543)

            _n_(23525, "self", lambda: self).head = _n_(23526, "new_item", lambda: new_item)
            _l_(23527)
            _n_(23528, "self", lambda: self).tail = _a_(23530, _n_(23529, "self", lambda: self), "head")
            _l_(23531)
        else:
            _n_(23532, "new_item", lambda: new_item).prev = _a_(23534, _n_(23533, "self", lambda: self), "tail")
            _l_(23535)
            _a_(23537, _n_(23536, "self", lambda: self), "tail").next = _n_(23538, "new_item", lambda: new_item)
            _l_(23539)
            _n_(23540, "self", lambda: self).tail = _n_(23541, "new_item", lambda: new_item)
            _l_(23542)
        _n_(23544, "self", lambda: self).count += 1
        _l_(23545)

    def print_foward(self):
        _l_(23555)

        for node in _c_(23549, _a_(23548, _n_(23547, "self", lambda: self), "iter")):
            _l_(23554)

            _c_(23552, _n_(23550, "print", lambda: print), _n_(23551, "node", lambda: node))
            _l_(23553)

    def print_backward(self):
        _l_(23569)

        current = _a_(23557, _n_(23556, "self", lambda: self), "tail")
        _l_(23558)
        while _n_(23559, "current", lambda: current):
            _l_(23568)

            _c_(23563, _n_(23560, "print", lambda: print), _a_(23562, _n_(23561, "current", lambda: current), "data"))
            _l_(23564)
            current = _a_(23566, _n_(23565, "current", lambda: current), "prev")
            _l_(23567)

    def iter(self):
        _l_(23583)

        current = _a_(23571, _n_(23570, "self", lambda: self), "head")
        _l_(23572)
        while _n_(23573, "current", lambda: current):
            _l_(23582)

            item_val = _a_(23575, _n_(23574, "current", lambda: current), "data")
            _l_(23576)
            current = _a_(23578, _n_(23577, "current", lambda: current), "next")
            _l_(23579)
            yield _n_(23580, "item_val", lambda: item_val)
            _l_(23581)
items = _c_(23586, _n_(23585, "doubly_linked_list", lambda: doubly_linked_list))
_l_(23587)
_c_(23590, _a_(23589, _n_(23588, "items", lambda: items), "append_item"), 'PHP')
_l_(23591)
_c_(23594, _a_(23593, _n_(23592, "items", lambda: items), "append_item"), 'Python')
_l_(23595)
_c_(23598, _a_(23597, _n_(23596, "items", lambda: items), "append_item"), 'C#')
_l_(23599)
_c_(23602, _a_(23601, _n_(23600, "items", lambda: items), "append_item"), 'C++')
_l_(23603)
_c_(23606, _a_(23605, _n_(23604, "items", lambda: items), "append_item"), 'Java')
_l_(23607)
_c_(23609, _n_(23608, "print", lambda: print), 'Print Items in the Doubly linked backwards:')
_l_(23610)
_c_(23613, _a_(23612, _n_(23611, "items", lambda: items), "print_backward"))
_l_(23614)