# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node(_n_(13931, "object", lambda: object)):
    _l_(13942)


    def __init__(self, data=None, next=None, prev=None):
        _l_(13941)

        _n_(13932, "self", lambda: self).data = _n_(13933, "data", lambda: data)
        _l_(13934)
        _n_(13935, "self", lambda: self).next = _n_(13936, "next", lambda: next)
        _l_(13937)
        _n_(13938, "self", lambda: self).prev = _n_(13939, "prev", lambda: prev)
        _l_(13940)

class doubly_linked_list(_n_(13943, "object", lambda: object)):
    _l_(14000)


    def __init__(self):
        _l_(13948)

        _n_(13944, "self", lambda: self).tail = None
        _l_(13945)
        _n_(13946, "self", lambda: self).count = 0
        _l_(13947)

    def append_item(self, data):
        _l_(13976)

        new_item = _c_(13951, _n_(13949, "Node", lambda: Node), _n_(13950, "data", lambda: data), None, None)
        _l_(13952)
        if _a_(13954, _n_(13953, "self", lambda: self), "head") is None:
            _l_(13973)

            _n_(13955, "self", lambda: self).head = _n_(13956, "new_item", lambda: new_item)
            _l_(13957)
            _n_(13958, "self", lambda: self).tail = _a_(13960, _n_(13959, "self", lambda: self), "head")
            _l_(13961)
        else:
            _n_(13962, "new_item", lambda: new_item).prev = _a_(13964, _n_(13963, "self", lambda: self), "tail")
            _l_(13965)
            _a_(13967, _n_(13966, "self", lambda: self), "tail").next = _n_(13968, "new_item", lambda: new_item)
            _l_(13969)
            _n_(13970, "self", lambda: self).tail = _n_(13971, "new_item", lambda: new_item)
            _l_(13972)
        _n_(13974, "self", lambda: self).count += 1
        _l_(13975)

    def print_foward(self):
        _l_(13985)

        for node in _c_(13979, _a_(13978, _n_(13977, "self", lambda: self), "iter")):
            _l_(13984)

            _c_(13982, _n_(13980, "print", lambda: print), _n_(13981, "node", lambda: node))
            _l_(13983)

    def iter(self):
        _l_(13999)

        current = _a_(13987, _n_(13986, "self", lambda: self), "head")
        _l_(13988)
        while _n_(13989, "current", lambda: current):
            _l_(13998)

            item_val = _a_(13991, _n_(13990, "current", lambda: current), "data")
            _l_(13992)
            current = _a_(13994, _n_(13993, "current", lambda: current), "next")
            _l_(13995)
            yield _n_(13996, "item_val", lambda: item_val)
            _l_(13997)
items = _c_(14002, _n_(14001, "doubly_linked_list", lambda: doubly_linked_list))
_l_(14003)
_c_(14006, _a_(14005, _n_(14004, "items", lambda: items), "append_item"), 'PHP')
_l_(14007)
_c_(14010, _a_(14009, _n_(14008, "items", lambda: items), "append_item"), 'Python')
_l_(14011)
_c_(14014, _a_(14013, _n_(14012, "items", lambda: items), "append_item"), 'C#')
_l_(14015)
_c_(14018, _a_(14017, _n_(14016, "items", lambda: items), "append_item"), 'C++')
_l_(14019)
_c_(14022, _a_(14021, _n_(14020, "items", lambda: items), "append_item"), 'Java')
_l_(14023)
_c_(14025, _n_(14024, "print", lambda: print), 'Items in the Doubly linked list: ')
_l_(14026)
_c_(14029, _a_(14028, _n_(14027, "items", lambda: items), "print_foward"))
_l_(14030)