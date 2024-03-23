# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node(_n_(23952, "object", lambda: object)):
    _l_(23963)


    def __init__(self, data=None, next=None, prev=None):
        _l_(23962)

        _n_(23953, "self", lambda: self).data = _n_(23954, "data", lambda: data)
        _l_(23955)
        _n_(23956, "self", lambda: self).next = _n_(23957, "next", lambda: next)
        _l_(23958)
        _n_(23959, "self", lambda: self).prev = _n_(23960, "prev", lambda: prev)
        _l_(23961)

class doubly_linked_list(_n_(23964, "object", lambda: object)):
    _l_(24037)


    def __init__(self):
        _l_(23971)

        _n_(23965, "self", lambda: self).head = None
        _l_(23966)
        _n_(23967, "self", lambda: self).tail = None
        _l_(23968)
        _n_(23969, "self", lambda: self).count = 0
        _l_(23970)

    def append_item(self, data):
        _l_(23999)

        new_item = _c_(23974, _n_(23972, "Node", lambda: Node), _n_(23973, "data", lambda: data), None, None)
        _l_(23975)
        if _a_(23977, _n_(23976, "self", lambda: self), "head") is None:
            _l_(23996)

            _n_(23978, "self", lambda: self).head = _n_(23979, "new_item", lambda: new_item)
            _l_(23980)
            _n_(23981, "self", lambda: self).tail = _a_(23983, _n_(23982, "self", lambda: self), "head")
            _l_(23984)
        else:
            _n_(23985, "new_item", lambda: new_item).prev = _a_(23987, _n_(23986, "self", lambda: self), "tail")
            _l_(23988)
            _a_(23990, _n_(23989, "self", lambda: self), "tail").next = _n_(23991, "new_item", lambda: new_item)
            _l_(23992)
            _n_(23993, "self", lambda: self).tail = _n_(23994, "new_item", lambda: new_item)
            _l_(23995)
        _n_(23997, "self", lambda: self).count += 1
        _l_(23998)

    def print_foward(self):
        _l_(24008)

        for node in _c_(24002, _a_(24001, _n_(24000, "self", lambda: self), "iter")):
            _l_(24007)

            _c_(24005, _n_(24003, "print", lambda: print), _n_(24004, "node", lambda: node))
            _l_(24006)

    def print_backward(self):
        _l_(24022)

        current = _a_(24010, _n_(24009, "self", lambda: self), "tail")
        _l_(24011)
        while _n_(24012, "current", lambda: current):
            _l_(24021)

            _c_(24016, _n_(24013, "print", lambda: print), _a_(24015, _n_(24014, "current", lambda: current), "data"))
            _l_(24017)
            current = _a_(24019, _n_(24018, "current", lambda: current), "prev")
            _l_(24020)

    def iter(self):
        _l_(24036)

        current = _a_(24024, _n_(24023, "self", lambda: self), "head")
        _l_(24025)
        while _n_(24026, "current", lambda: current):
            _l_(24035)

            item_val = _a_(24028, _n_(24027, "current", lambda: current), "data")
            _l_(24029)
            current = _a_(24031, _n_(24030, "current", lambda: current), "next")
            _l_(24032)
            yield _n_(24033, "item_val", lambda: item_val)
            _l_(24034)
_c_(24040, _a_(24039, _n_(24038, "items", lambda: items), "append_item"), 'PHP')
_l_(24041)
_c_(24044, _a_(24043, _n_(24042, "items", lambda: items), "append_item"), 'Python')
_l_(24045)
_c_(24048, _a_(24047, _n_(24046, "items", lambda: items), "append_item"), 'C#')
_l_(24049)
_c_(24052, _a_(24051, _n_(24050, "items", lambda: items), "append_item"), 'C++')
_l_(24053)
_c_(24056, _a_(24055, _n_(24054, "items", lambda: items), "append_item"), 'Java')
_l_(24057)
_c_(24059, _n_(24058, "print", lambda: print), 'Print Items in the Doubly linked backwards:')
_l_(24060)
_c_(24063, _a_(24062, _n_(24061, "items", lambda: items), "print_backward"))
_l_(24064)