# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node:
    _l_(89635)


    def __init__(self, data=None):
        _l_(89634)

        _n_(89629, "self", lambda: self).data = _n_(89630, "data", lambda: data)
        _l_(89631)
        _n_(89632, "self", lambda: self).next = None
        _l_(89633)

class singly_linked_list:
    _l_(89709)


    def __init__(self):
        _l_(89642)

        _n_(89636, "self", lambda: self).tail = None
        _l_(89637)
        _n_(89638, "self", lambda: self).head = None
        _l_(89639)
        _n_(89640, "self", lambda: self).count = 0
        _l_(89641)

    def append_item(self, data):
        _l_(89661)

        node = _c_(89645, _n_(89643, "Node", lambda: Node), _n_(89644, "data", lambda: data))
        _l_(89646)
        if _a_(89648, _n_(89647, "self", lambda: self), "head"):
            _l_(89658)

            _n_(89649, "self", lambda: self).head = _n_(89650, "node", lambda: node)
            _l_(89651)
        else:
            _n_(89652, "self", lambda: self).tail = _n_(89653, "node", lambda: node)
            _l_(89654)
            _n_(89655, "self", lambda: self).head = _n_(89656, "node", lambda: node)
            _l_(89657)
        _n_(89659, "self", lambda: self).count += 1
        _l_(89660)

    def delete_item(self, data):
        _l_(89694)

        current = _a_(89663, _n_(89662, "self", lambda: self), "tail")
        _l_(89664)
        prev = _a_(89666, _n_(89665, "self", lambda: self), "tail")
        _l_(89667)
        while _n_(89668, "current", lambda: current):
            _l_(89693)

            if _a_(89670, _n_(89669, "current", lambda: current), "data") == _n_(89671, "data", lambda: data):
                _l_(89687)

                if _n_(89672, "current", lambda: current) == _a_(89674, _n_(89673, "self", lambda: self), "tail"):
                    _l_(89683)

                    _n_(89675, "self", lambda: self).tail = _a_(89677, _n_(89676, "current", lambda: current), "next")
                    _l_(89678)
                else:
                    _n_(89679, "prev", lambda: prev).next = _a_(89681, _n_(89680, "current", lambda: current), "next")
                    _l_(89682)
                _n_(89684, "self", lambda: self).count -= 1
                _l_(89685)
                aux = ""
                _l_(89686)
                return aux
            prev = _n_(89688, "current", lambda: current)
            _l_(89689)
            current = _a_(89691, _n_(89690, "current", lambda: current), "next")
            _l_(89692)

    def iterate_item(self):
        _l_(89708)

        current_item = _a_(89696, _n_(89695, "self", lambda: self), "tail")
        _l_(89697)
        while _n_(89698, "current_item", lambda: current_item):
            _l_(89707)

            val = _a_(89700, _n_(89699, "current_item", lambda: current_item), "data")
            _l_(89701)
            current_item = _a_(89703, _n_(89702, "current_item", lambda: current_item), "next")
            _l_(89704)
            yield _n_(89705, "val", lambda: val)
            _l_(89706)
items = _c_(89711, _n_(89710, "singly_linked_list", lambda: singly_linked_list))
_l_(89712)
_c_(89715, _a_(89714, _n_(89713, "items", lambda: items), "append_item"), 'PHP')
_l_(89716)
_c_(89719, _a_(89718, _n_(89717, "items", lambda: items), "append_item"), 'Python')
_l_(89720)
_c_(89723, _a_(89722, _n_(89721, "items", lambda: items), "append_item"), 'C#')
_l_(89724)
_c_(89727, _a_(89726, _n_(89725, "items", lambda: items), "append_item"), 'C++')
_l_(89728)
_c_(89731, _a_(89730, _n_(89729, "items", lambda: items), "append_item"), 'Java')
_l_(89732)
_c_(89734, _n_(89733, "print", lambda: print), 'Original list:')
_l_(89735)
for val in _c_(89738, _a_(89737, _n_(89736, "items", lambda: items), "iterate_item")):
    _l_(89743)

    _c_(89741, _n_(89739, "print", lambda: print), _n_(89740, "val", lambda: val))
    _l_(89742)
_c_(89745, _n_(89744, "print", lambda: print), '\nAfter removing the last item from the list:')
_l_(89746)
_c_(89749, _a_(89748, _n_(89747, "items", lambda: items), "delete_item"), 'Java')
_l_(89750)
for val in _c_(89753, _a_(89752, _n_(89751, "items", lambda: items), "iterate_item")):
    _l_(89758)

    _c_(89756, _n_(89754, "print", lambda: print), _n_(89755, "val", lambda: val))
    _l_(89757)