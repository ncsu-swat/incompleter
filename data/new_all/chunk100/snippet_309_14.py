# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node(_n_(27563, "object", lambda: object)):
    _l_(27574)


    def __init__(self, value=None, next=None, prev=None):
        _l_(27573)

        _n_(27564, "self", lambda: self).value = _n_(27565, "value", lambda: value)
        _l_(27566)
        _n_(27567, "self", lambda: self).next = _n_(27568, "next", lambda: next)
        _l_(27569)
        _n_(27570, "self", lambda: self).prev = _n_(27571, "prev", lambda: prev)
        _l_(27572)

class doubly_linked_list(_n_(27575, "object", lambda: object)):
    _l_(27699)


    def __init__(self):
        _l_(27582)

        _n_(27576, "self", lambda: self).head = None
        _l_(27577)
        _n_(27578, "self", lambda: self).tail = None
        _l_(27579)
        _n_(27580, "self", lambda: self).count = 0
        _l_(27581)

    def append_item(self, value):
        _l_(27607)

        new_item = _c_(27585, _n_(27583, "Node", lambda: Node), _n_(27584, "value", lambda: value), None, None)
        _l_(27586)
        if _a_(27588, _n_(27587, "self", lambda: self), "head") is None:
            _l_(27604)

            _n_(27589, "self", lambda: self).tail = _a_(27591, _n_(27590, "self", lambda: self), "head")
            _l_(27592)
        else:
            _n_(27593, "new_item", lambda: new_item).prev = _a_(27595, _n_(27594, "self", lambda: self), "tail")
            _l_(27596)
            _a_(27598, _n_(27597, "self", lambda: self), "tail").next = _n_(27599, "new_item", lambda: new_item)
            _l_(27600)
            _n_(27601, "self", lambda: self).tail = _n_(27602, "new_item", lambda: new_item)
            _l_(27603)
        _n_(27605, "self", lambda: self).count += 1
        _l_(27606)

    def iter(self):
        _l_(27621)

        current = _a_(27609, _n_(27608, "self", lambda: self), "head")
        _l_(27610)
        while _n_(27611, "current", lambda: current):
            _l_(27620)

            item_val = _a_(27613, _n_(27612, "current", lambda: current), "value")
            _l_(27614)
            current = _a_(27616, _n_(27615, "current", lambda: current), "next")
            _l_(27617)
            yield _n_(27618, "item_val", lambda: item_val)
            _l_(27619)

    def print_foward(self):
        _l_(27630)

        for node in _c_(27624, _a_(27623, _n_(27622, "self", lambda: self), "iter")):
            _l_(27629)

            _c_(27627, _n_(27625, "print", lambda: print), _n_(27626, "node", lambda: node))
            _l_(27628)

    def search_item(self, val):
        _l_(27640)

        for node in _c_(27633, _a_(27632, _n_(27631, "self", lambda: self), "iter")):
            _l_(27638)

            if _n_(27634, "val", lambda: val) == _n_(27635, "node", lambda: node):
                _l_(27637)

                aux = True
                _l_(27636)
                return aux
        aux = False
        _l_(27639)
        return aux

    def delete(self, value):
        _l_(27698)

        current = _a_(27642, _n_(27641, "self", lambda: self), "head")
        _l_(27643)
        node_deleted = False
        _l_(27644)
        if _n_(27645, "current", lambda: current) is None:
            _l_(27693)

            node_deleted = False
            _l_(27646)
        elif _a_(27648, _n_(27647, "current", lambda: current), "value") == _n_(27649, "value", lambda: value):
            _l_(27692)

            _n_(27650, "self", lambda: self).head = _a_(27652, _n_(27651, "current", lambda: current), "next")
            _l_(27653)
            _a_(27655, _n_(27654, "self", lambda: self), "head").prev = None
            _l_(27656)
            node_deleted = True
            _l_(27657)
        elif _a_(27660, _a_(27659, _n_(27658, "self", lambda: self), "tail"), "value") == _n_(27661, "value", lambda: value):
            _l_(27691)

            _n_(27662, "self", lambda: self).tail = _a_(27665, _a_(27664, _n_(27663, "self", lambda: self), "tail"), "prev")
            _l_(27666)
            _a_(27668, _n_(27667, "self", lambda: self), "tail").next = None
            _l_(27669)
            node_deleted = True
            _l_(27670)
        else:
            while _n_(27671, "current", lambda: current):
                _l_(27690)

                if _a_(27673, _n_(27672, "current", lambda: current), "value") == _n_(27674, "value", lambda: value):
                    _l_(27686)

                    _a_(27676, _n_(27675, "current", lambda: current), "prev").next = _a_(27678, _n_(27677, "current", lambda: current), "next")
                    _l_(27679)
                    _a_(27681, _n_(27680, "current", lambda: current), "next").prev = _a_(27683, _n_(27682, "current", lambda: current), "prev")
                    _l_(27684)
                    node_deleted = True
                    _l_(27685)
                current = _a_(27688, _n_(27687, "current", lambda: current), "next")
                _l_(27689)
        if _n_(27694, "node_deleted", lambda: node_deleted):
            _l_(27697)

            _n_(27695, "self", lambda: self).count -= 1
            _l_(27696)
items = _c_(27701, _n_(27700, "doubly_linked_list", lambda: doubly_linked_list))
_l_(27702)
_c_(27705, _a_(27704, _n_(27703, "items", lambda: items), "append_item"), 'PHP')
_l_(27706)
_c_(27709, _a_(27708, _n_(27707, "items", lambda: items), "append_item"), 'Python')
_l_(27710)
_c_(27713, _a_(27712, _n_(27711, "items", lambda: items), "append_item"), 'C#')
_l_(27714)
_c_(27717, _a_(27716, _n_(27715, "items", lambda: items), "append_item"), 'C++')
_l_(27718)
_c_(27721, _a_(27720, _n_(27719, "items", lambda: items), "append_item"), 'Java')
_l_(27722)
_c_(27725, _a_(27724, _n_(27723, "items", lambda: items), "append_item"), 'SQL')
_l_(27726)
_c_(27728, _n_(27727, "print", lambda: print), 'Original list:')
_l_(27729)
_c_(27732, _a_(27731, _n_(27730, "items", lambda: items), "print_foward"))
_l_(27733)
_c_(27736, _a_(27735, _n_(27734, "items", lambda: items), "delete"), 'Java')
_l_(27737)
_c_(27740, _a_(27739, _n_(27738, "items", lambda: items), "delete"), 'Python')
_l_(27741)
_c_(27743, _n_(27742, "print", lambda: print), '\nList after deleting two items:')
_l_(27744)
_c_(27747, _a_(27746, _n_(27745, "items", lambda: items), "print_foward"))
_l_(27748)