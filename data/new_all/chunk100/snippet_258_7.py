# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node(_n_(20821, "object", lambda: object)):
    _l_(20832)


    def __init__(self, data=None, next=None, prev=None):
        _l_(20831)

        _n_(20822, "self", lambda: self).data = _n_(20823, "data", lambda: data)
        _l_(20824)
        _n_(20825, "self", lambda: self).next = _n_(20826, "next", lambda: next)
        _l_(20827)
        _n_(20828, "self", lambda: self).prev = _n_(20829, "prev", lambda: prev)
        _l_(20830)

class doubly_linked_list(_n_(20833, "object", lambda: object)):
    _l_(20869)


    def __init__(self):
        _l_(20840)

        _n_(20834, "self", lambda: self).head = None
        _l_(20835)
        _n_(20836, "self", lambda: self).tail = None
        _l_(20837)
        _n_(20838, "self", lambda: self).count = 0
        _l_(20839)

    def append_item(self, data):
        _l_(20868)

        new_item = _c_(20843, _n_(20841, "Node", lambda: Node), _n_(20842, "data", lambda: data), None, None)
        _l_(20844)
        if _a_(20846, _n_(20845, "self", lambda: self), "head") is None:
            _l_(20865)

            _n_(20847, "self", lambda: self).head = _n_(20848, "new_item", lambda: new_item)
            _l_(20849)
            _n_(20850, "self", lambda: self).tail = _a_(20852, _n_(20851, "self", lambda: self), "head")
            _l_(20853)
        else:
            _n_(20854, "new_item", lambda: new_item).prev = _a_(20856, _n_(20855, "self", lambda: self), "tail")
            _l_(20857)
            _a_(20859, _n_(20858, "self", lambda: self), "tail").next = _n_(20860, "new_item", lambda: new_item)
            _l_(20861)
            _n_(20862, "self", lambda: self).tail = _n_(20863, "new_item", lambda: new_item)
            _l_(20864)
        _n_(20866, "self", lambda: self).count += 1
        _l_(20867)
_c_(20872, _a_(20871, _n_(20870, "items", lambda: items), "append_item"), 'PHP')
_l_(20873)
_c_(20876, _a_(20875, _n_(20874, "items", lambda: items), "append_item"), 'Python')
_l_(20877)
_c_(20880, _a_(20879, _n_(20878, "items", lambda: items), "append_item"), 'C#')
_l_(20881)
_c_(20884, _a_(20883, _n_(20882, "items", lambda: items), "append_item"), 'C++')
_l_(20885)
_c_(20888, _a_(20887, _n_(20886, "items", lambda: items), "append_item"), 'Java')
_l_(20889)
_c_(20892, _a_(20891, _n_(20890, "items", lambda: items), "append_item"), 'SQL')
_l_(20893)
_c_(20897, _n_(20894, "print", lambda: print), 'Number of items of the  Doubly linked list:', _a_(20896, _n_(20895, "items", lambda: items), "count"))
_l_(20898)