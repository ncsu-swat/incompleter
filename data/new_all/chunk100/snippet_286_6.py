# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node(_n_(24065, "object", lambda: object)):
    _l_(24076)


    def __init__(self, data=None, next=None, prev=None):
        _l_(24075)

        _n_(24066, "self", lambda: self).data = _n_(24067, "data", lambda: data)
        _l_(24068)
        _n_(24069, "self", lambda: self).next = _n_(24070, "next", lambda: next)
        _l_(24071)
        _n_(24072, "self", lambda: self).prev = _n_(24073, "prev", lambda: prev)
        _l_(24074)

class doubly_linked_list(_n_(24077, "object", lambda: object)):
    _l_(24148)


    def __init__(self):
        _l_(24082)

        _n_(24078, "self", lambda: self).tail = None
        _l_(24079)
        _n_(24080, "self", lambda: self).count = 0
        _l_(24081)

    def append_item(self, data):
        _l_(24110)

        new_item = _c_(24085, _n_(24083, "Node", lambda: Node), _n_(24084, "data", lambda: data), None, None)
        _l_(24086)
        if _a_(24088, _n_(24087, "self", lambda: self), "head") is None:
            _l_(24107)

            _n_(24089, "self", lambda: self).head = _n_(24090, "new_item", lambda: new_item)
            _l_(24091)
            _n_(24092, "self", lambda: self).tail = _a_(24094, _n_(24093, "self", lambda: self), "head")
            _l_(24095)
        else:
            _n_(24096, "new_item", lambda: new_item).prev = _a_(24098, _n_(24097, "self", lambda: self), "tail")
            _l_(24099)
            _a_(24101, _n_(24100, "self", lambda: self), "tail").next = _n_(24102, "new_item", lambda: new_item)
            _l_(24103)
            _n_(24104, "self", lambda: self).tail = _n_(24105, "new_item", lambda: new_item)
            _l_(24106)
        _n_(24108, "self", lambda: self).count += 1
        _l_(24109)

    def print_foward(self):
        _l_(24119)

        for node in _c_(24113, _a_(24112, _n_(24111, "self", lambda: self), "iter")):
            _l_(24118)

            _c_(24116, _n_(24114, "print", lambda: print), _n_(24115, "node", lambda: node))
            _l_(24117)

    def print_backward(self):
        _l_(24133)

        current = _a_(24121, _n_(24120, "self", lambda: self), "tail")
        _l_(24122)
        while _n_(24123, "current", lambda: current):
            _l_(24132)

            _c_(24127, _n_(24124, "print", lambda: print), _a_(24126, _n_(24125, "current", lambda: current), "data"))
            _l_(24128)
            current = _a_(24130, _n_(24129, "current", lambda: current), "prev")
            _l_(24131)

    def iter(self):
        _l_(24147)

        current = _a_(24135, _n_(24134, "self", lambda: self), "head")
        _l_(24136)
        while _n_(24137, "current", lambda: current):
            _l_(24146)

            item_val = _a_(24139, _n_(24138, "current", lambda: current), "data")
            _l_(24140)
            current = _a_(24142, _n_(24141, "current", lambda: current), "next")
            _l_(24143)
            yield _n_(24144, "item_val", lambda: item_val)
            _l_(24145)
items = _c_(24150, _n_(24149, "doubly_linked_list", lambda: doubly_linked_list))
_l_(24151)
_c_(24154, _a_(24153, _n_(24152, "items", lambda: items), "append_item"), 'PHP')
_l_(24155)
_c_(24158, _a_(24157, _n_(24156, "items", lambda: items), "append_item"), 'Python')
_l_(24159)
_c_(24162, _a_(24161, _n_(24160, "items", lambda: items), "append_item"), 'C#')
_l_(24163)
_c_(24166, _a_(24165, _n_(24164, "items", lambda: items), "append_item"), 'C++')
_l_(24167)
_c_(24170, _a_(24169, _n_(24168, "items", lambda: items), "append_item"), 'Java')
_l_(24171)
_c_(24173, _n_(24172, "print", lambda: print), 'Print Items in the Doubly linked backwards:')
_l_(24174)
_c_(24177, _a_(24176, _n_(24175, "items", lambda: items), "print_backward"))
_l_(24178)