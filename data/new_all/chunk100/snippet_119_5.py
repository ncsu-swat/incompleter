# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node:
    _l_(7476)


    def __init__(self, data=None):
        _l_(7475)

        _n_(7470, "self", lambda: self).data = _n_(7471, "data", lambda: data)
        _l_(7472)
        _n_(7473, "self", lambda: self).next = None
        _l_(7474)

class singly_linked_list:
    _l_(7551)


    def __init__(self):
        _l_(7483)

        _n_(7477, "self", lambda: self).tail = None
        _l_(7478)
        _n_(7479, "self", lambda: self).head = None
        _l_(7480)
        _n_(7481, "self", lambda: self).count = 0
        _l_(7482)

    def append_item(self, data):
        _l_(7506)

        node = _c_(7486, _n_(7484, "Node", lambda: Node), _n_(7485, "data", lambda: data))
        _l_(7487)
        if _a_(7489, _n_(7488, "self", lambda: self), "head"):
            _l_(7503)

            _a_(7491, _n_(7490, "self", lambda: self), "head").next = _n_(7492, "node", lambda: node)
            _l_(7493)
            _n_(7494, "self", lambda: self).head = _n_(7495, "node", lambda: node)
            _l_(7496)
        else:
            _n_(7497, "self", lambda: self).tail = _n_(7498, "node", lambda: node)
            _l_(7499)
            _n_(7500, "self", lambda: self).head = _n_(7501, "node", lambda: node)
            _l_(7502)
        _n_(7504, "self", lambda: self).count += 1
        _l_(7505)

    def delete_item(self, data):
        _l_(7539)

        current = _a_(7508, _n_(7507, "self", lambda: self), "tail")
        _l_(7509)
        prev = _a_(7511, _n_(7510, "self", lambda: self), "tail")
        _l_(7512)
        while _n_(7513, "current", lambda: current):
            _l_(7538)

            if _a_(7515, _n_(7514, "current", lambda: current), "data") == _n_(7516, "data", lambda: data):
                _l_(7532)

                if _n_(7517, "current", lambda: current) == _a_(7519, _n_(7518, "self", lambda: self), "tail"):
                    _l_(7528)

                    _n_(7520, "self", lambda: self).tail = _a_(7522, _n_(7521, "current", lambda: current), "next")
                    _l_(7523)
                else:
                    _n_(7524, "prev", lambda: prev).next = _a_(7526, _n_(7525, "current", lambda: current), "next")
                    _l_(7527)
                _n_(7529, "self", lambda: self).count -= 1
                _l_(7530)
                aux = ""
                _l_(7531)
                return aux
            prev = _n_(7533, "current", lambda: current)
            _l_(7534)
            current = _a_(7536, _n_(7535, "current", lambda: current), "next")
            _l_(7537)

    def iterate_item(self):
        _l_(7550)

        current_item = _a_(7541, _n_(7540, "self", lambda: self), "tail")
        _l_(7542)
        while _n_(7543, "current_item", lambda: current_item):
            _l_(7549)

            val = _a_(7545, _n_(7544, "current_item", lambda: current_item), "data")
            _l_(7546)
            yield _n_(7547, "val", lambda: val)
            _l_(7548)
items = _c_(7553, _n_(7552, "singly_linked_list", lambda: singly_linked_list))
_l_(7554)
_c_(7557, _a_(7556, _n_(7555, "items", lambda: items), "append_item"), 'PHP')
_l_(7558)
_c_(7561, _a_(7560, _n_(7559, "items", lambda: items), "append_item"), 'Python')
_l_(7562)
_c_(7565, _a_(7564, _n_(7563, "items", lambda: items), "append_item"), 'C#')
_l_(7566)
_c_(7569, _a_(7568, _n_(7567, "items", lambda: items), "append_item"), 'C++')
_l_(7570)
_c_(7573, _a_(7572, _n_(7571, "items", lambda: items), "append_item"), 'Java')
_l_(7574)
_c_(7576, _n_(7575, "print", lambda: print), 'Original list:')
_l_(7577)
for val in _c_(7580, _a_(7579, _n_(7578, "items", lambda: items), "iterate_item")):
    _l_(7585)

    _c_(7583, _n_(7581, "print", lambda: print), _n_(7582, "val", lambda: val))
    _l_(7584)
_c_(7587, _n_(7586, "print", lambda: print), '\nAfter removing the first item from the list:')
_l_(7588)
_c_(7591, _a_(7590, _n_(7589, "items", lambda: items), "delete_item"), 'PHP')
_l_(7592)
for val in _c_(7595, _a_(7594, _n_(7593, "items", lambda: items), "iterate_item")):
    _l_(7600)

    _c_(7598, _n_(7596, "print", lambda: print), _n_(7597, "val", lambda: val))
    _l_(7599)