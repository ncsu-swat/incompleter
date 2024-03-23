# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node:
    _l_(44708)


    def __init__(self, data=None):
        _l_(44707)

        _n_(44702, "self", lambda: self).data = _n_(44703, "data", lambda: data)
        _l_(44704)
        _n_(44705, "self", lambda: self).next = None
        _l_(44706)

class singly_linked_list:
    _l_(44776)


    def __init__(self):
        _l_(44715)

        _n_(44709, "self", lambda: self).tail = None
        _l_(44710)
        _n_(44711, "self", lambda: self).head = None
        _l_(44712)
        _n_(44713, "self", lambda: self).count = 0
        _l_(44714)

    def append_item(self, data):
        _l_(44738)

        node = _c_(44718, _n_(44716, "Node", lambda: Node), _n_(44717, "data", lambda: data))
        _l_(44719)
        if _a_(44721, _n_(44720, "self", lambda: self), "head"):
            _l_(44735)

            _a_(44723, _n_(44722, "self", lambda: self), "head").next = _n_(44724, "node", lambda: node)
            _l_(44725)
            _n_(44726, "self", lambda: self).head = _n_(44727, "node", lambda: node)
            _l_(44728)
        else:
            _n_(44729, "self", lambda: self).tail = _n_(44730, "node", lambda: node)
            _l_(44731)
            _n_(44732, "self", lambda: self).head = _n_(44733, "node", lambda: node)
            _l_(44734)
        _n_(44736, "self", lambda: self).count += 1
        _l_(44737)

    def __getitem__(self, index):
        _l_(44754)

        if _n_(44739, "index", lambda: index) > _a_(44741, _n_(44740, "self", lambda: self), "count") - 1:
            _l_(44743)

            aux = 'Index out of range'
            _l_(44742)
            return aux
        for n in _c_(44746, _n_(44744, "range", lambda: range), _n_(44745, "index", lambda: index)):
            _l_(44750)

            current_val = _a_(44748, _n_(44747, "current_val", lambda: current_val), "next")
            _l_(44749)
        aux = _a_(44752, _n_(44751, "current_val", lambda: current_val), "data")
        _l_(44753)
        return aux

    def __setitem__(self, index, value):
        _l_(44775)

        if _n_(44755, "index", lambda: index) > _a_(44757, _n_(44756, "self", lambda: self), "count") - 1:
            _l_(44761)

            raise _c_(44759, _n_(44758, "Exception", lambda: Exception), 'Index out of range.')
            _l_(44760)
        current = _a_(44763, _n_(44762, "self", lambda: self), "tail")
        _l_(44764)
        for n in _c_(44767, _n_(44765, "range", lambda: range), _n_(44766, "index", lambda: index)):
            _l_(44771)

            current = _a_(44769, _n_(44768, "current", lambda: current), "next")
            _l_(44770)
        _n_(44772, "current", lambda: current).data = _n_(44773, "value", lambda: value)
        _l_(44774)
items = _c_(44778, _n_(44777, "singly_linked_list", lambda: singly_linked_list))
_l_(44779)
_c_(44782, _a_(44781, _n_(44780, "items", lambda: items), "append_item"), 'PHP')
_l_(44783)
_c_(44786, _a_(44785, _n_(44784, "items", lambda: items), "append_item"), 'Python')
_l_(44787)
_c_(44790, _a_(44789, _n_(44788, "items", lambda: items), "append_item"), 'C#')
_l_(44791)
_c_(44794, _a_(44793, _n_(44792, "items", lambda: items), "append_item"), 'C++')
_l_(44795)
_c_(44798, _a_(44797, _n_(44796, "items", lambda: items), "append_item"), 'Java')
_l_(44799)
_c_(44801, _n_(44800, "print", lambda: print), 'Modify items by index:')
_l_(44802)
_n_(44803, "items", lambda: items)[1] = 'SQL'
_l_(44804)
_c_(44807, _n_(44805, "print", lambda: print), 'New value: ', _n_(44806, "items", lambda: items)[1])
_l_(44808)
_n_(44809, "items", lambda: items)[4] = 'Perl'
_l_(44810)
_c_(44813, _n_(44811, "print", lambda: print), 'New value: ', _n_(44812, "items", lambda: items)[4])
_l_(44814)