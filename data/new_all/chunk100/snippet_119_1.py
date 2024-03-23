# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node:
    _l_(6298)


    def __init__(self, data=None):
        _l_(6297)

        _n_(6292, "self", lambda: self).data = _n_(6293, "data", lambda: data)
        _l_(6294)
        _n_(6295, "self", lambda: self).next = None
        _l_(6296)

class singly_linked_list:
    _l_(6372)


    def __init__(self):
        _l_(6305)

        _n_(6299, "self", lambda: self).tail = None
        _l_(6300)
        _n_(6301, "self", lambda: self).head = None
        _l_(6302)
        _n_(6303, "self", lambda: self).count = 0
        _l_(6304)

    def append_item(self, data):
        _l_(6324)

        if _a_(6307, _n_(6306, "self", lambda: self), "head"):
            _l_(6321)

            _a_(6309, _n_(6308, "self", lambda: self), "head").next = _n_(6310, "node", lambda: node)
            _l_(6311)
            _n_(6312, "self", lambda: self).head = _n_(6313, "node", lambda: node)
            _l_(6314)
        else:
            _n_(6315, "self", lambda: self).tail = _n_(6316, "node", lambda: node)
            _l_(6317)
            _n_(6318, "self", lambda: self).head = _n_(6319, "node", lambda: node)
            _l_(6320)
        _n_(6322, "self", lambda: self).count += 1
        _l_(6323)

    def delete_item(self, data):
        _l_(6357)

        current = _a_(6326, _n_(6325, "self", lambda: self), "tail")
        _l_(6327)
        prev = _a_(6329, _n_(6328, "self", lambda: self), "tail")
        _l_(6330)
        while _n_(6331, "current", lambda: current):
            _l_(6356)

            if _a_(6333, _n_(6332, "current", lambda: current), "data") == _n_(6334, "data", lambda: data):
                _l_(6350)

                if _n_(6335, "current", lambda: current) == _a_(6337, _n_(6336, "self", lambda: self), "tail"):
                    _l_(6346)

                    _n_(6338, "self", lambda: self).tail = _a_(6340, _n_(6339, "current", lambda: current), "next")
                    _l_(6341)
                else:
                    _n_(6342, "prev", lambda: prev).next = _a_(6344, _n_(6343, "current", lambda: current), "next")
                    _l_(6345)
                _n_(6347, "self", lambda: self).count -= 1
                _l_(6348)
                aux = ""
                _l_(6349)
                return aux
            prev = _n_(6351, "current", lambda: current)
            _l_(6352)
            current = _a_(6354, _n_(6353, "current", lambda: current), "next")
            _l_(6355)

    def iterate_item(self):
        _l_(6371)

        current_item = _a_(6359, _n_(6358, "self", lambda: self), "tail")
        _l_(6360)
        while _n_(6361, "current_item", lambda: current_item):
            _l_(6370)

            val = _a_(6363, _n_(6362, "current_item", lambda: current_item), "data")
            _l_(6364)
            current_item = _a_(6366, _n_(6365, "current_item", lambda: current_item), "next")
            _l_(6367)
            yield _n_(6368, "val", lambda: val)
            _l_(6369)
items = _c_(6374, _n_(6373, "singly_linked_list", lambda: singly_linked_list))
_l_(6375)
_c_(6378, _a_(6377, _n_(6376, "items", lambda: items), "append_item"), 'PHP')
_l_(6379)
_c_(6382, _a_(6381, _n_(6380, "items", lambda: items), "append_item"), 'Python')
_l_(6383)
_c_(6386, _a_(6385, _n_(6384, "items", lambda: items), "append_item"), 'C#')
_l_(6387)
_c_(6390, _a_(6389, _n_(6388, "items", lambda: items), "append_item"), 'C++')
_l_(6391)
_c_(6394, _a_(6393, _n_(6392, "items", lambda: items), "append_item"), 'Java')
_l_(6395)
_c_(6397, _n_(6396, "print", lambda: print), 'Original list:')
_l_(6398)
for val in _c_(6401, _a_(6400, _n_(6399, "items", lambda: items), "iterate_item")):
    _l_(6406)

    _c_(6404, _n_(6402, "print", lambda: print), _n_(6403, "val", lambda: val))
    _l_(6405)
_c_(6408, _n_(6407, "print", lambda: print), '\nAfter removing the first item from the list:')
_l_(6409)
_c_(6412, _a_(6411, _n_(6410, "items", lambda: items), "delete_item"), 'PHP')
_l_(6413)
for val in _c_(6416, _a_(6415, _n_(6414, "items", lambda: items), "iterate_item")):
    _l_(6421)

    _c_(6419, _n_(6417, "print", lambda: print), _n_(6418, "val", lambda: val))
    _l_(6420)