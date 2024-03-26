# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node(_n_(108510, "object", lambda: object)):
    _l_(108521)


    def __init__(self, data=None, next=None, prev=None):
        _l_(108520)

        _n_(108511, "self", lambda: self).data = _n_(108512, "data", lambda: data)
        _l_(108513)
        _n_(108514, "self", lambda: self).next = _n_(108515, "next", lambda: next)
        _l_(108516)
        _n_(108517, "self", lambda: self).prev = _n_(108518, "prev", lambda: prev)
        _l_(108519)

class doubly_linked_list(_n_(108522, "object", lambda: object)):
    _l_(108595)


    def __init__(self):
        _l_(108529)

        _n_(108523, "self", lambda: self).head = None
        _l_(108524)
        _n_(108525, "self", lambda: self).tail = None
        _l_(108526)
        _n_(108527, "self", lambda: self).count = 0
        _l_(108528)

    def append_item(self, data):
        _l_(108557)

        new_item = _c_(108532, _n_(108530, "Node", lambda: Node), _n_(108531, "data", lambda: data), None, None)
        _l_(108533)
        if _a_(108535, _n_(108534, "self", lambda: self), "head") is None:
            _l_(108554)

            _n_(108536, "self", lambda: self).head = _n_(108537, "new_item", lambda: new_item)
            _l_(108538)
            _n_(108539, "self", lambda: self).tail = _a_(108541, _n_(108540, "self", lambda: self), "head")
            _l_(108542)
        else:
            _n_(108543, "new_item", lambda: new_item).prev = _a_(108545, _n_(108544, "self", lambda: self), "tail")
            _l_(108546)
            _a_(108548, _n_(108547, "self", lambda: self), "tail").next = _n_(108549, "new_item", lambda: new_item)
            _l_(108550)
            _n_(108551, "self", lambda: self).tail = _n_(108552, "new_item", lambda: new_item)
            _l_(108553)
        _n_(108555, "self", lambda: self).count += 1
        _l_(108556)

    def print_foward(self):
        _l_(108566)

        for node in _c_(108560, _a_(108559, _n_(108558, "self", lambda: self), "iter")):
            _l_(108565)

            _c_(108563, _n_(108561, "print", lambda: print), _n_(108562, "node", lambda: node))
            _l_(108564)

    def print_backward(self):
        _l_(108580)

        current = _a_(108568, _n_(108567, "self", lambda: self), "tail")
        _l_(108569)
        while _n_(108570, "current", lambda: current):
            _l_(108579)

            _c_(108574, _n_(108571, "print", lambda: print), _a_(108573, _n_(108572, "current", lambda: current), "data"))
            _l_(108575)
            current = _a_(108577, _n_(108576, "current", lambda: current), "prev")
            _l_(108578)

    def iter(self):
        _l_(108594)

        current = _a_(108582, _n_(108581, "self", lambda: self), "head")
        _l_(108583)
        while _n_(108584, "current", lambda: current):
            _l_(108593)

            item_val = _a_(108586, _n_(108585, "current", lambda: current), "data")
            _l_(108587)
            current = _a_(108589, _n_(108588, "current", lambda: current), "next")
            _l_(108590)
            yield _n_(108591, "item_val", lambda: item_val)
            _l_(108592)
_c_(108598, _a_(108597, _n_(108596, "items", lambda: items), "append_item"), 'PHP')
_l_(108599)
_c_(108602, _a_(108601, _n_(108600, "items", lambda: items), "append_item"), 'Python')
_l_(108603)
_c_(108606, _a_(108605, _n_(108604, "items", lambda: items), "append_item"), 'C#')
_l_(108607)
_c_(108610, _a_(108609, _n_(108608, "items", lambda: items), "append_item"), 'C++')
_l_(108611)
_c_(108614, _a_(108613, _n_(108612, "items", lambda: items), "append_item"), 'Java')
_l_(108615)
_c_(108617, _n_(108616, "print", lambda: print), 'Print Items in the Doubly linked backwards:')
_l_(108618)
_c_(108621, _a_(108620, _n_(108619, "items", lambda: items), "print_backward"))
_l_(108622)