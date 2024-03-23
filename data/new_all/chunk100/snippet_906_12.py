# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node:
    _l_(89372)


    def __init__(self, data=None):
        _l_(89371)

        _n_(89366, "self", lambda: self).data = _n_(89367, "data", lambda: data)
        _l_(89368)
        _n_(89369, "self", lambda: self).next = None
        _l_(89370)

class singly_linked_list:
    _l_(89448)


    def __init__(self):
        _l_(89377)

        _n_(89373, "self", lambda: self).head = None
        _l_(89374)
        _n_(89375, "self", lambda: self).count = 0
        _l_(89376)

    def append_item(self, data):
        _l_(89400)

        node = _c_(89380, _n_(89378, "Node", lambda: Node), _n_(89379, "data", lambda: data))
        _l_(89381)
        if _a_(89383, _n_(89382, "self", lambda: self), "head"):
            _l_(89397)

            _a_(89385, _n_(89384, "self", lambda: self), "head").next = _n_(89386, "node", lambda: node)
            _l_(89387)
            _n_(89388, "self", lambda: self).head = _n_(89389, "node", lambda: node)
            _l_(89390)
        else:
            _n_(89391, "self", lambda: self).tail = _n_(89392, "node", lambda: node)
            _l_(89393)
            _n_(89394, "self", lambda: self).head = _n_(89395, "node", lambda: node)
            _l_(89396)
        _n_(89398, "self", lambda: self).count += 1
        _l_(89399)

    def delete_item(self, data):
        _l_(89433)

        current = _a_(89402, _n_(89401, "self", lambda: self), "tail")
        _l_(89403)
        prev = _a_(89405, _n_(89404, "self", lambda: self), "tail")
        _l_(89406)
        while _n_(89407, "current", lambda: current):
            _l_(89432)

            if _a_(89409, _n_(89408, "current", lambda: current), "data") == _n_(89410, "data", lambda: data):
                _l_(89426)

                if _n_(89411, "current", lambda: current) == _a_(89413, _n_(89412, "self", lambda: self), "tail"):
                    _l_(89422)

                    _n_(89414, "self", lambda: self).tail = _a_(89416, _n_(89415, "current", lambda: current), "next")
                    _l_(89417)
                else:
                    _n_(89418, "prev", lambda: prev).next = _a_(89420, _n_(89419, "current", lambda: current), "next")
                    _l_(89421)
                _n_(89423, "self", lambda: self).count -= 1
                _l_(89424)
                aux = ""
                _l_(89425)
                return aux
            prev = _n_(89427, "current", lambda: current)
            _l_(89428)
            current = _a_(89430, _n_(89429, "current", lambda: current), "next")
            _l_(89431)

    def iterate_item(self):
        _l_(89447)

        current_item = _a_(89435, _n_(89434, "self", lambda: self), "tail")
        _l_(89436)
        while _n_(89437, "current_item", lambda: current_item):
            _l_(89446)

            val = _a_(89439, _n_(89438, "current_item", lambda: current_item), "data")
            _l_(89440)
            current_item = _a_(89442, _n_(89441, "current_item", lambda: current_item), "next")
            _l_(89443)
            yield _n_(89444, "val", lambda: val)
            _l_(89445)
items = _c_(89450, _n_(89449, "singly_linked_list", lambda: singly_linked_list))
_l_(89451)
_c_(89454, _a_(89453, _n_(89452, "items", lambda: items), "append_item"), 'PHP')
_l_(89455)
_c_(89458, _a_(89457, _n_(89456, "items", lambda: items), "append_item"), 'Python')
_l_(89459)
_c_(89462, _a_(89461, _n_(89460, "items", lambda: items), "append_item"), 'C#')
_l_(89463)
_c_(89466, _a_(89465, _n_(89464, "items", lambda: items), "append_item"), 'C++')
_l_(89467)
_c_(89470, _a_(89469, _n_(89468, "items", lambda: items), "append_item"), 'Java')
_l_(89471)
_c_(89473, _n_(89472, "print", lambda: print), 'Original list:')
_l_(89474)
for val in _c_(89477, _a_(89476, _n_(89475, "items", lambda: items), "iterate_item")):
    _l_(89482)

    _c_(89480, _n_(89478, "print", lambda: print), _n_(89479, "val", lambda: val))
    _l_(89481)
_c_(89484, _n_(89483, "print", lambda: print), '\nAfter removing the last item from the list:')
_l_(89485)
_c_(89488, _a_(89487, _n_(89486, "items", lambda: items), "delete_item"), 'Java')
_l_(89489)
for val in _c_(89492, _a_(89491, _n_(89490, "items", lambda: items), "iterate_item")):
    _l_(89497)

    _c_(89495, _n_(89493, "print", lambda: print), _n_(89494, "val", lambda: val))
    _l_(89496)