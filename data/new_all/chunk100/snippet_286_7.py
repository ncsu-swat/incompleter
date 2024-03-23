# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node(_n_(24179, "object", lambda: object)):
    _l_(24187)


    def __init__(self, data=None, next=None, prev=None):
        _l_(24186)

        _n_(24180, "self", lambda: self).data = _n_(24181, "data", lambda: data)
        _l_(24182)
        _n_(24183, "self", lambda: self).prev = _n_(24184, "prev", lambda: prev)
        _l_(24185)

class doubly_linked_list(_n_(24188, "object", lambda: object)):
    _l_(24261)


    def __init__(self):
        _l_(24195)

        _n_(24189, "self", lambda: self).head = None
        _l_(24190)
        _n_(24191, "self", lambda: self).tail = None
        _l_(24192)
        _n_(24193, "self", lambda: self).count = 0
        _l_(24194)

    def append_item(self, data):
        _l_(24223)

        new_item = _c_(24198, _n_(24196, "Node", lambda: Node), _n_(24197, "data", lambda: data), None, None)
        _l_(24199)
        if _a_(24201, _n_(24200, "self", lambda: self), "head") is None:
            _l_(24220)

            _n_(24202, "self", lambda: self).head = _n_(24203, "new_item", lambda: new_item)
            _l_(24204)
            _n_(24205, "self", lambda: self).tail = _a_(24207, _n_(24206, "self", lambda: self), "head")
            _l_(24208)
        else:
            _n_(24209, "new_item", lambda: new_item).prev = _a_(24211, _n_(24210, "self", lambda: self), "tail")
            _l_(24212)
            _a_(24214, _n_(24213, "self", lambda: self), "tail").next = _n_(24215, "new_item", lambda: new_item)
            _l_(24216)
            _n_(24217, "self", lambda: self).tail = _n_(24218, "new_item", lambda: new_item)
            _l_(24219)
        _n_(24221, "self", lambda: self).count += 1
        _l_(24222)

    def print_foward(self):
        _l_(24232)

        for node in _c_(24226, _a_(24225, _n_(24224, "self", lambda: self), "iter")):
            _l_(24231)

            _c_(24229, _n_(24227, "print", lambda: print), _n_(24228, "node", lambda: node))
            _l_(24230)

    def print_backward(self):
        _l_(24246)

        current = _a_(24234, _n_(24233, "self", lambda: self), "tail")
        _l_(24235)
        while _n_(24236, "current", lambda: current):
            _l_(24245)

            _c_(24240, _n_(24237, "print", lambda: print), _a_(24239, _n_(24238, "current", lambda: current), "data"))
            _l_(24241)
            current = _a_(24243, _n_(24242, "current", lambda: current), "prev")
            _l_(24244)

    def iter(self):
        _l_(24260)

        current = _a_(24248, _n_(24247, "self", lambda: self), "head")
        _l_(24249)
        while _n_(24250, "current", lambda: current):
            _l_(24259)

            item_val = _a_(24252, _n_(24251, "current", lambda: current), "data")
            _l_(24253)
            current = _a_(24255, _n_(24254, "current", lambda: current), "next")
            _l_(24256)
            yield _n_(24257, "item_val", lambda: item_val)
            _l_(24258)
items = _c_(24263, _n_(24262, "doubly_linked_list", lambda: doubly_linked_list))
_l_(24264)
_c_(24267, _a_(24266, _n_(24265, "items", lambda: items), "append_item"), 'PHP')
_l_(24268)
_c_(24271, _a_(24270, _n_(24269, "items", lambda: items), "append_item"), 'Python')
_l_(24272)
_c_(24275, _a_(24274, _n_(24273, "items", lambda: items), "append_item"), 'C#')
_l_(24276)
_c_(24279, _a_(24278, _n_(24277, "items", lambda: items), "append_item"), 'C++')
_l_(24280)
_c_(24283, _a_(24282, _n_(24281, "items", lambda: items), "append_item"), 'Java')
_l_(24284)
_c_(24286, _n_(24285, "print", lambda: print), 'Print Items in the Doubly linked backwards:')
_l_(24287)
_c_(24290, _a_(24289, _n_(24288, "items", lambda: items), "print_backward"))
_l_(24291)