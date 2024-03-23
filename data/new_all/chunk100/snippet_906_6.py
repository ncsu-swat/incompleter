# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node:
    _l_(90552)


    def __init__(self, data=None):
        _l_(90551)

        _n_(90546, "self", lambda: self).data = _n_(90547, "data", lambda: data)
        _l_(90548)
        _n_(90549, "self", lambda: self).next = None
        _l_(90550)

class singly_linked_list:
    _l_(90628)


    def __init__(self):
        _l_(90557)

        _n_(90553, "self", lambda: self).tail = None
        _l_(90554)
        _n_(90555, "self", lambda: self).head = None
        _l_(90556)

    def append_item(self, data):
        _l_(90580)

        node = _c_(90560, _n_(90558, "Node", lambda: Node), _n_(90559, "data", lambda: data))
        _l_(90561)
        if _a_(90563, _n_(90562, "self", lambda: self), "head"):
            _l_(90577)

            _a_(90565, _n_(90564, "self", lambda: self), "head").next = _n_(90566, "node", lambda: node)
            _l_(90567)
            _n_(90568, "self", lambda: self).head = _n_(90569, "node", lambda: node)
            _l_(90570)
        else:
            _n_(90571, "self", lambda: self).tail = _n_(90572, "node", lambda: node)
            _l_(90573)
            _n_(90574, "self", lambda: self).head = _n_(90575, "node", lambda: node)
            _l_(90576)
        _n_(90578, "self", lambda: self).count += 1
        _l_(90579)

    def delete_item(self, data):
        _l_(90613)

        current = _a_(90582, _n_(90581, "self", lambda: self), "tail")
        _l_(90583)
        prev = _a_(90585, _n_(90584, "self", lambda: self), "tail")
        _l_(90586)
        while _n_(90587, "current", lambda: current):
            _l_(90612)

            if _a_(90589, _n_(90588, "current", lambda: current), "data") == _n_(90590, "data", lambda: data):
                _l_(90606)

                if _n_(90591, "current", lambda: current) == _a_(90593, _n_(90592, "self", lambda: self), "tail"):
                    _l_(90602)

                    _n_(90594, "self", lambda: self).tail = _a_(90596, _n_(90595, "current", lambda: current), "next")
                    _l_(90597)
                else:
                    _n_(90598, "prev", lambda: prev).next = _a_(90600, _n_(90599, "current", lambda: current), "next")
                    _l_(90601)
                _n_(90603, "self", lambda: self).count -= 1
                _l_(90604)
                aux = ""
                _l_(90605)
                return aux
            prev = _n_(90607, "current", lambda: current)
            _l_(90608)
            current = _a_(90610, _n_(90609, "current", lambda: current), "next")
            _l_(90611)

    def iterate_item(self):
        _l_(90627)

        current_item = _a_(90615, _n_(90614, "self", lambda: self), "tail")
        _l_(90616)
        while _n_(90617, "current_item", lambda: current_item):
            _l_(90626)

            val = _a_(90619, _n_(90618, "current_item", lambda: current_item), "data")
            _l_(90620)
            current_item = _a_(90622, _n_(90621, "current_item", lambda: current_item), "next")
            _l_(90623)
            yield _n_(90624, "val", lambda: val)
            _l_(90625)
items = _c_(90630, _n_(90629, "singly_linked_list", lambda: singly_linked_list))
_l_(90631)
_c_(90634, _a_(90633, _n_(90632, "items", lambda: items), "append_item"), 'PHP')
_l_(90635)
_c_(90638, _a_(90637, _n_(90636, "items", lambda: items), "append_item"), 'Python')
_l_(90639)
_c_(90642, _a_(90641, _n_(90640, "items", lambda: items), "append_item"), 'C#')
_l_(90643)
_c_(90646, _a_(90645, _n_(90644, "items", lambda: items), "append_item"), 'C++')
_l_(90647)
_c_(90650, _a_(90649, _n_(90648, "items", lambda: items), "append_item"), 'Java')
_l_(90651)
_c_(90653, _n_(90652, "print", lambda: print), 'Original list:')
_l_(90654)
for val in _c_(90657, _a_(90656, _n_(90655, "items", lambda: items), "iterate_item")):
    _l_(90662)

    _c_(90660, _n_(90658, "print", lambda: print), _n_(90659, "val", lambda: val))
    _l_(90661)
_c_(90664, _n_(90663, "print", lambda: print), '\nAfter removing the last item from the list:')
_l_(90665)
_c_(90668, _a_(90667, _n_(90666, "items", lambda: items), "delete_item"), 'Java')
_l_(90669)
for val in _c_(90672, _a_(90671, _n_(90670, "items", lambda: items), "iterate_item")):
    _l_(90677)

    _c_(90675, _n_(90673, "print", lambda: print), _n_(90674, "val", lambda: val))
    _l_(90676)