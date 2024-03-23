# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node(_n_(12942, "object", lambda: object)):
    _l_(12953)


    def __init__(self, data=None, next=None, prev=None):
        _l_(12952)

        _n_(12943, "self", lambda: self).data = _n_(12944, "data", lambda: data)
        _l_(12945)
        _n_(12946, "self", lambda: self).next = _n_(12947, "next", lambda: next)
        _l_(12948)
        _n_(12949, "self", lambda: self).prev = _n_(12950, "prev", lambda: prev)
        _l_(12951)

class doubly_linked_list(_n_(12954, "object", lambda: object)):
    _l_(13010)


    def __init__(self):
        _l_(12961)

        _n_(12955, "self", lambda: self).head = None
        _l_(12956)
        _n_(12957, "self", lambda: self).tail = None
        _l_(12958)
        _n_(12959, "self", lambda: self).count = 0
        _l_(12960)

    def append_item(self, data):
        _l_(12989)

        new_item = _c_(12964, _n_(12962, "Node", lambda: Node), _n_(12963, "data", lambda: data), None, None)
        _l_(12965)
        if _a_(12967, _n_(12966, "self", lambda: self), "head") is None:
            _l_(12986)

            _n_(12968, "self", lambda: self).head = _n_(12969, "new_item", lambda: new_item)
            _l_(12970)
            _n_(12971, "self", lambda: self).tail = _a_(12973, _n_(12972, "self", lambda: self), "head")
            _l_(12974)
        else:
            _n_(12975, "new_item", lambda: new_item).prev = _a_(12977, _n_(12976, "self", lambda: self), "tail")
            _l_(12978)
            _a_(12980, _n_(12979, "self", lambda: self), "tail").next = _n_(12981, "new_item", lambda: new_item)
            _l_(12982)
            _n_(12983, "self", lambda: self).tail = _n_(12984, "new_item", lambda: new_item)
            _l_(12985)
        _n_(12987, "self", lambda: self).count += 1
        _l_(12988)

    def print_foward(self):
        _l_(12998)

        for node in _c_(12992, _a_(12991, _n_(12990, "self", lambda: self), "iter")):
            _l_(12997)

            _c_(12995, _n_(12993, "print", lambda: print), _n_(12994, "node", lambda: node))
            _l_(12996)

    def iter(self):
        _l_(13009)

        while _n_(12999, "current", lambda: current):
            _l_(13008)

            item_val = _a_(13001, _n_(13000, "current", lambda: current), "data")
            _l_(13002)
            current = _a_(13004, _n_(13003, "current", lambda: current), "next")
            _l_(13005)
            yield _n_(13006, "item_val", lambda: item_val)
            _l_(13007)
items = _c_(13012, _n_(13011, "doubly_linked_list", lambda: doubly_linked_list))
_l_(13013)
_c_(13016, _a_(13015, _n_(13014, "items", lambda: items), "append_item"), 'PHP')
_l_(13017)
_c_(13020, _a_(13019, _n_(13018, "items", lambda: items), "append_item"), 'Python')
_l_(13021)
_c_(13024, _a_(13023, _n_(13022, "items", lambda: items), "append_item"), 'C#')
_l_(13025)
_c_(13028, _a_(13027, _n_(13026, "items", lambda: items), "append_item"), 'C++')
_l_(13029)
_c_(13032, _a_(13031, _n_(13030, "items", lambda: items), "append_item"), 'Java')
_l_(13033)
_c_(13035, _n_(13034, "print", lambda: print), 'Items in the Doubly linked list: ')
_l_(13036)
_c_(13039, _a_(13038, _n_(13037, "items", lambda: items), "print_foward"))
_l_(13040)