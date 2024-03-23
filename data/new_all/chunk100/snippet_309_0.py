# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node(_n_(26446, "object", lambda: object)):
    _l_(26457)


    def __init__(self, value=None, next=None, prev=None):
        _l_(26456)

        _n_(26447, "self", lambda: self).value = _n_(26448, "value", lambda: value)
        _l_(26449)
        _n_(26450, "self", lambda: self).next = _n_(26451, "next", lambda: next)
        _l_(26452)
        _n_(26453, "self", lambda: self).prev = _n_(26454, "prev", lambda: prev)
        _l_(26455)

class doubly_linked_list(_n_(26458, "object", lambda: object)):
    _l_(26583)


    def __init__(self):
        _l_(26463)

        _n_(26459, "self", lambda: self).head = None
        _l_(26460)
        _n_(26461, "self", lambda: self).tail = None
        _l_(26462)

    def append_item(self, value):
        _l_(26491)

        new_item = _c_(26466, _n_(26464, "Node", lambda: Node), _n_(26465, "value", lambda: value), None, None)
        _l_(26467)
        if _a_(26469, _n_(26468, "self", lambda: self), "head") is None:
            _l_(26488)

            _n_(26470, "self", lambda: self).head = _n_(26471, "new_item", lambda: new_item)
            _l_(26472)
            _n_(26473, "self", lambda: self).tail = _a_(26475, _n_(26474, "self", lambda: self), "head")
            _l_(26476)
        else:
            _n_(26477, "new_item", lambda: new_item).prev = _a_(26479, _n_(26478, "self", lambda: self), "tail")
            _l_(26480)
            _a_(26482, _n_(26481, "self", lambda: self), "tail").next = _n_(26483, "new_item", lambda: new_item)
            _l_(26484)
            _n_(26485, "self", lambda: self).tail = _n_(26486, "new_item", lambda: new_item)
            _l_(26487)
        _n_(26489, "self", lambda: self).count += 1
        _l_(26490)

    def iter(self):
        _l_(26505)

        current = _a_(26493, _n_(26492, "self", lambda: self), "head")
        _l_(26494)
        while _n_(26495, "current", lambda: current):
            _l_(26504)

            item_val = _a_(26497, _n_(26496, "current", lambda: current), "value")
            _l_(26498)
            current = _a_(26500, _n_(26499, "current", lambda: current), "next")
            _l_(26501)
            yield _n_(26502, "item_val", lambda: item_val)
            _l_(26503)

    def print_foward(self):
        _l_(26514)

        for node in _c_(26508, _a_(26507, _n_(26506, "self", lambda: self), "iter")):
            _l_(26513)

            _c_(26511, _n_(26509, "print", lambda: print), _n_(26510, "node", lambda: node))
            _l_(26512)

    def search_item(self, val):
        _l_(26524)

        for node in _c_(26517, _a_(26516, _n_(26515, "self", lambda: self), "iter")):
            _l_(26522)

            if _n_(26518, "val", lambda: val) == _n_(26519, "node", lambda: node):
                _l_(26521)

                aux = True
                _l_(26520)
                return aux
        aux = False
        _l_(26523)
        return aux

    def delete(self, value):
        _l_(26582)

        current = _a_(26526, _n_(26525, "self", lambda: self), "head")
        _l_(26527)
        node_deleted = False
        _l_(26528)
        if _n_(26529, "current", lambda: current) is None:
            _l_(26577)

            node_deleted = False
            _l_(26530)
        elif _a_(26532, _n_(26531, "current", lambda: current), "value") == _n_(26533, "value", lambda: value):
            _l_(26576)

            _n_(26534, "self", lambda: self).head = _a_(26536, _n_(26535, "current", lambda: current), "next")
            _l_(26537)
            _a_(26539, _n_(26538, "self", lambda: self), "head").prev = None
            _l_(26540)
            node_deleted = True
            _l_(26541)
        elif _a_(26544, _a_(26543, _n_(26542, "self", lambda: self), "tail"), "value") == _n_(26545, "value", lambda: value):
            _l_(26575)

            _n_(26546, "self", lambda: self).tail = _a_(26549, _a_(26548, _n_(26547, "self", lambda: self), "tail"), "prev")
            _l_(26550)
            _a_(26552, _n_(26551, "self", lambda: self), "tail").next = None
            _l_(26553)
            node_deleted = True
            _l_(26554)
        else:
            while _n_(26555, "current", lambda: current):
                _l_(26574)

                if _a_(26557, _n_(26556, "current", lambda: current), "value") == _n_(26558, "value", lambda: value):
                    _l_(26570)

                    _a_(26560, _n_(26559, "current", lambda: current), "prev").next = _a_(26562, _n_(26561, "current", lambda: current), "next")
                    _l_(26563)
                    _a_(26565, _n_(26564, "current", lambda: current), "next").prev = _a_(26567, _n_(26566, "current", lambda: current), "prev")
                    _l_(26568)
                    node_deleted = True
                    _l_(26569)
                current = _a_(26572, _n_(26571, "current", lambda: current), "next")
                _l_(26573)
        if _n_(26578, "node_deleted", lambda: node_deleted):
            _l_(26581)

            _n_(26579, "self", lambda: self).count -= 1
            _l_(26580)
items = _c_(26585, _n_(26584, "doubly_linked_list", lambda: doubly_linked_list))
_l_(26586)
_c_(26589, _a_(26588, _n_(26587, "items", lambda: items), "append_item"), 'PHP')
_l_(26590)
_c_(26593, _a_(26592, _n_(26591, "items", lambda: items), "append_item"), 'Python')
_l_(26594)
_c_(26597, _a_(26596, _n_(26595, "items", lambda: items), "append_item"), 'C#')
_l_(26598)
_c_(26601, _a_(26600, _n_(26599, "items", lambda: items), "append_item"), 'C++')
_l_(26602)
_c_(26605, _a_(26604, _n_(26603, "items", lambda: items), "append_item"), 'Java')
_l_(26606)
_c_(26609, _a_(26608, _n_(26607, "items", lambda: items), "append_item"), 'SQL')
_l_(26610)
_c_(26612, _n_(26611, "print", lambda: print), 'Original list:')
_l_(26613)
_c_(26616, _a_(26615, _n_(26614, "items", lambda: items), "print_foward"))
_l_(26617)
_c_(26620, _a_(26619, _n_(26618, "items", lambda: items), "delete"), 'Java')
_l_(26621)
_c_(26624, _a_(26623, _n_(26622, "items", lambda: items), "delete"), 'Python')
_l_(26625)
_c_(26627, _n_(26626, "print", lambda: print), '\nList after deleting two items:')
_l_(26628)
_c_(26631, _a_(26630, _n_(26629, "items", lambda: items), "print_foward"))
_l_(26632)