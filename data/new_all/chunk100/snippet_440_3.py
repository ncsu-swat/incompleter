# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node:
    _l_(45272)


    def __init__(self, data=None):
        _l_(45271)

        _n_(45266, "self", lambda: self).data = _n_(45267, "data", lambda: data)
        _l_(45268)
        _n_(45269, "self", lambda: self).next = None
        _l_(45270)

class singly_linked_list:
    _l_(45340)


    def __init__(self):
        _l_(45279)

        _n_(45273, "self", lambda: self).tail = None
        _l_(45274)
        _n_(45275, "self", lambda: self).head = None
        _l_(45276)
        _n_(45277, "self", lambda: self).count = 0
        _l_(45278)

    def append_item(self, data):
        _l_(45299)

        node = _c_(45282, _n_(45280, "Node", lambda: Node), _n_(45281, "data", lambda: data))
        _l_(45283)
        if _a_(45285, _n_(45284, "self", lambda: self), "head"):
            _l_(45296)

            _a_(45287, _n_(45286, "self", lambda: self), "head").next = _n_(45288, "node", lambda: node)
            _l_(45289)
        else:
            _n_(45290, "self", lambda: self).tail = _n_(45291, "node", lambda: node)
            _l_(45292)
            _n_(45293, "self", lambda: self).head = _n_(45294, "node", lambda: node)
            _l_(45295)
        _n_(45297, "self", lambda: self).count += 1
        _l_(45298)

    def __getitem__(self, index):
        _l_(45318)

        if _n_(45300, "index", lambda: index) > _a_(45302, _n_(45301, "self", lambda: self), "count") - 1:
            _l_(45304)

            aux = 'Index out of range'
            _l_(45303)
            return aux
        current_val = _a_(45306, _n_(45305, "self", lambda: self), "tail")
        _l_(45307)
        for n in _c_(45310, _n_(45308, "range", lambda: range), _n_(45309, "index", lambda: index)):
            _l_(45314)

            current_val = _a_(45312, _n_(45311, "current_val", lambda: current_val), "next")
            _l_(45313)
        aux = _a_(45316, _n_(45315, "current_val", lambda: current_val), "data")
        _l_(45317)
        return aux

    def __setitem__(self, index, value):
        _l_(45339)

        if _n_(45319, "index", lambda: index) > _a_(45321, _n_(45320, "self", lambda: self), "count") - 1:
            _l_(45325)

            raise _c_(45323, _n_(45322, "Exception", lambda: Exception), 'Index out of range.')
            _l_(45324)
        current = _a_(45327, _n_(45326, "self", lambda: self), "tail")
        _l_(45328)
        for n in _c_(45331, _n_(45329, "range", lambda: range), _n_(45330, "index", lambda: index)):
            _l_(45335)

            current = _a_(45333, _n_(45332, "current", lambda: current), "next")
            _l_(45334)
        _n_(45336, "current", lambda: current).data = _n_(45337, "value", lambda: value)
        _l_(45338)
items = _c_(45342, _n_(45341, "singly_linked_list", lambda: singly_linked_list))
_l_(45343)
_c_(45346, _a_(45345, _n_(45344, "items", lambda: items), "append_item"), 'PHP')
_l_(45347)
_c_(45350, _a_(45349, _n_(45348, "items", lambda: items), "append_item"), 'Python')
_l_(45351)
_c_(45354, _a_(45353, _n_(45352, "items", lambda: items), "append_item"), 'C#')
_l_(45355)
_c_(45358, _a_(45357, _n_(45356, "items", lambda: items), "append_item"), 'C++')
_l_(45359)
_c_(45362, _a_(45361, _n_(45360, "items", lambda: items), "append_item"), 'Java')
_l_(45363)
_c_(45365, _n_(45364, "print", lambda: print), 'Modify items by index:')
_l_(45366)
_n_(45367, "items", lambda: items)[1] = 'SQL'
_l_(45368)
_c_(45371, _n_(45369, "print", lambda: print), 'New value: ', _n_(45370, "items", lambda: items)[1])
_l_(45372)
_n_(45373, "items", lambda: items)[4] = 'Perl'
_l_(45374)
_c_(45377, _n_(45375, "print", lambda: print), 'New value: ', _n_(45376, "items", lambda: items)[4])
_l_(45378)