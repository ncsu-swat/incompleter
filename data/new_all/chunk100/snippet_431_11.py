# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node(_n_(42526, "object", lambda: object)):
    _l_(42537)


    def __init__(self, data=None, next=None, prev=None):
        _l_(42536)

        _n_(42527, "self", lambda: self).data = _n_(42528, "data", lambda: data)
        _l_(42529)
        _n_(42530, "self", lambda: self).next = _n_(42531, "next", lambda: next)
        _l_(42532)
        _n_(42533, "self", lambda: self).prev = _n_(42534, "prev", lambda: prev)
        _l_(42535)

class doubly_linked_list(_n_(42538, "object", lambda: object)):
    _l_(42604)


    def __init__(self):
        _l_(42545)

        _n_(42539, "self", lambda: self).head = None
        _l_(42540)
        _n_(42541, "self", lambda: self).tail = None
        _l_(42542)
        _n_(42543, "self", lambda: self).count = 0
        _l_(42544)

    def append_item(self, data):
        _l_(42573)

        new_item = _c_(42548, _n_(42546, "Node", lambda: Node), _n_(42547, "data", lambda: data), None, None)
        _l_(42549)
        if _a_(42551, _n_(42550, "self", lambda: self), "head") is None:
            _l_(42570)

            _n_(42552, "self", lambda: self).head = _n_(42553, "new_item", lambda: new_item)
            _l_(42554)
            _n_(42555, "self", lambda: self).tail = _a_(42557, _n_(42556, "self", lambda: self), "head")
            _l_(42558)
        else:
            _n_(42559, "new_item", lambda: new_item).prev = _a_(42561, _n_(42560, "self", lambda: self), "tail")
            _l_(42562)
            _a_(42564, _n_(42563, "self", lambda: self), "tail").next = _n_(42565, "new_item", lambda: new_item)
            _l_(42566)
            _n_(42567, "self", lambda: self).tail = _n_(42568, "new_item", lambda: new_item)
            _l_(42569)
        _n_(42571, "self", lambda: self).count += 1
        _l_(42572)

    def iter(self):
        _l_(42584)

        while _n_(42574, "current", lambda: current):
            _l_(42583)

            item_val = _a_(42576, _n_(42575, "current", lambda: current), "data")
            _l_(42577)
            current = _a_(42579, _n_(42578, "current", lambda: current), "next")
            _l_(42580)
            yield _n_(42581, "item_val", lambda: item_val)
            _l_(42582)

    def print_foward(self):
        _l_(42593)

        for node in _c_(42587, _a_(42586, _n_(42585, "self", lambda: self), "iter")):
            _l_(42592)

            _c_(42590, _n_(42588, "print", lambda: print), _n_(42589, "node", lambda: node))
            _l_(42591)

    def search_item(self, val):
        _l_(42603)

        for node in _c_(42596, _a_(42595, _n_(42594, "self", lambda: self), "iter")):
            _l_(42601)

            if _n_(42597, "val", lambda: val) == _n_(42598, "node", lambda: node):
                _l_(42600)

                aux = True
                _l_(42599)
                return aux
        aux = False
        _l_(42602)
        return aux
items = _c_(42606, _n_(42605, "doubly_linked_list", lambda: doubly_linked_list))
_l_(42607)
_c_(42610, _a_(42609, _n_(42608, "items", lambda: items), "append_item"), 'PHP')
_l_(42611)
_c_(42614, _a_(42613, _n_(42612, "items", lambda: items), "append_item"), 'Python')
_l_(42615)
_c_(42618, _a_(42617, _n_(42616, "items", lambda: items), "append_item"), 'C#')
_l_(42619)
_c_(42622, _a_(42621, _n_(42620, "items", lambda: items), "append_item"), 'C++')
_l_(42623)
_c_(42626, _a_(42625, _n_(42624, "items", lambda: items), "append_item"), 'Java')
_l_(42627)
_c_(42630, _a_(42629, _n_(42628, "items", lambda: items), "append_item"), 'SQL')
_l_(42631)
_c_(42633, _n_(42632, "print", lambda: print), 'Original list:')
_l_(42634)
_c_(42637, _a_(42636, _n_(42635, "items", lambda: items), "print_foward"))
_l_(42638)
_c_(42640, _n_(42639, "print", lambda: print), '\n')
_l_(42641)
if _c_(42644, _a_(42643, _n_(42642, "items", lambda: items), "search_item"), 'SQL'):
    _l_(42651)

    _c_(42646, _n_(42645, "print", lambda: print), 'True')
    _l_(42647)
else:
    _c_(42649, _n_(42648, "print", lambda: print), 'False')
    _l_(42650)
if _c_(42654, _a_(42653, _n_(42652, "items", lambda: items), "search_item"), 'C+'):
    _l_(42661)

    _c_(42656, _n_(42655, "print", lambda: print), 'True')
    _l_(42657)
else:
    _c_(42659, _n_(42658, "print", lambda: print), 'False')
    _l_(42660)