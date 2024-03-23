# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node(_n_(20899, "object", lambda: object)):
    _l_(20907)


    def __init__(self, data=None, next=None, prev=None):
        _l_(20906)

        _n_(20900, "self", lambda: self).next = _n_(20901, "next", lambda: next)
        _l_(20902)
        _n_(20903, "self", lambda: self).prev = _n_(20904, "prev", lambda: prev)
        _l_(20905)

class doubly_linked_list(_n_(20908, "object", lambda: object)):
    _l_(20944)


    def __init__(self):
        _l_(20915)

        _n_(20909, "self", lambda: self).head = None
        _l_(20910)
        _n_(20911, "self", lambda: self).tail = None
        _l_(20912)
        _n_(20913, "self", lambda: self).count = 0
        _l_(20914)

    def append_item(self, data):
        _l_(20943)

        new_item = _c_(20918, _n_(20916, "Node", lambda: Node), _n_(20917, "data", lambda: data), None, None)
        _l_(20919)
        if _a_(20921, _n_(20920, "self", lambda: self), "head") is None:
            _l_(20940)

            _n_(20922, "self", lambda: self).head = _n_(20923, "new_item", lambda: new_item)
            _l_(20924)
            _n_(20925, "self", lambda: self).tail = _a_(20927, _n_(20926, "self", lambda: self), "head")
            _l_(20928)
        else:
            _n_(20929, "new_item", lambda: new_item).prev = _a_(20931, _n_(20930, "self", lambda: self), "tail")
            _l_(20932)
            _a_(20934, _n_(20933, "self", lambda: self), "tail").next = _n_(20935, "new_item", lambda: new_item)
            _l_(20936)
            _n_(20937, "self", lambda: self).tail = _n_(20938, "new_item", lambda: new_item)
            _l_(20939)
        _n_(20941, "self", lambda: self).count += 1
        _l_(20942)
items = _c_(20946, _n_(20945, "doubly_linked_list", lambda: doubly_linked_list))
_l_(20947)
_c_(20950, _a_(20949, _n_(20948, "items", lambda: items), "append_item"), 'PHP')
_l_(20951)
_c_(20954, _a_(20953, _n_(20952, "items", lambda: items), "append_item"), 'Python')
_l_(20955)
_c_(20958, _a_(20957, _n_(20956, "items", lambda: items), "append_item"), 'C#')
_l_(20959)
_c_(20962, _a_(20961, _n_(20960, "items", lambda: items), "append_item"), 'C++')
_l_(20963)
_c_(20966, _a_(20965, _n_(20964, "items", lambda: items), "append_item"), 'Java')
_l_(20967)
_c_(20970, _a_(20969, _n_(20968, "items", lambda: items), "append_item"), 'SQL')
_l_(20971)
_c_(20975, _n_(20972, "print", lambda: print), 'Number of items of the  Doubly linked list:', _a_(20974, _n_(20973, "items", lambda: items), "count"))
_l_(20976)