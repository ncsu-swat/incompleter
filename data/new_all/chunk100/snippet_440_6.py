# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node:
    _l_(45611)


    def __init__(self, data=None):
        _l_(45610)

        _n_(45607, "self", lambda: self).data = _n_(45608, "data", lambda: data)
        _l_(45609)

class singly_linked_list:
    _l_(45682)


    def __init__(self):
        _l_(45618)

        _n_(45612, "self", lambda: self).tail = None
        _l_(45613)
        _n_(45614, "self", lambda: self).head = None
        _l_(45615)
        _n_(45616, "self", lambda: self).count = 0
        _l_(45617)

    def append_item(self, data):
        _l_(45641)

        node = _c_(45621, _n_(45619, "Node", lambda: Node), _n_(45620, "data", lambda: data))
        _l_(45622)
        if _a_(45624, _n_(45623, "self", lambda: self), "head"):
            _l_(45638)

            _a_(45626, _n_(45625, "self", lambda: self), "head").next = _n_(45627, "node", lambda: node)
            _l_(45628)
            _n_(45629, "self", lambda: self).head = _n_(45630, "node", lambda: node)
            _l_(45631)
        else:
            _n_(45632, "self", lambda: self).tail = _n_(45633, "node", lambda: node)
            _l_(45634)
            _n_(45635, "self", lambda: self).head = _n_(45636, "node", lambda: node)
            _l_(45637)
        _n_(45639, "self", lambda: self).count += 1
        _l_(45640)

    def __getitem__(self, index):
        _l_(45660)

        if _n_(45642, "index", lambda: index) > _a_(45644, _n_(45643, "self", lambda: self), "count") - 1:
            _l_(45646)

            aux = 'Index out of range'
            _l_(45645)
            return aux
        current_val = _a_(45648, _n_(45647, "self", lambda: self), "tail")
        _l_(45649)
        for n in _c_(45652, _n_(45650, "range", lambda: range), _n_(45651, "index", lambda: index)):
            _l_(45656)

            current_val = _a_(45654, _n_(45653, "current_val", lambda: current_val), "next")
            _l_(45655)
        aux = _a_(45658, _n_(45657, "current_val", lambda: current_val), "data")
        _l_(45659)
        return aux

    def __setitem__(self, index, value):
        _l_(45681)

        if _n_(45661, "index", lambda: index) > _a_(45663, _n_(45662, "self", lambda: self), "count") - 1:
            _l_(45667)

            raise _c_(45665, _n_(45664, "Exception", lambda: Exception), 'Index out of range.')
            _l_(45666)
        current = _a_(45669, _n_(45668, "self", lambda: self), "tail")
        _l_(45670)
        for n in _c_(45673, _n_(45671, "range", lambda: range), _n_(45672, "index", lambda: index)):
            _l_(45677)

            current = _a_(45675, _n_(45674, "current", lambda: current), "next")
            _l_(45676)
        _n_(45678, "current", lambda: current).data = _n_(45679, "value", lambda: value)
        _l_(45680)
items = _c_(45684, _n_(45683, "singly_linked_list", lambda: singly_linked_list))
_l_(45685)
_c_(45688, _a_(45687, _n_(45686, "items", lambda: items), "append_item"), 'PHP')
_l_(45689)
_c_(45692, _a_(45691, _n_(45690, "items", lambda: items), "append_item"), 'Python')
_l_(45693)
_c_(45696, _a_(45695, _n_(45694, "items", lambda: items), "append_item"), 'C#')
_l_(45697)
_c_(45700, _a_(45699, _n_(45698, "items", lambda: items), "append_item"), 'C++')
_l_(45701)
_c_(45704, _a_(45703, _n_(45702, "items", lambda: items), "append_item"), 'Java')
_l_(45705)
_c_(45707, _n_(45706, "print", lambda: print), 'Modify items by index:')
_l_(45708)
_n_(45709, "items", lambda: items)[1] = 'SQL'
_l_(45710)
_c_(45713, _n_(45711, "print", lambda: print), 'New value: ', _n_(45712, "items", lambda: items)[1])
_l_(45714)
_n_(45715, "items", lambda: items)[4] = 'Perl'
_l_(45716)
_c_(45719, _n_(45717, "print", lambda: print), 'New value: ', _n_(45718, "items", lambda: items)[4])
_l_(45720)