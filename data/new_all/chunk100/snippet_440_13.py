# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node:
    _l_(45044)


    def __init__(self, data=None):
        _l_(45043)

        _n_(45041, "self", lambda: self).next = None
        _l_(45042)

class singly_linked_list:
    _l_(45115)


    def __init__(self):
        _l_(45051)

        _n_(45045, "self", lambda: self).tail = None
        _l_(45046)
        _n_(45047, "self", lambda: self).head = None
        _l_(45048)
        _n_(45049, "self", lambda: self).count = 0
        _l_(45050)

    def append_item(self, data):
        _l_(45074)

        node = _c_(45054, _n_(45052, "Node", lambda: Node), _n_(45053, "data", lambda: data))
        _l_(45055)
        if _a_(45057, _n_(45056, "self", lambda: self), "head"):
            _l_(45071)

            _a_(45059, _n_(45058, "self", lambda: self), "head").next = _n_(45060, "node", lambda: node)
            _l_(45061)
            _n_(45062, "self", lambda: self).head = _n_(45063, "node", lambda: node)
            _l_(45064)
        else:
            _n_(45065, "self", lambda: self).tail = _n_(45066, "node", lambda: node)
            _l_(45067)
            _n_(45068, "self", lambda: self).head = _n_(45069, "node", lambda: node)
            _l_(45070)
        _n_(45072, "self", lambda: self).count += 1
        _l_(45073)

    def __getitem__(self, index):
        _l_(45093)

        if _n_(45075, "index", lambda: index) > _a_(45077, _n_(45076, "self", lambda: self), "count") - 1:
            _l_(45079)

            aux = 'Index out of range'
            _l_(45078)
            return aux
        current_val = _a_(45081, _n_(45080, "self", lambda: self), "tail")
        _l_(45082)
        for n in _c_(45085, _n_(45083, "range", lambda: range), _n_(45084, "index", lambda: index)):
            _l_(45089)

            current_val = _a_(45087, _n_(45086, "current_val", lambda: current_val), "next")
            _l_(45088)
        aux = _a_(45091, _n_(45090, "current_val", lambda: current_val), "data")
        _l_(45092)
        return aux

    def __setitem__(self, index, value):
        _l_(45114)

        if _n_(45094, "index", lambda: index) > _a_(45096, _n_(45095, "self", lambda: self), "count") - 1:
            _l_(45100)

            raise _c_(45098, _n_(45097, "Exception", lambda: Exception), 'Index out of range.')
            _l_(45099)
        current = _a_(45102, _n_(45101, "self", lambda: self), "tail")
        _l_(45103)
        for n in _c_(45106, _n_(45104, "range", lambda: range), _n_(45105, "index", lambda: index)):
            _l_(45110)

            current = _a_(45108, _n_(45107, "current", lambda: current), "next")
            _l_(45109)
        _n_(45111, "current", lambda: current).data = _n_(45112, "value", lambda: value)
        _l_(45113)
items = _c_(45117, _n_(45116, "singly_linked_list", lambda: singly_linked_list))
_l_(45118)
_c_(45121, _a_(45120, _n_(45119, "items", lambda: items), "append_item"), 'PHP')
_l_(45122)
_c_(45125, _a_(45124, _n_(45123, "items", lambda: items), "append_item"), 'Python')
_l_(45126)
_c_(45129, _a_(45128, _n_(45127, "items", lambda: items), "append_item"), 'C#')
_l_(45130)
_c_(45133, _a_(45132, _n_(45131, "items", lambda: items), "append_item"), 'C++')
_l_(45134)
_c_(45137, _a_(45136, _n_(45135, "items", lambda: items), "append_item"), 'Java')
_l_(45138)
_c_(45140, _n_(45139, "print", lambda: print), 'Modify items by index:')
_l_(45141)
_n_(45142, "items", lambda: items)[1] = 'SQL'
_l_(45143)
_c_(45146, _n_(45144, "print", lambda: print), 'New value: ', _n_(45145, "items", lambda: items)[1])
_l_(45147)
_n_(45148, "items", lambda: items)[4] = 'Perl'
_l_(45149)
_c_(45152, _n_(45150, "print", lambda: print), 'New value: ', _n_(45151, "items", lambda: items)[4])
_l_(45153)