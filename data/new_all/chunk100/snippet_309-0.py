# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node(_n_(109660, "object", lambda: object)):
    _l_(109671)


    def __init__(self, value=None, next=None, prev=None):
        _l_(109670)

        _n_(109661, "self", lambda: self).value = _n_(109662, "value", lambda: value)
        _l_(109663)
        _n_(109664, "self", lambda: self).next = _n_(109665, "next", lambda: next)
        _l_(109666)
        _n_(109667, "self", lambda: self).prev = _n_(109668, "prev", lambda: prev)
        _l_(109669)

class doubly_linked_list(_n_(109672, "object", lambda: object)):
    _l_(109799)


    def __init__(self):
        _l_(109679)

        _n_(109673, "self", lambda: self).head = None
        _l_(109674)
        _n_(109675, "self", lambda: self).tail = None
        _l_(109676)
        _n_(109677, "self", lambda: self).count = 0
        _l_(109678)

    def append_item(self, value):
        _l_(109707)

        new_item = _c_(109682, _n_(109680, "Node", lambda: Node), _n_(109681, "value", lambda: value), None, None)
        _l_(109683)
        if _a_(109685, _n_(109684, "self", lambda: self), "head") is None:
            _l_(109704)

            _n_(109686, "self", lambda: self).head = _n_(109687, "new_item", lambda: new_item)
            _l_(109688)
            _n_(109689, "self", lambda: self).tail = _a_(109691, _n_(109690, "self", lambda: self), "head")
            _l_(109692)
        else:
            _n_(109693, "new_item", lambda: new_item).prev = _a_(109695, _n_(109694, "self", lambda: self), "tail")
            _l_(109696)
            _a_(109698, _n_(109697, "self", lambda: self), "tail").next = _n_(109699, "new_item", lambda: new_item)
            _l_(109700)
            _n_(109701, "self", lambda: self).tail = _n_(109702, "new_item", lambda: new_item)
            _l_(109703)
        _n_(109705, "self", lambda: self).count += 1
        _l_(109706)

    def iter(self):
        _l_(109721)

        current = _a_(109709, _n_(109708, "self", lambda: self), "head")
        _l_(109710)
        while _n_(109711, "current", lambda: current):
            _l_(109720)

            item_val = _a_(109713, _n_(109712, "current", lambda: current), "value")
            _l_(109714)
            current = _a_(109716, _n_(109715, "current", lambda: current), "next")
            _l_(109717)
            yield _n_(109718, "item_val", lambda: item_val)
            _l_(109719)

    def print_foward(self):
        _l_(109730)

        for node in _c_(109724, _a_(109723, _n_(109722, "self", lambda: self), "iter")):
            _l_(109729)

            _c_(109727, _n_(109725, "print", lambda: print), _n_(109726, "node", lambda: node))
            _l_(109728)

    def search_item(self, val):
        _l_(109740)

        for node in _c_(109733, _a_(109732, _n_(109731, "self", lambda: self), "iter")):
            _l_(109738)

            if _n_(109734, "val", lambda: val) == _n_(109735, "node", lambda: node):
                _l_(109737)

                aux = True
                _l_(109736)
                return aux
        aux = False
        _l_(109739)
        return aux

    def delete(self, value):
        _l_(109798)

        current = _a_(109742, _n_(109741, "self", lambda: self), "head")
        _l_(109743)
        node_deleted = False
        _l_(109744)
        if _n_(109745, "current", lambda: current) is None:
            _l_(109793)

            node_deleted = False
            _l_(109746)
        elif _a_(109748, _n_(109747, "current", lambda: current), "value") == _n_(109749, "value", lambda: value):
            _l_(109792)

            _n_(109750, "self", lambda: self).head = _a_(109752, _n_(109751, "current", lambda: current), "next")
            _l_(109753)
            _a_(109755, _n_(109754, "self", lambda: self), "head").prev = None
            _l_(109756)
            node_deleted = True
            _l_(109757)
        elif _a_(109760, _a_(109759, _n_(109758, "self", lambda: self), "tail"), "value") == _n_(109761, "value", lambda: value):
            _l_(109791)

            _n_(109762, "self", lambda: self).tail = _a_(109765, _a_(109764, _n_(109763, "self", lambda: self), "tail"), "prev")
            _l_(109766)
            _a_(109768, _n_(109767, "self", lambda: self), "tail").next = None
            _l_(109769)
            node_deleted = True
            _l_(109770)
        else:
            while _n_(109771, "current", lambda: current):
                _l_(109790)

                if _a_(109773, _n_(109772, "current", lambda: current), "value") == _n_(109774, "value", lambda: value):
                    _l_(109786)

                    _a_(109776, _n_(109775, "current", lambda: current), "prev").next = _a_(109778, _n_(109777, "current", lambda: current), "next")
                    _l_(109779)
                    _a_(109781, _n_(109780, "current", lambda: current), "next").prev = _a_(109783, _n_(109782, "current", lambda: current), "prev")
                    _l_(109784)
                    node_deleted = True
                    _l_(109785)
                current = _a_(109788, _n_(109787, "current", lambda: current), "next")
                _l_(109789)
        if _n_(109794, "node_deleted", lambda: node_deleted):
            _l_(109797)

            _n_(109795, "self", lambda: self).count -= 1
            _l_(109796)
_c_(109802, _a_(109801, _n_(109800, "items", lambda: items), "append_item"), 'PHP')
_l_(109803)
_c_(109806, _a_(109805, _n_(109804, "items", lambda: items), "append_item"), 'Python')
_l_(109807)
_c_(109810, _a_(109809, _n_(109808, "items", lambda: items), "append_item"), 'C#')
_l_(109811)
_c_(109814, _a_(109813, _n_(109812, "items", lambda: items), "append_item"), 'C++')
_l_(109815)
_c_(109818, _a_(109817, _n_(109816, "items", lambda: items), "append_item"), 'Java')
_l_(109819)
_c_(109822, _a_(109821, _n_(109820, "items", lambda: items), "append_item"), 'SQL')
_l_(109823)
_c_(109825, _n_(109824, "print", lambda: print), 'Original list:')
_l_(109826)
_c_(109829, _a_(109828, _n_(109827, "items", lambda: items), "print_foward"))
_l_(109830)
_c_(109833, _a_(109832, _n_(109831, "items", lambda: items), "delete"), 'Java')
_l_(109834)
_c_(109837, _a_(109836, _n_(109835, "items", lambda: items), "delete"), 'Python')
_l_(109838)
_c_(109840, _n_(109839, "print", lambda: print), '\nList after deleting two items:')
_l_(109841)
_c_(109844, _a_(109843, _n_(109842, "items", lambda: items), "print_foward"))
_l_(109845)