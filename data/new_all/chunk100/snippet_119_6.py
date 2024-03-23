# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node:
    _l_(7607)


    def __init__(self, data=None):
        _l_(7606)

        _n_(7601, "self", lambda: self).data = _n_(7602, "data", lambda: data)
        _l_(7603)
        _n_(7604, "self", lambda: self).next = None
        _l_(7605)

class singly_linked_list:
    _l_(7683)


    def __init__(self):
        _l_(7612)

        _n_(7608, "self", lambda: self).tail = None
        _l_(7609)
        _n_(7610, "self", lambda: self).count = 0
        _l_(7611)

    def append_item(self, data):
        _l_(7635)

        node = _c_(7615, _n_(7613, "Node", lambda: Node), _n_(7614, "data", lambda: data))
        _l_(7616)
        if _a_(7618, _n_(7617, "self", lambda: self), "head"):
            _l_(7632)

            _a_(7620, _n_(7619, "self", lambda: self), "head").next = _n_(7621, "node", lambda: node)
            _l_(7622)
            _n_(7623, "self", lambda: self).head = _n_(7624, "node", lambda: node)
            _l_(7625)
        else:
            _n_(7626, "self", lambda: self).tail = _n_(7627, "node", lambda: node)
            _l_(7628)
            _n_(7629, "self", lambda: self).head = _n_(7630, "node", lambda: node)
            _l_(7631)
        _n_(7633, "self", lambda: self).count += 1
        _l_(7634)

    def delete_item(self, data):
        _l_(7668)

        current = _a_(7637, _n_(7636, "self", lambda: self), "tail")
        _l_(7638)
        prev = _a_(7640, _n_(7639, "self", lambda: self), "tail")
        _l_(7641)
        while _n_(7642, "current", lambda: current):
            _l_(7667)

            if _a_(7644, _n_(7643, "current", lambda: current), "data") == _n_(7645, "data", lambda: data):
                _l_(7661)

                if _n_(7646, "current", lambda: current) == _a_(7648, _n_(7647, "self", lambda: self), "tail"):
                    _l_(7657)

                    _n_(7649, "self", lambda: self).tail = _a_(7651, _n_(7650, "current", lambda: current), "next")
                    _l_(7652)
                else:
                    _n_(7653, "prev", lambda: prev).next = _a_(7655, _n_(7654, "current", lambda: current), "next")
                    _l_(7656)
                _n_(7658, "self", lambda: self).count -= 1
                _l_(7659)
                aux = ""
                _l_(7660)
                return aux
            prev = _n_(7662, "current", lambda: current)
            _l_(7663)
            current = _a_(7665, _n_(7664, "current", lambda: current), "next")
            _l_(7666)

    def iterate_item(self):
        _l_(7682)

        current_item = _a_(7670, _n_(7669, "self", lambda: self), "tail")
        _l_(7671)
        while _n_(7672, "current_item", lambda: current_item):
            _l_(7681)

            val = _a_(7674, _n_(7673, "current_item", lambda: current_item), "data")
            _l_(7675)
            current_item = _a_(7677, _n_(7676, "current_item", lambda: current_item), "next")
            _l_(7678)
            yield _n_(7679, "val", lambda: val)
            _l_(7680)
items = _c_(7685, _n_(7684, "singly_linked_list", lambda: singly_linked_list))
_l_(7686)
_c_(7689, _a_(7688, _n_(7687, "items", lambda: items), "append_item"), 'PHP')
_l_(7690)
_c_(7693, _a_(7692, _n_(7691, "items", lambda: items), "append_item"), 'Python')
_l_(7694)
_c_(7697, _a_(7696, _n_(7695, "items", lambda: items), "append_item"), 'C#')
_l_(7698)
_c_(7701, _a_(7700, _n_(7699, "items", lambda: items), "append_item"), 'C++')
_l_(7702)
_c_(7705, _a_(7704, _n_(7703, "items", lambda: items), "append_item"), 'Java')
_l_(7706)
_c_(7708, _n_(7707, "print", lambda: print), 'Original list:')
_l_(7709)
for val in _c_(7712, _a_(7711, _n_(7710, "items", lambda: items), "iterate_item")):
    _l_(7717)

    _c_(7715, _n_(7713, "print", lambda: print), _n_(7714, "val", lambda: val))
    _l_(7716)
_c_(7719, _n_(7718, "print", lambda: print), '\nAfter removing the first item from the list:')
_l_(7720)
_c_(7723, _a_(7722, _n_(7721, "items", lambda: items), "delete_item"), 'PHP')
_l_(7724)
for val in _c_(7727, _a_(7726, _n_(7725, "items", lambda: items), "iterate_item")):
    _l_(7732)

    _c_(7730, _n_(7728, "print", lambda: print), _n_(7729, "val", lambda: val))
    _l_(7731)