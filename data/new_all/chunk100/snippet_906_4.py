# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node:
    _l_(90289)


    def __init__(self, data=None):
        _l_(90288)

        _n_(90283, "self", lambda: self).data = _n_(90284, "data", lambda: data)
        _l_(90285)
        _n_(90286, "self", lambda: self).next = None
        _l_(90287)

class singly_linked_list:
    _l_(90364)


    def __init__(self):
        _l_(90296)

        _n_(90290, "self", lambda: self).tail = None
        _l_(90291)
        _n_(90292, "self", lambda: self).head = None
        _l_(90293)
        _n_(90294, "self", lambda: self).count = 0
        _l_(90295)

    def append_item(self, data):
        _l_(90319)

        node = _c_(90299, _n_(90297, "Node", lambda: Node), _n_(90298, "data", lambda: data))
        _l_(90300)
        if _a_(90302, _n_(90301, "self", lambda: self), "head"):
            _l_(90316)

            _a_(90304, _n_(90303, "self", lambda: self), "head").next = _n_(90305, "node", lambda: node)
            _l_(90306)
            _n_(90307, "self", lambda: self).head = _n_(90308, "node", lambda: node)
            _l_(90309)
        else:
            _n_(90310, "self", lambda: self).tail = _n_(90311, "node", lambda: node)
            _l_(90312)
            _n_(90313, "self", lambda: self).head = _n_(90314, "node", lambda: node)
            _l_(90315)
        _n_(90317, "self", lambda: self).count += 1
        _l_(90318)

    def delete_item(self, data):
        _l_(90352)

        current = _a_(90321, _n_(90320, "self", lambda: self), "tail")
        _l_(90322)
        prev = _a_(90324, _n_(90323, "self", lambda: self), "tail")
        _l_(90325)
        while _n_(90326, "current", lambda: current):
            _l_(90351)

            if _a_(90328, _n_(90327, "current", lambda: current), "data") == _n_(90329, "data", lambda: data):
                _l_(90345)

                if _n_(90330, "current", lambda: current) == _a_(90332, _n_(90331, "self", lambda: self), "tail"):
                    _l_(90341)

                    _n_(90333, "self", lambda: self).tail = _a_(90335, _n_(90334, "current", lambda: current), "next")
                    _l_(90336)
                else:
                    _n_(90337, "prev", lambda: prev).next = _a_(90339, _n_(90338, "current", lambda: current), "next")
                    _l_(90340)
                _n_(90342, "self", lambda: self).count -= 1
                _l_(90343)
                aux = ""
                _l_(90344)
                return aux
            prev = _n_(90346, "current", lambda: current)
            _l_(90347)
            current = _a_(90349, _n_(90348, "current", lambda: current), "next")
            _l_(90350)

    def iterate_item(self):
        _l_(90363)

        current_item = _a_(90354, _n_(90353, "self", lambda: self), "tail")
        _l_(90355)
        while _n_(90356, "current_item", lambda: current_item):
            _l_(90362)

            val = _a_(90358, _n_(90357, "current_item", lambda: current_item), "data")
            _l_(90359)
            yield _n_(90360, "val", lambda: val)
            _l_(90361)
items = _c_(90366, _n_(90365, "singly_linked_list", lambda: singly_linked_list))
_l_(90367)
_c_(90370, _a_(90369, _n_(90368, "items", lambda: items), "append_item"), 'PHP')
_l_(90371)
_c_(90374, _a_(90373, _n_(90372, "items", lambda: items), "append_item"), 'Python')
_l_(90375)
_c_(90378, _a_(90377, _n_(90376, "items", lambda: items), "append_item"), 'C#')
_l_(90379)
_c_(90382, _a_(90381, _n_(90380, "items", lambda: items), "append_item"), 'C++')
_l_(90383)
_c_(90386, _a_(90385, _n_(90384, "items", lambda: items), "append_item"), 'Java')
_l_(90387)
_c_(90389, _n_(90388, "print", lambda: print), 'Original list:')
_l_(90390)
for val in _c_(90393, _a_(90392, _n_(90391, "items", lambda: items), "iterate_item")):
    _l_(90398)

    _c_(90396, _n_(90394, "print", lambda: print), _n_(90395, "val", lambda: val))
    _l_(90397)
_c_(90400, _n_(90399, "print", lambda: print), '\nAfter removing the last item from the list:')
_l_(90401)
_c_(90404, _a_(90403, _n_(90402, "items", lambda: items), "delete_item"), 'Java')
_l_(90405)
for val in _c_(90408, _a_(90407, _n_(90406, "items", lambda: items), "iterate_item")):
    _l_(90413)

    _c_(90411, _n_(90409, "print", lambda: print), _n_(90410, "val", lambda: val))
    _l_(90412)