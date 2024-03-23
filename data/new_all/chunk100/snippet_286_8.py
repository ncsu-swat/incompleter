# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node(_n_(24292, "object", lambda: object)):
    _l_(24303)


    def __init__(self, data=None, next=None, prev=None):
        _l_(24302)

        _n_(24293, "self", lambda: self).data = _n_(24294, "data", lambda: data)
        _l_(24295)
        _n_(24296, "self", lambda: self).next = _n_(24297, "next", lambda: next)
        _l_(24298)
        _n_(24299, "self", lambda: self).prev = _n_(24300, "prev", lambda: prev)
        _l_(24301)

class doubly_linked_list(_n_(24304, "object", lambda: object)):
    _l_(24374)


    def __init__(self):
        _l_(24311)

        _n_(24305, "self", lambda: self).head = None
        _l_(24306)
        _n_(24307, "self", lambda: self).tail = None
        _l_(24308)
        _n_(24309, "self", lambda: self).count = 0
        _l_(24310)

    def append_item(self, data):
        _l_(24339)

        new_item = _c_(24314, _n_(24312, "Node", lambda: Node), _n_(24313, "data", lambda: data), None, None)
        _l_(24315)
        if _a_(24317, _n_(24316, "self", lambda: self), "head") is None:
            _l_(24336)

            _n_(24318, "self", lambda: self).head = _n_(24319, "new_item", lambda: new_item)
            _l_(24320)
            _n_(24321, "self", lambda: self).tail = _a_(24323, _n_(24322, "self", lambda: self), "head")
            _l_(24324)
        else:
            _n_(24325, "new_item", lambda: new_item).prev = _a_(24327, _n_(24326, "self", lambda: self), "tail")
            _l_(24328)
            _a_(24330, _n_(24329, "self", lambda: self), "tail").next = _n_(24331, "new_item", lambda: new_item)
            _l_(24332)
            _n_(24333, "self", lambda: self).tail = _n_(24334, "new_item", lambda: new_item)
            _l_(24335)
        _n_(24337, "self", lambda: self).count += 1
        _l_(24338)

    def print_foward(self):
        _l_(24348)

        for node in _c_(24342, _a_(24341, _n_(24340, "self", lambda: self), "iter")):
            _l_(24347)

            _c_(24345, _n_(24343, "print", lambda: print), _n_(24344, "node", lambda: node))
            _l_(24346)

    def print_backward(self):
        _l_(24359)

        current = _a_(24350, _n_(24349, "self", lambda: self), "tail")
        _l_(24351)
        while _n_(24352, "current", lambda: current):
            _l_(24358)

            _c_(24356, _n_(24353, "print", lambda: print), _a_(24355, _n_(24354, "current", lambda: current), "data"))
            _l_(24357)

    def iter(self):
        _l_(24373)

        current = _a_(24361, _n_(24360, "self", lambda: self), "head")
        _l_(24362)
        while _n_(24363, "current", lambda: current):
            _l_(24372)

            item_val = _a_(24365, _n_(24364, "current", lambda: current), "data")
            _l_(24366)
            current = _a_(24368, _n_(24367, "current", lambda: current), "next")
            _l_(24369)
            yield _n_(24370, "item_val", lambda: item_val)
            _l_(24371)
items = _c_(24376, _n_(24375, "doubly_linked_list", lambda: doubly_linked_list))
_l_(24377)
_c_(24380, _a_(24379, _n_(24378, "items", lambda: items), "append_item"), 'PHP')
_l_(24381)
_c_(24384, _a_(24383, _n_(24382, "items", lambda: items), "append_item"), 'Python')
_l_(24385)
_c_(24388, _a_(24387, _n_(24386, "items", lambda: items), "append_item"), 'C#')
_l_(24389)
_c_(24392, _a_(24391, _n_(24390, "items", lambda: items), "append_item"), 'C++')
_l_(24393)
_c_(24396, _a_(24395, _n_(24394, "items", lambda: items), "append_item"), 'Java')
_l_(24397)
_c_(24399, _n_(24398, "print", lambda: print), 'Print Items in the Doubly linked backwards:')
_l_(24400)
_c_(24403, _a_(24402, _n_(24401, "items", lambda: items), "print_backward"))
_l_(24404)