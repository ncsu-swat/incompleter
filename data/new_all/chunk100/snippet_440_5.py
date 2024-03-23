# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node:
    _l_(45499)


    def __init__(self, data=None):
        _l_(45498)

        _n_(45493, "self", lambda: self).data = _n_(45494, "data", lambda: data)
        _l_(45495)
        _n_(45496, "self", lambda: self).next = None
        _l_(45497)

class singly_linked_list:
    _l_(45568)


    def __init__(self):
        _l_(45504)

        _n_(45500, "self", lambda: self).tail = None
        _l_(45501)
        _n_(45502, "self", lambda: self).head = None
        _l_(45503)

    def append_item(self, data):
        _l_(45527)

        node = _c_(45507, _n_(45505, "Node", lambda: Node), _n_(45506, "data", lambda: data))
        _l_(45508)
        if _a_(45510, _n_(45509, "self", lambda: self), "head"):
            _l_(45524)

            _a_(45512, _n_(45511, "self", lambda: self), "head").next = _n_(45513, "node", lambda: node)
            _l_(45514)
            _n_(45515, "self", lambda: self).head = _n_(45516, "node", lambda: node)
            _l_(45517)
        else:
            _n_(45518, "self", lambda: self).tail = _n_(45519, "node", lambda: node)
            _l_(45520)
            _n_(45521, "self", lambda: self).head = _n_(45522, "node", lambda: node)
            _l_(45523)
        _n_(45525, "self", lambda: self).count += 1
        _l_(45526)

    def __getitem__(self, index):
        _l_(45546)

        if _n_(45528, "index", lambda: index) > _a_(45530, _n_(45529, "self", lambda: self), "count") - 1:
            _l_(45532)

            aux = 'Index out of range'
            _l_(45531)
            return aux
        current_val = _a_(45534, _n_(45533, "self", lambda: self), "tail")
        _l_(45535)
        for n in _c_(45538, _n_(45536, "range", lambda: range), _n_(45537, "index", lambda: index)):
            _l_(45542)

            current_val = _a_(45540, _n_(45539, "current_val", lambda: current_val), "next")
            _l_(45541)
        aux = _a_(45544, _n_(45543, "current_val", lambda: current_val), "data")
        _l_(45545)
        return aux

    def __setitem__(self, index, value):
        _l_(45567)

        if _n_(45547, "index", lambda: index) > _a_(45549, _n_(45548, "self", lambda: self), "count") - 1:
            _l_(45553)

            raise _c_(45551, _n_(45550, "Exception", lambda: Exception), 'Index out of range.')
            _l_(45552)
        current = _a_(45555, _n_(45554, "self", lambda: self), "tail")
        _l_(45556)
        for n in _c_(45559, _n_(45557, "range", lambda: range), _n_(45558, "index", lambda: index)):
            _l_(45563)

            current = _a_(45561, _n_(45560, "current", lambda: current), "next")
            _l_(45562)
        _n_(45564, "current", lambda: current).data = _n_(45565, "value", lambda: value)
        _l_(45566)
items = _c_(45570, _n_(45569, "singly_linked_list", lambda: singly_linked_list))
_l_(45571)
_c_(45574, _a_(45573, _n_(45572, "items", lambda: items), "append_item"), 'PHP')
_l_(45575)
_c_(45578, _a_(45577, _n_(45576, "items", lambda: items), "append_item"), 'Python')
_l_(45579)
_c_(45582, _a_(45581, _n_(45580, "items", lambda: items), "append_item"), 'C#')
_l_(45583)
_c_(45586, _a_(45585, _n_(45584, "items", lambda: items), "append_item"), 'C++')
_l_(45587)
_c_(45590, _a_(45589, _n_(45588, "items", lambda: items), "append_item"), 'Java')
_l_(45591)
_c_(45593, _n_(45592, "print", lambda: print), 'Modify items by index:')
_l_(45594)
_n_(45595, "items", lambda: items)[1] = 'SQL'
_l_(45596)
_c_(45599, _n_(45597, "print", lambda: print), 'New value: ', _n_(45598, "items", lambda: items)[1])
_l_(45600)
_n_(45601, "items", lambda: items)[4] = 'Perl'
_l_(45602)
_c_(45605, _n_(45603, "print", lambda: print), 'New value: ', _n_(45604, "items", lambda: items)[4])
_l_(45606)