# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node(_n_(23840, "object", lambda: object)):
    _l_(23851)


    def __init__(self, data=None, next=None, prev=None):
        _l_(23850)

        _n_(23841, "self", lambda: self).data = _n_(23842, "data", lambda: data)
        _l_(23843)
        _n_(23844, "self", lambda: self).next = _n_(23845, "next", lambda: next)
        _l_(23846)
        _n_(23847, "self", lambda: self).prev = _n_(23848, "prev", lambda: prev)
        _l_(23849)

class doubly_linked_list(_n_(23852, "object", lambda: object)):
    _l_(23921)


    def __init__(self):
        _l_(23859)

        _n_(23853, "self", lambda: self).head = None
        _l_(23854)
        _n_(23855, "self", lambda: self).tail = None
        _l_(23856)
        _n_(23857, "self", lambda: self).count = 0
        _l_(23858)

    def append_item(self, data):
        _l_(23883)

        new_item = _c_(23862, _n_(23860, "Node", lambda: Node), _n_(23861, "data", lambda: data), None, None)
        _l_(23863)
        if _a_(23865, _n_(23864, "self", lambda: self), "head") is None:
            _l_(23880)

            _n_(23866, "self", lambda: self).head = _n_(23867, "new_item", lambda: new_item)
            _l_(23868)
        else:
            _n_(23869, "new_item", lambda: new_item).prev = _a_(23871, _n_(23870, "self", lambda: self), "tail")
            _l_(23872)
            _a_(23874, _n_(23873, "self", lambda: self), "tail").next = _n_(23875, "new_item", lambda: new_item)
            _l_(23876)
            _n_(23877, "self", lambda: self).tail = _n_(23878, "new_item", lambda: new_item)
            _l_(23879)
        _n_(23881, "self", lambda: self).count += 1
        _l_(23882)

    def print_foward(self):
        _l_(23892)

        for node in _c_(23886, _a_(23885, _n_(23884, "self", lambda: self), "iter")):
            _l_(23891)

            _c_(23889, _n_(23887, "print", lambda: print), _n_(23888, "node", lambda: node))
            _l_(23890)

    def print_backward(self):
        _l_(23906)

        current = _a_(23894, _n_(23893, "self", lambda: self), "tail")
        _l_(23895)
        while _n_(23896, "current", lambda: current):
            _l_(23905)

            _c_(23900, _n_(23897, "print", lambda: print), _a_(23899, _n_(23898, "current", lambda: current), "data"))
            _l_(23901)
            current = _a_(23903, _n_(23902, "current", lambda: current), "prev")
            _l_(23904)

    def iter(self):
        _l_(23920)

        current = _a_(23908, _n_(23907, "self", lambda: self), "head")
        _l_(23909)
        while _n_(23910, "current", lambda: current):
            _l_(23919)

            item_val = _a_(23912, _n_(23911, "current", lambda: current), "data")
            _l_(23913)
            current = _a_(23915, _n_(23914, "current", lambda: current), "next")
            _l_(23916)
            yield _n_(23917, "item_val", lambda: item_val)
            _l_(23918)
items = _c_(23923, _n_(23922, "doubly_linked_list", lambda: doubly_linked_list))
_l_(23924)
_c_(23927, _a_(23926, _n_(23925, "items", lambda: items), "append_item"), 'PHP')
_l_(23928)
_c_(23931, _a_(23930, _n_(23929, "items", lambda: items), "append_item"), 'Python')
_l_(23932)
_c_(23935, _a_(23934, _n_(23933, "items", lambda: items), "append_item"), 'C#')
_l_(23936)
_c_(23939, _a_(23938, _n_(23937, "items", lambda: items), "append_item"), 'C++')
_l_(23940)
_c_(23943, _a_(23942, _n_(23941, "items", lambda: items), "append_item"), 'Java')
_l_(23944)
_c_(23946, _n_(23945, "print", lambda: print), 'Print Items in the Doubly linked backwards:')
_l_(23947)
_c_(23950, _a_(23949, _n_(23948, "items", lambda: items), "print_backward"))
_l_(23951)