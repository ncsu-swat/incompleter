# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node(_n_(26633, "object", lambda: object)):
    _l_(26641)


    def __init__(self, value=None, next=None, prev=None):
        _l_(26640)

        _n_(26634, "self", lambda: self).value = _n_(26635, "value", lambda: value)
        _l_(26636)
        _n_(26637, "self", lambda: self).next = _n_(26638, "next", lambda: next)
        _l_(26639)

class doubly_linked_list(_n_(26642, "object", lambda: object)):
    _l_(26769)


    def __init__(self):
        _l_(26649)

        _n_(26643, "self", lambda: self).head = None
        _l_(26644)
        _n_(26645, "self", lambda: self).tail = None
        _l_(26646)
        _n_(26647, "self", lambda: self).count = 0
        _l_(26648)

    def append_item(self, value):
        _l_(26677)

        new_item = _c_(26652, _n_(26650, "Node", lambda: Node), _n_(26651, "value", lambda: value), None, None)
        _l_(26653)
        if _a_(26655, _n_(26654, "self", lambda: self), "head") is None:
            _l_(26674)

            _n_(26656, "self", lambda: self).head = _n_(26657, "new_item", lambda: new_item)
            _l_(26658)
            _n_(26659, "self", lambda: self).tail = _a_(26661, _n_(26660, "self", lambda: self), "head")
            _l_(26662)
        else:
            _n_(26663, "new_item", lambda: new_item).prev = _a_(26665, _n_(26664, "self", lambda: self), "tail")
            _l_(26666)
            _a_(26668, _n_(26667, "self", lambda: self), "tail").next = _n_(26669, "new_item", lambda: new_item)
            _l_(26670)
            _n_(26671, "self", lambda: self).tail = _n_(26672, "new_item", lambda: new_item)
            _l_(26673)
        _n_(26675, "self", lambda: self).count += 1
        _l_(26676)

    def iter(self):
        _l_(26691)

        current = _a_(26679, _n_(26678, "self", lambda: self), "head")
        _l_(26680)
        while _n_(26681, "current", lambda: current):
            _l_(26690)

            item_val = _a_(26683, _n_(26682, "current", lambda: current), "value")
            _l_(26684)
            current = _a_(26686, _n_(26685, "current", lambda: current), "next")
            _l_(26687)
            yield _n_(26688, "item_val", lambda: item_val)
            _l_(26689)

    def print_foward(self):
        _l_(26700)

        for node in _c_(26694, _a_(26693, _n_(26692, "self", lambda: self), "iter")):
            _l_(26699)

            _c_(26697, _n_(26695, "print", lambda: print), _n_(26696, "node", lambda: node))
            _l_(26698)

    def search_item(self, val):
        _l_(26710)

        for node in _c_(26703, _a_(26702, _n_(26701, "self", lambda: self), "iter")):
            _l_(26708)

            if _n_(26704, "val", lambda: val) == _n_(26705, "node", lambda: node):
                _l_(26707)

                aux = True
                _l_(26706)
                return aux
        aux = False
        _l_(26709)
        return aux

    def delete(self, value):
        _l_(26768)

        current = _a_(26712, _n_(26711, "self", lambda: self), "head")
        _l_(26713)
        node_deleted = False
        _l_(26714)
        if _n_(26715, "current", lambda: current) is None:
            _l_(26763)

            node_deleted = False
            _l_(26716)
        elif _a_(26718, _n_(26717, "current", lambda: current), "value") == _n_(26719, "value", lambda: value):
            _l_(26762)

            _n_(26720, "self", lambda: self).head = _a_(26722, _n_(26721, "current", lambda: current), "next")
            _l_(26723)
            _a_(26725, _n_(26724, "self", lambda: self), "head").prev = None
            _l_(26726)
            node_deleted = True
            _l_(26727)
        elif _a_(26730, _a_(26729, _n_(26728, "self", lambda: self), "tail"), "value") == _n_(26731, "value", lambda: value):
            _l_(26761)

            _n_(26732, "self", lambda: self).tail = _a_(26735, _a_(26734, _n_(26733, "self", lambda: self), "tail"), "prev")
            _l_(26736)
            _a_(26738, _n_(26737, "self", lambda: self), "tail").next = None
            _l_(26739)
            node_deleted = True
            _l_(26740)
        else:
            while _n_(26741, "current", lambda: current):
                _l_(26760)

                if _a_(26743, _n_(26742, "current", lambda: current), "value") == _n_(26744, "value", lambda: value):
                    _l_(26756)

                    _a_(26746, _n_(26745, "current", lambda: current), "prev").next = _a_(26748, _n_(26747, "current", lambda: current), "next")
                    _l_(26749)
                    _a_(26751, _n_(26750, "current", lambda: current), "next").prev = _a_(26753, _n_(26752, "current", lambda: current), "prev")
                    _l_(26754)
                    node_deleted = True
                    _l_(26755)
                current = _a_(26758, _n_(26757, "current", lambda: current), "next")
                _l_(26759)
        if _n_(26764, "node_deleted", lambda: node_deleted):
            _l_(26767)

            _n_(26765, "self", lambda: self).count -= 1
            _l_(26766)
items = _c_(26771, _n_(26770, "doubly_linked_list", lambda: doubly_linked_list))
_l_(26772)
_c_(26775, _a_(26774, _n_(26773, "items", lambda: items), "append_item"), 'PHP')
_l_(26776)
_c_(26779, _a_(26778, _n_(26777, "items", lambda: items), "append_item"), 'Python')
_l_(26780)
_c_(26783, _a_(26782, _n_(26781, "items", lambda: items), "append_item"), 'C#')
_l_(26784)
_c_(26787, _a_(26786, _n_(26785, "items", lambda: items), "append_item"), 'C++')
_l_(26788)
_c_(26791, _a_(26790, _n_(26789, "items", lambda: items), "append_item"), 'Java')
_l_(26792)
_c_(26795, _a_(26794, _n_(26793, "items", lambda: items), "append_item"), 'SQL')
_l_(26796)
_c_(26798, _n_(26797, "print", lambda: print), 'Original list:')
_l_(26799)
_c_(26802, _a_(26801, _n_(26800, "items", lambda: items), "print_foward"))
_l_(26803)
_c_(26806, _a_(26805, _n_(26804, "items", lambda: items), "delete"), 'Java')
_l_(26807)
_c_(26810, _a_(26809, _n_(26808, "items", lambda: items), "delete"), 'Python')
_l_(26811)
_c_(26813, _n_(26812, "print", lambda: print), '\nList after deleting two items:')
_l_(26814)
_c_(26817, _a_(26816, _n_(26815, "items", lambda: items), "print_foward"))
_l_(26818)