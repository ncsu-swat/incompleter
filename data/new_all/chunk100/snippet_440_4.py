# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node:
    _l_(45385)


    def __init__(self, data=None):
        _l_(45384)

        _n_(45379, "self", lambda: self).data = _n_(45380, "data", lambda: data)
        _l_(45381)
        _n_(45382, "self", lambda: self).next = None
        _l_(45383)

class singly_linked_list:
    _l_(45454)


    def __init__(self):
        _l_(45390)

        _n_(45386, "self", lambda: self).tail = None
        _l_(45387)
        _n_(45388, "self", lambda: self).count = 0
        _l_(45389)

    def append_item(self, data):
        _l_(45413)

        node = _c_(45393, _n_(45391, "Node", lambda: Node), _n_(45392, "data", lambda: data))
        _l_(45394)
        if _a_(45396, _n_(45395, "self", lambda: self), "head"):
            _l_(45410)

            _a_(45398, _n_(45397, "self", lambda: self), "head").next = _n_(45399, "node", lambda: node)
            _l_(45400)
            _n_(45401, "self", lambda: self).head = _n_(45402, "node", lambda: node)
            _l_(45403)
        else:
            _n_(45404, "self", lambda: self).tail = _n_(45405, "node", lambda: node)
            _l_(45406)
            _n_(45407, "self", lambda: self).head = _n_(45408, "node", lambda: node)
            _l_(45409)
        _n_(45411, "self", lambda: self).count += 1
        _l_(45412)

    def __getitem__(self, index):
        _l_(45432)

        if _n_(45414, "index", lambda: index) > _a_(45416, _n_(45415, "self", lambda: self), "count") - 1:
            _l_(45418)

            aux = 'Index out of range'
            _l_(45417)
            return aux
        current_val = _a_(45420, _n_(45419, "self", lambda: self), "tail")
        _l_(45421)
        for n in _c_(45424, _n_(45422, "range", lambda: range), _n_(45423, "index", lambda: index)):
            _l_(45428)

            current_val = _a_(45426, _n_(45425, "current_val", lambda: current_val), "next")
            _l_(45427)
        aux = _a_(45430, _n_(45429, "current_val", lambda: current_val), "data")
        _l_(45431)
        return aux

    def __setitem__(self, index, value):
        _l_(45453)

        if _n_(45433, "index", lambda: index) > _a_(45435, _n_(45434, "self", lambda: self), "count") - 1:
            _l_(45439)

            raise _c_(45437, _n_(45436, "Exception", lambda: Exception), 'Index out of range.')
            _l_(45438)
        current = _a_(45441, _n_(45440, "self", lambda: self), "tail")
        _l_(45442)
        for n in _c_(45445, _n_(45443, "range", lambda: range), _n_(45444, "index", lambda: index)):
            _l_(45449)

            current = _a_(45447, _n_(45446, "current", lambda: current), "next")
            _l_(45448)
        _n_(45450, "current", lambda: current).data = _n_(45451, "value", lambda: value)
        _l_(45452)
items = _c_(45456, _n_(45455, "singly_linked_list", lambda: singly_linked_list))
_l_(45457)
_c_(45460, _a_(45459, _n_(45458, "items", lambda: items), "append_item"), 'PHP')
_l_(45461)
_c_(45464, _a_(45463, _n_(45462, "items", lambda: items), "append_item"), 'Python')
_l_(45465)
_c_(45468, _a_(45467, _n_(45466, "items", lambda: items), "append_item"), 'C#')
_l_(45469)
_c_(45472, _a_(45471, _n_(45470, "items", lambda: items), "append_item"), 'C++')
_l_(45473)
_c_(45476, _a_(45475, _n_(45474, "items", lambda: items), "append_item"), 'Java')
_l_(45477)
_c_(45479, _n_(45478, "print", lambda: print), 'Modify items by index:')
_l_(45480)
_n_(45481, "items", lambda: items)[1] = 'SQL'
_l_(45482)
_c_(45485, _n_(45483, "print", lambda: print), 'New value: ', _n_(45484, "items", lambda: items)[1])
_l_(45486)
_n_(45487, "items", lambda: items)[4] = 'Perl'
_l_(45488)
_c_(45491, _n_(45489, "print", lambda: print), 'New value: ', _n_(45490, "items", lambda: items)[4])
_l_(45492)