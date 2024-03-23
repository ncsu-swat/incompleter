# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node:
    _l_(89504)


    def __init__(self, data=None):
        _l_(89503)

        _n_(89498, "self", lambda: self).data = _n_(89499, "data", lambda: data)
        _l_(89500)
        _n_(89501, "self", lambda: self).next = None
        _l_(89502)

class singly_linked_list:
    _l_(89579)


    def __init__(self):
        _l_(89511)

        _n_(89505, "self", lambda: self).tail = None
        _l_(89506)
        _n_(89507, "self", lambda: self).head = None
        _l_(89508)
        _n_(89509, "self", lambda: self).count = 0
        _l_(89510)

    def append_item(self, data):
        _l_(89534)

        node = _c_(89514, _n_(89512, "Node", lambda: Node), _n_(89513, "data", lambda: data))
        _l_(89515)
        if _a_(89517, _n_(89516, "self", lambda: self), "head"):
            _l_(89531)

            _a_(89519, _n_(89518, "self", lambda: self), "head").next = _n_(89520, "node", lambda: node)
            _l_(89521)
            _n_(89522, "self", lambda: self).head = _n_(89523, "node", lambda: node)
            _l_(89524)
        else:
            _n_(89525, "self", lambda: self).tail = _n_(89526, "node", lambda: node)
            _l_(89527)
            _n_(89528, "self", lambda: self).head = _n_(89529, "node", lambda: node)
            _l_(89530)
        _n_(89532, "self", lambda: self).count += 1
        _l_(89533)

    def delete_item(self, data):
        _l_(89564)

        current = _a_(89536, _n_(89535, "self", lambda: self), "tail")
        _l_(89537)
        prev = _a_(89539, _n_(89538, "self", lambda: self), "tail")
        _l_(89540)
        while _n_(89541, "current", lambda: current):
            _l_(89563)

            if _a_(89543, _n_(89542, "current", lambda: current), "data") == _n_(89544, "data", lambda: data):
                _l_(89560)

                if _n_(89545, "current", lambda: current) == _a_(89547, _n_(89546, "self", lambda: self), "tail"):
                    _l_(89556)

                    _n_(89548, "self", lambda: self).tail = _a_(89550, _n_(89549, "current", lambda: current), "next")
                    _l_(89551)
                else:
                    _n_(89552, "prev", lambda: prev).next = _a_(89554, _n_(89553, "current", lambda: current), "next")
                    _l_(89555)
                _n_(89557, "self", lambda: self).count -= 1
                _l_(89558)
                aux = ""
                _l_(89559)
                return aux
            prev = _n_(89561, "current", lambda: current)
            _l_(89562)

    def iterate_item(self):
        _l_(89578)

        current_item = _a_(89566, _n_(89565, "self", lambda: self), "tail")
        _l_(89567)
        while _n_(89568, "current_item", lambda: current_item):
            _l_(89577)

            val = _a_(89570, _n_(89569, "current_item", lambda: current_item), "data")
            _l_(89571)
            current_item = _a_(89573, _n_(89572, "current_item", lambda: current_item), "next")
            _l_(89574)
            yield _n_(89575, "val", lambda: val)
            _l_(89576)
items = _c_(89581, _n_(89580, "singly_linked_list", lambda: singly_linked_list))
_l_(89582)
_c_(89585, _a_(89584, _n_(89583, "items", lambda: items), "append_item"), 'PHP')
_l_(89586)
_c_(89589, _a_(89588, _n_(89587, "items", lambda: items), "append_item"), 'Python')
_l_(89590)
_c_(89593, _a_(89592, _n_(89591, "items", lambda: items), "append_item"), 'C#')
_l_(89594)
_c_(89597, _a_(89596, _n_(89595, "items", lambda: items), "append_item"), 'C++')
_l_(89598)
_c_(89601, _a_(89600, _n_(89599, "items", lambda: items), "append_item"), 'Java')
_l_(89602)
_c_(89604, _n_(89603, "print", lambda: print), 'Original list:')
_l_(89605)
for val in _c_(89608, _a_(89607, _n_(89606, "items", lambda: items), "iterate_item")):
    _l_(89613)

    _c_(89611, _n_(89609, "print", lambda: print), _n_(89610, "val", lambda: val))
    _l_(89612)
_c_(89615, _n_(89614, "print", lambda: print), '\nAfter removing the last item from the list:')
_l_(89616)
_c_(89619, _a_(89618, _n_(89617, "items", lambda: items), "delete_item"), 'Java')
_l_(89620)
for val in _c_(89623, _a_(89622, _n_(89621, "items", lambda: items), "iterate_item")):
    _l_(89628)

    _c_(89626, _n_(89624, "print", lambda: print), _n_(89625, "val", lambda: val))
    _l_(89627)