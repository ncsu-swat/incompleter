# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node(_n_(23048, "object", lambda: object)):
    _l_(23059)


    def __init__(self, data=None, next=None, prev=None):
        _l_(23058)

        _n_(23049, "self", lambda: self).data = _n_(23050, "data", lambda: data)
        _l_(23051)
        _n_(23052, "self", lambda: self).next = _n_(23053, "next", lambda: next)
        _l_(23054)
        _n_(23055, "self", lambda: self).prev = _n_(23056, "prev", lambda: prev)
        _l_(23057)

class doubly_linked_list(_n_(23060, "object", lambda: object)):
    _l_(23131)


    def __init__(self):
        _l_(23065)

        _n_(23061, "self", lambda: self).head = None
        _l_(23062)
        _n_(23063, "self", lambda: self).tail = None
        _l_(23064)

    def append_item(self, data):
        _l_(23093)

        new_item = _c_(23068, _n_(23066, "Node", lambda: Node), _n_(23067, "data", lambda: data), None, None)
        _l_(23069)
        if _a_(23071, _n_(23070, "self", lambda: self), "head") is None:
            _l_(23090)

            _n_(23072, "self", lambda: self).head = _n_(23073, "new_item", lambda: new_item)
            _l_(23074)
            _n_(23075, "self", lambda: self).tail = _a_(23077, _n_(23076, "self", lambda: self), "head")
            _l_(23078)
        else:
            _n_(23079, "new_item", lambda: new_item).prev = _a_(23081, _n_(23080, "self", lambda: self), "tail")
            _l_(23082)
            _a_(23084, _n_(23083, "self", lambda: self), "tail").next = _n_(23085, "new_item", lambda: new_item)
            _l_(23086)
            _n_(23087, "self", lambda: self).tail = _n_(23088, "new_item", lambda: new_item)
            _l_(23089)
        _n_(23091, "self", lambda: self).count += 1
        _l_(23092)

    def print_foward(self):
        _l_(23102)

        for node in _c_(23096, _a_(23095, _n_(23094, "self", lambda: self), "iter")):
            _l_(23101)

            _c_(23099, _n_(23097, "print", lambda: print), _n_(23098, "node", lambda: node))
            _l_(23100)

    def print_backward(self):
        _l_(23116)

        current = _a_(23104, _n_(23103, "self", lambda: self), "tail")
        _l_(23105)
        while _n_(23106, "current", lambda: current):
            _l_(23115)

            _c_(23110, _n_(23107, "print", lambda: print), _a_(23109, _n_(23108, "current", lambda: current), "data"))
            _l_(23111)
            current = _a_(23113, _n_(23112, "current", lambda: current), "prev")
            _l_(23114)

    def iter(self):
        _l_(23130)

        current = _a_(23118, _n_(23117, "self", lambda: self), "head")
        _l_(23119)
        while _n_(23120, "current", lambda: current):
            _l_(23129)

            item_val = _a_(23122, _n_(23121, "current", lambda: current), "data")
            _l_(23123)
            current = _a_(23125, _n_(23124, "current", lambda: current), "next")
            _l_(23126)
            yield _n_(23127, "item_val", lambda: item_val)
            _l_(23128)
items = _c_(23133, _n_(23132, "doubly_linked_list", lambda: doubly_linked_list))
_l_(23134)
_c_(23137, _a_(23136, _n_(23135, "items", lambda: items), "append_item"), 'PHP')
_l_(23138)
_c_(23141, _a_(23140, _n_(23139, "items", lambda: items), "append_item"), 'Python')
_l_(23142)
_c_(23145, _a_(23144, _n_(23143, "items", lambda: items), "append_item"), 'C#')
_l_(23146)
_c_(23149, _a_(23148, _n_(23147, "items", lambda: items), "append_item"), 'C++')
_l_(23150)
_c_(23153, _a_(23152, _n_(23151, "items", lambda: items), "append_item"), 'Java')
_l_(23154)
_c_(23156, _n_(23155, "print", lambda: print), 'Print Items in the Doubly linked backwards:')
_l_(23157)
_c_(23160, _a_(23159, _n_(23158, "items", lambda: items), "print_backward"))
_l_(23161)