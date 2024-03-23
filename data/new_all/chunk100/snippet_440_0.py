# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node:
    _l_(44595)


    def __init__(self, data=None):
        _l_(44594)

        _n_(44589, "self", lambda: self).data = _n_(44590, "data", lambda: data)
        _l_(44591)
        _n_(44592, "self", lambda: self).next = None
        _l_(44593)

class singly_linked_list:
    _l_(44663)


    def __init__(self):
        _l_(44602)

        _n_(44596, "self", lambda: self).tail = None
        _l_(44597)
        _n_(44598, "self", lambda: self).head = None
        _l_(44599)
        _n_(44600, "self", lambda: self).count = 0
        _l_(44601)

    def append_item(self, data):
        _l_(44625)

        node = _c_(44605, _n_(44603, "Node", lambda: Node), _n_(44604, "data", lambda: data))
        _l_(44606)
        if _a_(44608, _n_(44607, "self", lambda: self), "head"):
            _l_(44622)

            _a_(44610, _n_(44609, "self", lambda: self), "head").next = _n_(44611, "node", lambda: node)
            _l_(44612)
            _n_(44613, "self", lambda: self).head = _n_(44614, "node", lambda: node)
            _l_(44615)
        else:
            _n_(44616, "self", lambda: self).tail = _n_(44617, "node", lambda: node)
            _l_(44618)
            _n_(44619, "self", lambda: self).head = _n_(44620, "node", lambda: node)
            _l_(44621)
        _n_(44623, "self", lambda: self).count += 1
        _l_(44624)

    def __getitem__(self, index):
        _l_(44644)

        if _n_(44626, "index", lambda: index) > _a_(44628, _n_(44627, "self", lambda: self), "count") - 1:
            _l_(44630)

            aux = 'Index out of range'
            _l_(44629)
            return aux
        current_val = _a_(44632, _n_(44631, "self", lambda: self), "tail")
        _l_(44633)
        for n in _c_(44636, _n_(44634, "range", lambda: range), _n_(44635, "index", lambda: index)):
            _l_(44640)

            current_val = _a_(44638, _n_(44637, "current_val", lambda: current_val), "next")
            _l_(44639)
        aux = _a_(44642, _n_(44641, "current_val", lambda: current_val), "data")
        _l_(44643)
        return aux

    def __setitem__(self, index, value):
        _l_(44662)

        if _n_(44645, "index", lambda: index) > _a_(44647, _n_(44646, "self", lambda: self), "count") - 1:
            _l_(44651)

            raise _c_(44649, _n_(44648, "Exception", lambda: Exception), 'Index out of range.')
            _l_(44650)
        current = _a_(44653, _n_(44652, "self", lambda: self), "tail")
        _l_(44654)
        for n in _c_(44657, _n_(44655, "range", lambda: range), _n_(44656, "index", lambda: index)):
            _l_(44661)

            current = _a_(44659, _n_(44658, "current", lambda: current), "next")
            _l_(44660)
items = _c_(44665, _n_(44664, "singly_linked_list", lambda: singly_linked_list))
_l_(44666)
_c_(44669, _a_(44668, _n_(44667, "items", lambda: items), "append_item"), 'PHP')
_l_(44670)
_c_(44673, _a_(44672, _n_(44671, "items", lambda: items), "append_item"), 'Python')
_l_(44674)
_c_(44677, _a_(44676, _n_(44675, "items", lambda: items), "append_item"), 'C#')
_l_(44678)
_c_(44681, _a_(44680, _n_(44679, "items", lambda: items), "append_item"), 'C++')
_l_(44682)
_c_(44685, _a_(44684, _n_(44683, "items", lambda: items), "append_item"), 'Java')
_l_(44686)
_c_(44688, _n_(44687, "print", lambda: print), 'Modify items by index:')
_l_(44689)
_n_(44690, "items", lambda: items)[1] = 'SQL'
_l_(44691)
_c_(44694, _n_(44692, "print", lambda: print), 'New value: ', _n_(44693, "items", lambda: items)[1])
_l_(44695)
_n_(44696, "items", lambda: items)[4] = 'Perl'
_l_(44697)
_c_(44700, _n_(44698, "print", lambda: print), 'New value: ', _n_(44699, "items", lambda: items)[4])
_l_(44701)