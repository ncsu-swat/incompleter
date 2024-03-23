# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node:
    _l_(90682)


    def __init__(self, data=None):
        _l_(90681)

        _n_(90678, "self", lambda: self).data = _n_(90679, "data", lambda: data)
        _l_(90680)

class singly_linked_list:
    _l_(90760)


    def __init__(self):
        _l_(90689)

        _n_(90683, "self", lambda: self).tail = None
        _l_(90684)
        _n_(90685, "self", lambda: self).head = None
        _l_(90686)
        _n_(90687, "self", lambda: self).count = 0
        _l_(90688)

    def append_item(self, data):
        _l_(90712)

        node = _c_(90692, _n_(90690, "Node", lambda: Node), _n_(90691, "data", lambda: data))
        _l_(90693)
        if _a_(90695, _n_(90694, "self", lambda: self), "head"):
            _l_(90709)

            _a_(90697, _n_(90696, "self", lambda: self), "head").next = _n_(90698, "node", lambda: node)
            _l_(90699)
            _n_(90700, "self", lambda: self).head = _n_(90701, "node", lambda: node)
            _l_(90702)
        else:
            _n_(90703, "self", lambda: self).tail = _n_(90704, "node", lambda: node)
            _l_(90705)
            _n_(90706, "self", lambda: self).head = _n_(90707, "node", lambda: node)
            _l_(90708)
        _n_(90710, "self", lambda: self).count += 1
        _l_(90711)

    def delete_item(self, data):
        _l_(90745)

        current = _a_(90714, _n_(90713, "self", lambda: self), "tail")
        _l_(90715)
        prev = _a_(90717, _n_(90716, "self", lambda: self), "tail")
        _l_(90718)
        while _n_(90719, "current", lambda: current):
            _l_(90744)

            if _a_(90721, _n_(90720, "current", lambda: current), "data") == _n_(90722, "data", lambda: data):
                _l_(90738)

                if _n_(90723, "current", lambda: current) == _a_(90725, _n_(90724, "self", lambda: self), "tail"):
                    _l_(90734)

                    _n_(90726, "self", lambda: self).tail = _a_(90728, _n_(90727, "current", lambda: current), "next")
                    _l_(90729)
                else:
                    _n_(90730, "prev", lambda: prev).next = _a_(90732, _n_(90731, "current", lambda: current), "next")
                    _l_(90733)
                _n_(90735, "self", lambda: self).count -= 1
                _l_(90736)
                aux = ""
                _l_(90737)
                return aux
            prev = _n_(90739, "current", lambda: current)
            _l_(90740)
            current = _a_(90742, _n_(90741, "current", lambda: current), "next")
            _l_(90743)

    def iterate_item(self):
        _l_(90759)

        current_item = _a_(90747, _n_(90746, "self", lambda: self), "tail")
        _l_(90748)
        while _n_(90749, "current_item", lambda: current_item):
            _l_(90758)

            val = _a_(90751, _n_(90750, "current_item", lambda: current_item), "data")
            _l_(90752)
            current_item = _a_(90754, _n_(90753, "current_item", lambda: current_item), "next")
            _l_(90755)
            yield _n_(90756, "val", lambda: val)
            _l_(90757)
items = _c_(90762, _n_(90761, "singly_linked_list", lambda: singly_linked_list))
_l_(90763)
_c_(90766, _a_(90765, _n_(90764, "items", lambda: items), "append_item"), 'PHP')
_l_(90767)
_c_(90770, _a_(90769, _n_(90768, "items", lambda: items), "append_item"), 'Python')
_l_(90771)
_c_(90774, _a_(90773, _n_(90772, "items", lambda: items), "append_item"), 'C#')
_l_(90775)
_c_(90778, _a_(90777, _n_(90776, "items", lambda: items), "append_item"), 'C++')
_l_(90779)
_c_(90782, _a_(90781, _n_(90780, "items", lambda: items), "append_item"), 'Java')
_l_(90783)
_c_(90785, _n_(90784, "print", lambda: print), 'Original list:')
_l_(90786)
for val in _c_(90789, _a_(90788, _n_(90787, "items", lambda: items), "iterate_item")):
    _l_(90794)

    _c_(90792, _n_(90790, "print", lambda: print), _n_(90791, "val", lambda: val))
    _l_(90793)
_c_(90796, _n_(90795, "print", lambda: print), '\nAfter removing the last item from the list:')
_l_(90797)
_c_(90800, _a_(90799, _n_(90798, "items", lambda: items), "delete_item"), 'Java')
_l_(90801)
for val in _c_(90804, _a_(90803, _n_(90802, "items", lambda: items), "iterate_item")):
    _l_(90809)

    _c_(90807, _n_(90805, "print", lambda: print), _n_(90806, "val", lambda: val))
    _l_(90808)