# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node(_n_(23615, "object", lambda: object)):
    _l_(23626)


    def __init__(self, data=None, next=None, prev=None):
        _l_(23625)

        _n_(23616, "self", lambda: self).data = _n_(23617, "data", lambda: data)
        _l_(23618)
        _n_(23619, "self", lambda: self).next = _n_(23620, "next", lambda: next)
        _l_(23621)
        _n_(23622, "self", lambda: self).prev = _n_(23623, "prev", lambda: prev)
        _l_(23624)

class doubly_linked_list(_n_(23627, "object", lambda: object)):
    _l_(23696)


    def __init__(self):
        _l_(23634)

        _n_(23628, "self", lambda: self).head = None
        _l_(23629)
        _n_(23630, "self", lambda: self).tail = None
        _l_(23631)
        _n_(23632, "self", lambda: self).count = 0
        _l_(23633)

    def append_item(self, data):
        _l_(23658)

        if _a_(23636, _n_(23635, "self", lambda: self), "head") is None:
            _l_(23655)

            _n_(23637, "self", lambda: self).head = _n_(23638, "new_item", lambda: new_item)
            _l_(23639)
            _n_(23640, "self", lambda: self).tail = _a_(23642, _n_(23641, "self", lambda: self), "head")
            _l_(23643)
        else:
            _n_(23644, "new_item", lambda: new_item).prev = _a_(23646, _n_(23645, "self", lambda: self), "tail")
            _l_(23647)
            _a_(23649, _n_(23648, "self", lambda: self), "tail").next = _n_(23650, "new_item", lambda: new_item)
            _l_(23651)
            _n_(23652, "self", lambda: self).tail = _n_(23653, "new_item", lambda: new_item)
            _l_(23654)
        _n_(23656, "self", lambda: self).count += 1
        _l_(23657)

    def print_foward(self):
        _l_(23667)

        for node in _c_(23661, _a_(23660, _n_(23659, "self", lambda: self), "iter")):
            _l_(23666)

            _c_(23664, _n_(23662, "print", lambda: print), _n_(23663, "node", lambda: node))
            _l_(23665)

    def print_backward(self):
        _l_(23681)

        current = _a_(23669, _n_(23668, "self", lambda: self), "tail")
        _l_(23670)
        while _n_(23671, "current", lambda: current):
            _l_(23680)

            _c_(23675, _n_(23672, "print", lambda: print), _a_(23674, _n_(23673, "current", lambda: current), "data"))
            _l_(23676)
            current = _a_(23678, _n_(23677, "current", lambda: current), "prev")
            _l_(23679)

    def iter(self):
        _l_(23695)

        current = _a_(23683, _n_(23682, "self", lambda: self), "head")
        _l_(23684)
        while _n_(23685, "current", lambda: current):
            _l_(23694)

            item_val = _a_(23687, _n_(23686, "current", lambda: current), "data")
            _l_(23688)
            current = _a_(23690, _n_(23689, "current", lambda: current), "next")
            _l_(23691)
            yield _n_(23692, "item_val", lambda: item_val)
            _l_(23693)
items = _c_(23698, _n_(23697, "doubly_linked_list", lambda: doubly_linked_list))
_l_(23699)
_c_(23702, _a_(23701, _n_(23700, "items", lambda: items), "append_item"), 'PHP')
_l_(23703)
_c_(23706, _a_(23705, _n_(23704, "items", lambda: items), "append_item"), 'Python')
_l_(23707)
_c_(23710, _a_(23709, _n_(23708, "items", lambda: items), "append_item"), 'C#')
_l_(23711)
_c_(23714, _a_(23713, _n_(23712, "items", lambda: items), "append_item"), 'C++')
_l_(23715)
_c_(23718, _a_(23717, _n_(23716, "items", lambda: items), "append_item"), 'Java')
_l_(23719)
_c_(23721, _n_(23720, "print", lambda: print), 'Print Items in the Doubly linked backwards:')
_l_(23722)
_c_(23725, _a_(23724, _n_(23723, "items", lambda: items), "print_backward"))
_l_(23726)