# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node(_n_(28492, "object", lambda: object)):
    _l_(28500)


    def __init__(self, value=None, next=None, prev=None):
        _l_(28499)

        _n_(28493, "self", lambda: self).next = _n_(28494, "next", lambda: next)
        _l_(28495)
        _n_(28496, "self", lambda: self).prev = _n_(28497, "prev", lambda: prev)
        _l_(28498)

class doubly_linked_list(_n_(28501, "object", lambda: object)):
    _l_(28628)


    def __init__(self):
        _l_(28508)

        _n_(28502, "self", lambda: self).head = None
        _l_(28503)
        _n_(28504, "self", lambda: self).tail = None
        _l_(28505)
        _n_(28506, "self", lambda: self).count = 0
        _l_(28507)

    def append_item(self, value):
        _l_(28536)

        new_item = _c_(28511, _n_(28509, "Node", lambda: Node), _n_(28510, "value", lambda: value), None, None)
        _l_(28512)
        if _a_(28514, _n_(28513, "self", lambda: self), "head") is None:
            _l_(28533)

            _n_(28515, "self", lambda: self).head = _n_(28516, "new_item", lambda: new_item)
            _l_(28517)
            _n_(28518, "self", lambda: self).tail = _a_(28520, _n_(28519, "self", lambda: self), "head")
            _l_(28521)
        else:
            _n_(28522, "new_item", lambda: new_item).prev = _a_(28524, _n_(28523, "self", lambda: self), "tail")
            _l_(28525)
            _a_(28527, _n_(28526, "self", lambda: self), "tail").next = _n_(28528, "new_item", lambda: new_item)
            _l_(28529)
            _n_(28530, "self", lambda: self).tail = _n_(28531, "new_item", lambda: new_item)
            _l_(28532)
        _n_(28534, "self", lambda: self).count += 1
        _l_(28535)

    def iter(self):
        _l_(28550)

        current = _a_(28538, _n_(28537, "self", lambda: self), "head")
        _l_(28539)
        while _n_(28540, "current", lambda: current):
            _l_(28549)

            item_val = _a_(28542, _n_(28541, "current", lambda: current), "value")
            _l_(28543)
            current = _a_(28545, _n_(28544, "current", lambda: current), "next")
            _l_(28546)
            yield _n_(28547, "item_val", lambda: item_val)
            _l_(28548)

    def print_foward(self):
        _l_(28559)

        for node in _c_(28553, _a_(28552, _n_(28551, "self", lambda: self), "iter")):
            _l_(28558)

            _c_(28556, _n_(28554, "print", lambda: print), _n_(28555, "node", lambda: node))
            _l_(28557)

    def search_item(self, val):
        _l_(28569)

        for node in _c_(28562, _a_(28561, _n_(28560, "self", lambda: self), "iter")):
            _l_(28567)

            if _n_(28563, "val", lambda: val) == _n_(28564, "node", lambda: node):
                _l_(28566)

                aux = True
                _l_(28565)
                return aux
        aux = False
        _l_(28568)
        return aux

    def delete(self, value):
        _l_(28627)

        current = _a_(28571, _n_(28570, "self", lambda: self), "head")
        _l_(28572)
        node_deleted = False
        _l_(28573)
        if _n_(28574, "current", lambda: current) is None:
            _l_(28622)

            node_deleted = False
            _l_(28575)
        elif _a_(28577, _n_(28576, "current", lambda: current), "value") == _n_(28578, "value", lambda: value):
            _l_(28621)

            _n_(28579, "self", lambda: self).head = _a_(28581, _n_(28580, "current", lambda: current), "next")
            _l_(28582)
            _a_(28584, _n_(28583, "self", lambda: self), "head").prev = None
            _l_(28585)
            node_deleted = True
            _l_(28586)
        elif _a_(28589, _a_(28588, _n_(28587, "self", lambda: self), "tail"), "value") == _n_(28590, "value", lambda: value):
            _l_(28620)

            _n_(28591, "self", lambda: self).tail = _a_(28594, _a_(28593, _n_(28592, "self", lambda: self), "tail"), "prev")
            _l_(28595)
            _a_(28597, _n_(28596, "self", lambda: self), "tail").next = None
            _l_(28598)
            node_deleted = True
            _l_(28599)
        else:
            while _n_(28600, "current", lambda: current):
                _l_(28619)

                if _a_(28602, _n_(28601, "current", lambda: current), "value") == _n_(28603, "value", lambda: value):
                    _l_(28615)

                    _a_(28605, _n_(28604, "current", lambda: current), "prev").next = _a_(28607, _n_(28606, "current", lambda: current), "next")
                    _l_(28608)
                    _a_(28610, _n_(28609, "current", lambda: current), "next").prev = _a_(28612, _n_(28611, "current", lambda: current), "prev")
                    _l_(28613)
                    node_deleted = True
                    _l_(28614)
                current = _a_(28617, _n_(28616, "current", lambda: current), "next")
                _l_(28618)
        if _n_(28623, "node_deleted", lambda: node_deleted):
            _l_(28626)

            _n_(28624, "self", lambda: self).count -= 1
            _l_(28625)
items = _c_(28630, _n_(28629, "doubly_linked_list", lambda: doubly_linked_list))
_l_(28631)
_c_(28634, _a_(28633, _n_(28632, "items", lambda: items), "append_item"), 'PHP')
_l_(28635)
_c_(28638, _a_(28637, _n_(28636, "items", lambda: items), "append_item"), 'Python')
_l_(28639)
_c_(28642, _a_(28641, _n_(28640, "items", lambda: items), "append_item"), 'C#')
_l_(28643)
_c_(28646, _a_(28645, _n_(28644, "items", lambda: items), "append_item"), 'C++')
_l_(28647)
_c_(28650, _a_(28649, _n_(28648, "items", lambda: items), "append_item"), 'Java')
_l_(28651)
_c_(28654, _a_(28653, _n_(28652, "items", lambda: items), "append_item"), 'SQL')
_l_(28655)
_c_(28657, _n_(28656, "print", lambda: print), 'Original list:')
_l_(28658)
_c_(28661, _a_(28660, _n_(28659, "items", lambda: items), "print_foward"))
_l_(28662)
_c_(28665, _a_(28664, _n_(28663, "items", lambda: items), "delete"), 'Java')
_l_(28666)
_c_(28669, _a_(28668, _n_(28667, "items", lambda: items), "delete"), 'Python')
_l_(28670)
_c_(28672, _n_(28671, "print", lambda: print), '\nList after deleting two items:')
_l_(28673)
_c_(28676, _a_(28675, _n_(28674, "items", lambda: items), "print_foward"))
_l_(28677)