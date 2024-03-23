# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node(_n_(23162, "object", lambda: object)):
    _l_(23170)


    def __init__(self, data=None, next=None, prev=None):
        _l_(23169)

        _n_(23163, "self", lambda: self).data = _n_(23164, "data", lambda: data)
        _l_(23165)
        _n_(23166, "self", lambda: self).next = _n_(23167, "next", lambda: next)
        _l_(23168)

class doubly_linked_list(_n_(23171, "object", lambda: object)):
    _l_(23244)


    def __init__(self):
        _l_(23178)

        _n_(23172, "self", lambda: self).head = None
        _l_(23173)
        _n_(23174, "self", lambda: self).tail = None
        _l_(23175)
        _n_(23176, "self", lambda: self).count = 0
        _l_(23177)

    def append_item(self, data):
        _l_(23206)

        new_item = _c_(23181, _n_(23179, "Node", lambda: Node), _n_(23180, "data", lambda: data), None, None)
        _l_(23182)
        if _a_(23184, _n_(23183, "self", lambda: self), "head") is None:
            _l_(23203)

            _n_(23185, "self", lambda: self).head = _n_(23186, "new_item", lambda: new_item)
            _l_(23187)
            _n_(23188, "self", lambda: self).tail = _a_(23190, _n_(23189, "self", lambda: self), "head")
            _l_(23191)
        else:
            _n_(23192, "new_item", lambda: new_item).prev = _a_(23194, _n_(23193, "self", lambda: self), "tail")
            _l_(23195)
            _a_(23197, _n_(23196, "self", lambda: self), "tail").next = _n_(23198, "new_item", lambda: new_item)
            _l_(23199)
            _n_(23200, "self", lambda: self).tail = _n_(23201, "new_item", lambda: new_item)
            _l_(23202)
        _n_(23204, "self", lambda: self).count += 1
        _l_(23205)

    def print_foward(self):
        _l_(23215)

        for node in _c_(23209, _a_(23208, _n_(23207, "self", lambda: self), "iter")):
            _l_(23214)

            _c_(23212, _n_(23210, "print", lambda: print), _n_(23211, "node", lambda: node))
            _l_(23213)

    def print_backward(self):
        _l_(23229)

        current = _a_(23217, _n_(23216, "self", lambda: self), "tail")
        _l_(23218)
        while _n_(23219, "current", lambda: current):
            _l_(23228)

            _c_(23223, _n_(23220, "print", lambda: print), _a_(23222, _n_(23221, "current", lambda: current), "data"))
            _l_(23224)
            current = _a_(23226, _n_(23225, "current", lambda: current), "prev")
            _l_(23227)

    def iter(self):
        _l_(23243)

        current = _a_(23231, _n_(23230, "self", lambda: self), "head")
        _l_(23232)
        while _n_(23233, "current", lambda: current):
            _l_(23242)

            item_val = _a_(23235, _n_(23234, "current", lambda: current), "data")
            _l_(23236)
            current = _a_(23238, _n_(23237, "current", lambda: current), "next")
            _l_(23239)
            yield _n_(23240, "item_val", lambda: item_val)
            _l_(23241)
items = _c_(23246, _n_(23245, "doubly_linked_list", lambda: doubly_linked_list))
_l_(23247)
_c_(23250, _a_(23249, _n_(23248, "items", lambda: items), "append_item"), 'PHP')
_l_(23251)
_c_(23254, _a_(23253, _n_(23252, "items", lambda: items), "append_item"), 'Python')
_l_(23255)
_c_(23258, _a_(23257, _n_(23256, "items", lambda: items), "append_item"), 'C#')
_l_(23259)
_c_(23262, _a_(23261, _n_(23260, "items", lambda: items), "append_item"), 'C++')
_l_(23263)
_c_(23266, _a_(23265, _n_(23264, "items", lambda: items), "append_item"), 'Java')
_l_(23267)
_c_(23269, _n_(23268, "print", lambda: print), 'Print Items in the Doubly linked backwards:')
_l_(23270)
_c_(23273, _a_(23272, _n_(23271, "items", lambda: items), "print_backward"))
_l_(23274)