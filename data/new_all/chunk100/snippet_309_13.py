# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node(_n_(27377, "object", lambda: object)):
    _l_(27388)


    def __init__(self, value=None, next=None, prev=None):
        _l_(27387)

        _n_(27378, "self", lambda: self).value = _n_(27379, "value", lambda: value)
        _l_(27380)
        _n_(27381, "self", lambda: self).next = _n_(27382, "next", lambda: next)
        _l_(27383)
        _n_(27384, "self", lambda: self).prev = _n_(27385, "prev", lambda: prev)
        _l_(27386)

class doubly_linked_list(_n_(27389, "object", lambda: object)):
    _l_(27513)


    def __init__(self):
        _l_(27396)

        _n_(27390, "self", lambda: self).head = None
        _l_(27391)
        _n_(27392, "self", lambda: self).tail = None
        _l_(27393)
        _n_(27394, "self", lambda: self).count = 0
        _l_(27395)

    def append_item(self, value):
        _l_(27424)

        new_item = _c_(27399, _n_(27397, "Node", lambda: Node), _n_(27398, "value", lambda: value), None, None)
        _l_(27400)
        if _a_(27402, _n_(27401, "self", lambda: self), "head") is None:
            _l_(27421)

            _n_(27403, "self", lambda: self).head = _n_(27404, "new_item", lambda: new_item)
            _l_(27405)
            _n_(27406, "self", lambda: self).tail = _a_(27408, _n_(27407, "self", lambda: self), "head")
            _l_(27409)
        else:
            _n_(27410, "new_item", lambda: new_item).prev = _a_(27412, _n_(27411, "self", lambda: self), "tail")
            _l_(27413)
            _a_(27415, _n_(27414, "self", lambda: self), "tail").next = _n_(27416, "new_item", lambda: new_item)
            _l_(27417)
            _n_(27418, "self", lambda: self).tail = _n_(27419, "new_item", lambda: new_item)
            _l_(27420)
        _n_(27422, "self", lambda: self).count += 1
        _l_(27423)

    def iter(self):
        _l_(27435)

        while _n_(27425, "current", lambda: current):
            _l_(27434)

            item_val = _a_(27427, _n_(27426, "current", lambda: current), "value")
            _l_(27428)
            current = _a_(27430, _n_(27429, "current", lambda: current), "next")
            _l_(27431)
            yield _n_(27432, "item_val", lambda: item_val)
            _l_(27433)

    def print_foward(self):
        _l_(27444)

        for node in _c_(27438, _a_(27437, _n_(27436, "self", lambda: self), "iter")):
            _l_(27443)

            _c_(27441, _n_(27439, "print", lambda: print), _n_(27440, "node", lambda: node))
            _l_(27442)

    def search_item(self, val):
        _l_(27454)

        for node in _c_(27447, _a_(27446, _n_(27445, "self", lambda: self), "iter")):
            _l_(27452)

            if _n_(27448, "val", lambda: val) == _n_(27449, "node", lambda: node):
                _l_(27451)

                aux = True
                _l_(27450)
                return aux
        aux = False
        _l_(27453)
        return aux

    def delete(self, value):
        _l_(27512)

        current = _a_(27456, _n_(27455, "self", lambda: self), "head")
        _l_(27457)
        node_deleted = False
        _l_(27458)
        if _n_(27459, "current", lambda: current) is None:
            _l_(27507)

            node_deleted = False
            _l_(27460)
        elif _a_(27462, _n_(27461, "current", lambda: current), "value") == _n_(27463, "value", lambda: value):
            _l_(27506)

            _n_(27464, "self", lambda: self).head = _a_(27466, _n_(27465, "current", lambda: current), "next")
            _l_(27467)
            _a_(27469, _n_(27468, "self", lambda: self), "head").prev = None
            _l_(27470)
            node_deleted = True
            _l_(27471)
        elif _a_(27474, _a_(27473, _n_(27472, "self", lambda: self), "tail"), "value") == _n_(27475, "value", lambda: value):
            _l_(27505)

            _n_(27476, "self", lambda: self).tail = _a_(27479, _a_(27478, _n_(27477, "self", lambda: self), "tail"), "prev")
            _l_(27480)
            _a_(27482, _n_(27481, "self", lambda: self), "tail").next = None
            _l_(27483)
            node_deleted = True
            _l_(27484)
        else:
            while _n_(27485, "current", lambda: current):
                _l_(27504)

                if _a_(27487, _n_(27486, "current", lambda: current), "value") == _n_(27488, "value", lambda: value):
                    _l_(27500)

                    _a_(27490, _n_(27489, "current", lambda: current), "prev").next = _a_(27492, _n_(27491, "current", lambda: current), "next")
                    _l_(27493)
                    _a_(27495, _n_(27494, "current", lambda: current), "next").prev = _a_(27497, _n_(27496, "current", lambda: current), "prev")
                    _l_(27498)
                    node_deleted = True
                    _l_(27499)
                current = _a_(27502, _n_(27501, "current", lambda: current), "next")
                _l_(27503)
        if _n_(27508, "node_deleted", lambda: node_deleted):
            _l_(27511)

            _n_(27509, "self", lambda: self).count -= 1
            _l_(27510)
items = _c_(27515, _n_(27514, "doubly_linked_list", lambda: doubly_linked_list))
_l_(27516)
_c_(27519, _a_(27518, _n_(27517, "items", lambda: items), "append_item"), 'PHP')
_l_(27520)
_c_(27523, _a_(27522, _n_(27521, "items", lambda: items), "append_item"), 'Python')
_l_(27524)
_c_(27527, _a_(27526, _n_(27525, "items", lambda: items), "append_item"), 'C#')
_l_(27528)
_c_(27531, _a_(27530, _n_(27529, "items", lambda: items), "append_item"), 'C++')
_l_(27532)
_c_(27535, _a_(27534, _n_(27533, "items", lambda: items), "append_item"), 'Java')
_l_(27536)
_c_(27539, _a_(27538, _n_(27537, "items", lambda: items), "append_item"), 'SQL')
_l_(27540)
_c_(27542, _n_(27541, "print", lambda: print), 'Original list:')
_l_(27543)
_c_(27546, _a_(27545, _n_(27544, "items", lambda: items), "print_foward"))
_l_(27547)
_c_(27550, _a_(27549, _n_(27548, "items", lambda: items), "delete"), 'Java')
_l_(27551)
_c_(27554, _a_(27553, _n_(27552, "items", lambda: items), "delete"), 'Python')
_l_(27555)
_c_(27557, _n_(27556, "print", lambda: print), '\nList after deleting two items:')
_l_(27558)
_c_(27561, _a_(27560, _n_(27559, "items", lambda: items), "print_foward"))
_l_(27562)