# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node:
    _l_(101242)


    def __init__(self, data=None):
        _l_(101241)

        _n_(101236, "self", lambda: self).data = _n_(101237, "data", lambda: data)
        _l_(101238)
        _n_(101239, "self", lambda: self).next = None
        _l_(101240)

class singly_linked_list:
    _l_(101320)


    def __init__(self):
        _l_(101249)

        _n_(101243, "self", lambda: self).tail = None
        _l_(101244)
        _n_(101245, "self", lambda: self).head = None
        _l_(101246)
        _n_(101247, "self", lambda: self).count = 0
        _l_(101248)

    def append_item(self, data):
        _l_(101272)

        node = _c_(101252, _n_(101250, "Node", lambda: Node), _n_(101251, "data", lambda: data))
        _l_(101253)
        if _a_(101255, _n_(101254, "self", lambda: self), "head"):
            _l_(101269)

            _a_(101257, _n_(101256, "self", lambda: self), "head").next = _n_(101258, "node", lambda: node)
            _l_(101259)
            _n_(101260, "self", lambda: self).head = _n_(101261, "node", lambda: node)
            _l_(101262)
        else:
            _n_(101263, "self", lambda: self).tail = _n_(101264, "node", lambda: node)
            _l_(101265)
            _n_(101266, "self", lambda: self).head = _n_(101267, "node", lambda: node)
            _l_(101268)
        _n_(101270, "self", lambda: self).count += 1
        _l_(101271)

    def delete_item(self, data):
        _l_(101305)

        current = _a_(101274, _n_(101273, "self", lambda: self), "tail")
        _l_(101275)
        prev = _a_(101277, _n_(101276, "self", lambda: self), "tail")
        _l_(101278)
        while _n_(101279, "current", lambda: current):
            _l_(101304)

            if _a_(101281, _n_(101280, "current", lambda: current), "data") == _n_(101282, "data", lambda: data):
                _l_(101298)

                if _n_(101283, "current", lambda: current) == _a_(101285, _n_(101284, "self", lambda: self), "tail"):
                    _l_(101294)

                    _n_(101286, "self", lambda: self).tail = _a_(101288, _n_(101287, "current", lambda: current), "next")
                    _l_(101289)
                else:
                    _n_(101290, "prev", lambda: prev).next = _a_(101292, _n_(101291, "current", lambda: current), "next")
                    _l_(101293)
                _n_(101295, "self", lambda: self).count -= 1
                _l_(101296)
                aux = ""
                _l_(101297)
                return aux
            prev = _n_(101299, "current", lambda: current)
            _l_(101300)
            current = _a_(101302, _n_(101301, "current", lambda: current), "next")
            _l_(101303)

    def iterate_item(self):
        _l_(101319)

        current_item = _a_(101307, _n_(101306, "self", lambda: self), "tail")
        _l_(101308)
        while _n_(101309, "current_item", lambda: current_item):
            _l_(101318)

            val = _a_(101311, _n_(101310, "current_item", lambda: current_item), "data")
            _l_(101312)
            current_item = _a_(101314, _n_(101313, "current_item", lambda: current_item), "next")
            _l_(101315)
            yield _n_(101316, "val", lambda: val)
            _l_(101317)
_c_(101323, _a_(101322, _n_(101321, "items", lambda: items), "append_item"), 'PHP')
_l_(101324)
_c_(101327, _a_(101326, _n_(101325, "items", lambda: items), "append_item"), 'Python')
_l_(101328)
_c_(101331, _a_(101330, _n_(101329, "items", lambda: items), "append_item"), 'C#')
_l_(101332)
_c_(101335, _a_(101334, _n_(101333, "items", lambda: items), "append_item"), 'C++')
_l_(101336)
_c_(101339, _a_(101338, _n_(101337, "items", lambda: items), "append_item"), 'Java')
_l_(101340)
_c_(101342, _n_(101341, "print", lambda: print), 'Original list:')
_l_(101343)
for val in _c_(101346, _a_(101345, _n_(101344, "items", lambda: items), "iterate_item")):
    _l_(101351)

    _c_(101349, _n_(101347, "print", lambda: print), _n_(101348, "val", lambda: val))
    _l_(101350)
_c_(101353, _n_(101352, "print", lambda: print), '\nAfter removing the first item from the list:')
_l_(101354)
_c_(101357, _a_(101356, _n_(101355, "items", lambda: items), "delete_item"), 'PHP')
_l_(101358)
for val in _c_(101361, _a_(101360, _n_(101359, "items", lambda: items), "iterate_item")):
    _l_(101366)

    _c_(101364, _n_(101362, "print", lambda: print), _n_(101363, "val", lambda: val))
    _l_(101365)