# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node(_n_(28678, "object", lambda: object)):
    _l_(28689)


    def __init__(self, value=None, next=None, prev=None):
        _l_(28688)

        _n_(28679, "self", lambda: self).value = _n_(28680, "value", lambda: value)
        _l_(28681)
        _n_(28682, "self", lambda: self).next = _n_(28683, "next", lambda: next)
        _l_(28684)
        _n_(28685, "self", lambda: self).prev = _n_(28686, "prev", lambda: prev)
        _l_(28687)

class doubly_linked_list(_n_(28690, "object", lambda: object)):
    _l_(28814)


    def __init__(self):
        _l_(28697)

        _n_(28691, "self", lambda: self).head = None
        _l_(28692)
        _n_(28693, "self", lambda: self).tail = None
        _l_(28694)
        _n_(28695, "self", lambda: self).count = 0
        _l_(28696)

    def append_item(self, value):
        _l_(28725)

        new_item = _c_(28700, _n_(28698, "Node", lambda: Node), _n_(28699, "value", lambda: value), None, None)
        _l_(28701)
        if _a_(28703, _n_(28702, "self", lambda: self), "head") is None:
            _l_(28722)

            _n_(28704, "self", lambda: self).head = _n_(28705, "new_item", lambda: new_item)
            _l_(28706)
            _n_(28707, "self", lambda: self).tail = _a_(28709, _n_(28708, "self", lambda: self), "head")
            _l_(28710)
        else:
            _n_(28711, "new_item", lambda: new_item).prev = _a_(28713, _n_(28712, "self", lambda: self), "tail")
            _l_(28714)
            _a_(28716, _n_(28715, "self", lambda: self), "tail").next = _n_(28717, "new_item", lambda: new_item)
            _l_(28718)
            _n_(28719, "self", lambda: self).tail = _n_(28720, "new_item", lambda: new_item)
            _l_(28721)
        _n_(28723, "self", lambda: self).count += 1
        _l_(28724)

    def iter(self):
        _l_(28736)

        current = _a_(28727, _n_(28726, "self", lambda: self), "head")
        _l_(28728)
        while _n_(28729, "current", lambda: current):
            _l_(28735)

            current = _a_(28731, _n_(28730, "current", lambda: current), "next")
            _l_(28732)
            yield _n_(28733, "item_val", lambda: item_val)
            _l_(28734)

    def print_foward(self):
        _l_(28745)

        for node in _c_(28739, _a_(28738, _n_(28737, "self", lambda: self), "iter")):
            _l_(28744)

            _c_(28742, _n_(28740, "print", lambda: print), _n_(28741, "node", lambda: node))
            _l_(28743)

    def search_item(self, val):
        _l_(28755)

        for node in _c_(28748, _a_(28747, _n_(28746, "self", lambda: self), "iter")):
            _l_(28753)

            if _n_(28749, "val", lambda: val) == _n_(28750, "node", lambda: node):
                _l_(28752)

                aux = True
                _l_(28751)
                return aux
        aux = False
        _l_(28754)
        return aux

    def delete(self, value):
        _l_(28813)

        current = _a_(28757, _n_(28756, "self", lambda: self), "head")
        _l_(28758)
        node_deleted = False
        _l_(28759)
        if _n_(28760, "current", lambda: current) is None:
            _l_(28808)

            node_deleted = False
            _l_(28761)
        elif _a_(28763, _n_(28762, "current", lambda: current), "value") == _n_(28764, "value", lambda: value):
            _l_(28807)

            _n_(28765, "self", lambda: self).head = _a_(28767, _n_(28766, "current", lambda: current), "next")
            _l_(28768)
            _a_(28770, _n_(28769, "self", lambda: self), "head").prev = None
            _l_(28771)
            node_deleted = True
            _l_(28772)
        elif _a_(28775, _a_(28774, _n_(28773, "self", lambda: self), "tail"), "value") == _n_(28776, "value", lambda: value):
            _l_(28806)

            _n_(28777, "self", lambda: self).tail = _a_(28780, _a_(28779, _n_(28778, "self", lambda: self), "tail"), "prev")
            _l_(28781)
            _a_(28783, _n_(28782, "self", lambda: self), "tail").next = None
            _l_(28784)
            node_deleted = True
            _l_(28785)
        else:
            while _n_(28786, "current", lambda: current):
                _l_(28805)

                if _a_(28788, _n_(28787, "current", lambda: current), "value") == _n_(28789, "value", lambda: value):
                    _l_(28801)

                    _a_(28791, _n_(28790, "current", lambda: current), "prev").next = _a_(28793, _n_(28792, "current", lambda: current), "next")
                    _l_(28794)
                    _a_(28796, _n_(28795, "current", lambda: current), "next").prev = _a_(28798, _n_(28797, "current", lambda: current), "prev")
                    _l_(28799)
                    node_deleted = True
                    _l_(28800)
                current = _a_(28803, _n_(28802, "current", lambda: current), "next")
                _l_(28804)
        if _n_(28809, "node_deleted", lambda: node_deleted):
            _l_(28812)

            _n_(28810, "self", lambda: self).count -= 1
            _l_(28811)
items = _c_(28816, _n_(28815, "doubly_linked_list", lambda: doubly_linked_list))
_l_(28817)
_c_(28820, _a_(28819, _n_(28818, "items", lambda: items), "append_item"), 'PHP')
_l_(28821)
_c_(28824, _a_(28823, _n_(28822, "items", lambda: items), "append_item"), 'Python')
_l_(28825)
_c_(28828, _a_(28827, _n_(28826, "items", lambda: items), "append_item"), 'C#')
_l_(28829)
_c_(28832, _a_(28831, _n_(28830, "items", lambda: items), "append_item"), 'C++')
_l_(28833)
_c_(28836, _a_(28835, _n_(28834, "items", lambda: items), "append_item"), 'Java')
_l_(28837)
_c_(28840, _a_(28839, _n_(28838, "items", lambda: items), "append_item"), 'SQL')
_l_(28841)
_c_(28843, _n_(28842, "print", lambda: print), 'Original list:')
_l_(28844)
_c_(28847, _a_(28846, _n_(28845, "items", lambda: items), "print_foward"))
_l_(28848)
_c_(28851, _a_(28850, _n_(28849, "items", lambda: items), "delete"), 'Java')
_l_(28852)
_c_(28855, _a_(28854, _n_(28853, "items", lambda: items), "delete"), 'Python')
_l_(28856)
_c_(28858, _n_(28857, "print", lambda: print), '\nList after deleting two items:')
_l_(28859)
_c_(28862, _a_(28861, _n_(28860, "items", lambda: items), "print_foward"))
_l_(28863)