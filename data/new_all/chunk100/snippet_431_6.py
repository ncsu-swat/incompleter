# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node(_n_(43477, "object", lambda: object)):
    _l_(43488)


    def __init__(self, data=None, next=None, prev=None):
        _l_(43487)

        _n_(43478, "self", lambda: self).data = _n_(43479, "data", lambda: data)
        _l_(43480)
        _n_(43481, "self", lambda: self).next = _n_(43482, "next", lambda: next)
        _l_(43483)
        _n_(43484, "self", lambda: self).prev = _n_(43485, "prev", lambda: prev)
        _l_(43486)

class doubly_linked_list(_n_(43489, "object", lambda: object)):
    _l_(43555)


    def __init__(self):
        _l_(43496)

        _n_(43490, "self", lambda: self).head = None
        _l_(43491)
        _n_(43492, "self", lambda: self).tail = None
        _l_(43493)
        _n_(43494, "self", lambda: self).count = 0
        _l_(43495)

    def append_item(self, data):
        _l_(43524)

        new_item = _c_(43499, _n_(43497, "Node", lambda: Node), _n_(43498, "data", lambda: data), None, None)
        _l_(43500)
        if _a_(43502, _n_(43501, "self", lambda: self), "head") is None:
            _l_(43521)

            _n_(43503, "self", lambda: self).head = _n_(43504, "new_item", lambda: new_item)
            _l_(43505)
            _n_(43506, "self", lambda: self).tail = _a_(43508, _n_(43507, "self", lambda: self), "head")
            _l_(43509)
        else:
            _n_(43510, "new_item", lambda: new_item).prev = _a_(43512, _n_(43511, "self", lambda: self), "tail")
            _l_(43513)
            _a_(43515, _n_(43514, "self", lambda: self), "tail").next = _n_(43516, "new_item", lambda: new_item)
            _l_(43517)
            _n_(43518, "self", lambda: self).tail = _n_(43519, "new_item", lambda: new_item)
            _l_(43520)
        _n_(43522, "self", lambda: self).count += 1
        _l_(43523)

    def iter(self):
        _l_(43535)

        current = _a_(43526, _n_(43525, "self", lambda: self), "head")
        _l_(43527)
        while _n_(43528, "current", lambda: current):
            _l_(43534)

            current = _a_(43530, _n_(43529, "current", lambda: current), "next")
            _l_(43531)
            yield _n_(43532, "item_val", lambda: item_val)
            _l_(43533)

    def print_foward(self):
        _l_(43544)

        for node in _c_(43538, _a_(43537, _n_(43536, "self", lambda: self), "iter")):
            _l_(43543)

            _c_(43541, _n_(43539, "print", lambda: print), _n_(43540, "node", lambda: node))
            _l_(43542)

    def search_item(self, val):
        _l_(43554)

        for node in _c_(43547, _a_(43546, _n_(43545, "self", lambda: self), "iter")):
            _l_(43552)

            if _n_(43548, "val", lambda: val) == _n_(43549, "node", lambda: node):
                _l_(43551)

                aux = True
                _l_(43550)
                return aux
        aux = False
        _l_(43553)
        return aux
items = _c_(43557, _n_(43556, "doubly_linked_list", lambda: doubly_linked_list))
_l_(43558)
_c_(43561, _a_(43560, _n_(43559, "items", lambda: items), "append_item"), 'PHP')
_l_(43562)
_c_(43565, _a_(43564, _n_(43563, "items", lambda: items), "append_item"), 'Python')
_l_(43566)
_c_(43569, _a_(43568, _n_(43567, "items", lambda: items), "append_item"), 'C#')
_l_(43570)
_c_(43573, _a_(43572, _n_(43571, "items", lambda: items), "append_item"), 'C++')
_l_(43574)
_c_(43577, _a_(43576, _n_(43575, "items", lambda: items), "append_item"), 'Java')
_l_(43578)
_c_(43581, _a_(43580, _n_(43579, "items", lambda: items), "append_item"), 'SQL')
_l_(43582)
_c_(43584, _n_(43583, "print", lambda: print), 'Original list:')
_l_(43585)
_c_(43588, _a_(43587, _n_(43586, "items", lambda: items), "print_foward"))
_l_(43589)
_c_(43591, _n_(43590, "print", lambda: print), '\n')
_l_(43592)
if _c_(43595, _a_(43594, _n_(43593, "items", lambda: items), "search_item"), 'SQL'):
    _l_(43602)

    _c_(43597, _n_(43596, "print", lambda: print), 'True')
    _l_(43598)
else:
    _c_(43600, _n_(43599, "print", lambda: print), 'False')
    _l_(43601)
if _c_(43605, _a_(43604, _n_(43603, "items", lambda: items), "search_item"), 'C+'):
    _l_(43612)

    _c_(43607, _n_(43606, "print", lambda: print), 'True')
    _l_(43608)
else:
    _c_(43610, _n_(43609, "print", lambda: print), 'False')
    _l_(43611)