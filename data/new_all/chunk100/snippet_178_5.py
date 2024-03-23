# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node(_n_(13635, "object", lambda: object)):
    _l_(13646)


    def __init__(self, data=None, next=None, prev=None):
        _l_(13645)

        _n_(13636, "self", lambda: self).data = _n_(13637, "data", lambda: data)
        _l_(13638)
        _n_(13639, "self", lambda: self).next = _n_(13640, "next", lambda: next)
        _l_(13641)
        _n_(13642, "self", lambda: self).prev = _n_(13643, "prev", lambda: prev)
        _l_(13644)

class doubly_linked_list(_n_(13647, "object", lambda: object)):
    _l_(13702)


    def __init__(self):
        _l_(13654)

        _n_(13648, "self", lambda: self).head = None
        _l_(13649)
        _n_(13650, "self", lambda: self).tail = None
        _l_(13651)
        _n_(13652, "self", lambda: self).count = 0
        _l_(13653)

    def append_item(self, data):
        _l_(13678)

        new_item = _c_(13657, _n_(13655, "Node", lambda: Node), _n_(13656, "data", lambda: data), None, None)
        _l_(13658)
        if _a_(13660, _n_(13659, "self", lambda: self), "head") is None:
            _l_(13675)

            _n_(13661, "self", lambda: self).head = _n_(13662, "new_item", lambda: new_item)
            _l_(13663)
        else:
            _n_(13664, "new_item", lambda: new_item).prev = _a_(13666, _n_(13665, "self", lambda: self), "tail")
            _l_(13667)
            _a_(13669, _n_(13668, "self", lambda: self), "tail").next = _n_(13670, "new_item", lambda: new_item)
            _l_(13671)
            _n_(13672, "self", lambda: self).tail = _n_(13673, "new_item", lambda: new_item)
            _l_(13674)
        _n_(13676, "self", lambda: self).count += 1
        _l_(13677)

    def print_foward(self):
        _l_(13687)

        for node in _c_(13681, _a_(13680, _n_(13679, "self", lambda: self), "iter")):
            _l_(13686)

            _c_(13684, _n_(13682, "print", lambda: print), _n_(13683, "node", lambda: node))
            _l_(13685)

    def iter(self):
        _l_(13701)

        current = _a_(13689, _n_(13688, "self", lambda: self), "head")
        _l_(13690)
        while _n_(13691, "current", lambda: current):
            _l_(13700)

            item_val = _a_(13693, _n_(13692, "current", lambda: current), "data")
            _l_(13694)
            current = _a_(13696, _n_(13695, "current", lambda: current), "next")
            _l_(13697)
            yield _n_(13698, "item_val", lambda: item_val)
            _l_(13699)
items = _c_(13704, _n_(13703, "doubly_linked_list", lambda: doubly_linked_list))
_l_(13705)
_c_(13708, _a_(13707, _n_(13706, "items", lambda: items), "append_item"), 'PHP')
_l_(13709)
_c_(13712, _a_(13711, _n_(13710, "items", lambda: items), "append_item"), 'Python')
_l_(13713)
_c_(13716, _a_(13715, _n_(13714, "items", lambda: items), "append_item"), 'C#')
_l_(13717)
_c_(13720, _a_(13719, _n_(13718, "items", lambda: items), "append_item"), 'C++')
_l_(13721)
_c_(13724, _a_(13723, _n_(13722, "items", lambda: items), "append_item"), 'Java')
_l_(13725)
_c_(13727, _n_(13726, "print", lambda: print), 'Items in the Doubly linked list: ')
_l_(13728)
_c_(13731, _a_(13730, _n_(13729, "items", lambda: items), "print_foward"))
_l_(13732)