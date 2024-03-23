# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node(_n_(14031, "object", lambda: object)):
    _l_(14042)


    def __init__(self, data=None, next=None, prev=None):
        _l_(14041)

        _n_(14032, "self", lambda: self).data = _n_(14033, "data", lambda: data)
        _l_(14034)
        _n_(14035, "self", lambda: self).next = _n_(14036, "next", lambda: next)
        _l_(14037)
        _n_(14038, "self", lambda: self).prev = _n_(14039, "prev", lambda: prev)
        _l_(14040)

class doubly_linked_list(_n_(14043, "object", lambda: object)):
    _l_(14099)


    def __init__(self):
        _l_(14050)

        _n_(14044, "self", lambda: self).head = None
        _l_(14045)
        _n_(14046, "self", lambda: self).tail = None
        _l_(14047)
        _n_(14048, "self", lambda: self).count = 0
        _l_(14049)

    def append_item(self, data):
        _l_(14078)

        new_item = _c_(14053, _n_(14051, "Node", lambda: Node), _n_(14052, "data", lambda: data), None, None)
        _l_(14054)
        if _a_(14056, _n_(14055, "self", lambda: self), "head") is None:
            _l_(14075)

            _n_(14057, "self", lambda: self).head = _n_(14058, "new_item", lambda: new_item)
            _l_(14059)
            _n_(14060, "self", lambda: self).tail = _a_(14062, _n_(14061, "self", lambda: self), "head")
            _l_(14063)
        else:
            _n_(14064, "new_item", lambda: new_item).prev = _a_(14066, _n_(14065, "self", lambda: self), "tail")
            _l_(14067)
            _a_(14069, _n_(14068, "self", lambda: self), "tail").next = _n_(14070, "new_item", lambda: new_item)
            _l_(14071)
            _n_(14072, "self", lambda: self).tail = _n_(14073, "new_item", lambda: new_item)
            _l_(14074)
        _n_(14076, "self", lambda: self).count += 1
        _l_(14077)

    def print_foward(self):
        _l_(14087)

        for node in _c_(14081, _a_(14080, _n_(14079, "self", lambda: self), "iter")):
            _l_(14086)

            _c_(14084, _n_(14082, "print", lambda: print), _n_(14083, "node", lambda: node))
            _l_(14085)

    def iter(self):
        _l_(14098)

        current = _a_(14089, _n_(14088, "self", lambda: self), "head")
        _l_(14090)
        while _n_(14091, "current", lambda: current):
            _l_(14097)

            item_val = _a_(14093, _n_(14092, "current", lambda: current), "data")
            _l_(14094)
            yield _n_(14095, "item_val", lambda: item_val)
            _l_(14096)
items = _c_(14101, _n_(14100, "doubly_linked_list", lambda: doubly_linked_list))
_l_(14102)
_c_(14105, _a_(14104, _n_(14103, "items", lambda: items), "append_item"), 'PHP')
_l_(14106)
_c_(14109, _a_(14108, _n_(14107, "items", lambda: items), "append_item"), 'Python')
_l_(14110)
_c_(14113, _a_(14112, _n_(14111, "items", lambda: items), "append_item"), 'C#')
_l_(14114)
_c_(14117, _a_(14116, _n_(14115, "items", lambda: items), "append_item"), 'C++')
_l_(14118)
_c_(14121, _a_(14120, _n_(14119, "items", lambda: items), "append_item"), 'Java')
_l_(14122)
_c_(14124, _n_(14123, "print", lambda: print), 'Items in the Doubly linked list: ')
_l_(14125)
_c_(14128, _a_(14127, _n_(14126, "items", lambda: items), "print_foward"))
_l_(14129)