# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node:
    _l_(88849)


    def __init__(self, data=None):
        _l_(88848)

        _n_(88843, "self", lambda: self).data = _n_(88844, "data", lambda: data)
        _l_(88845)
        _n_(88846, "self", lambda: self).next = None
        _l_(88847)

class singly_linked_list:
    _l_(88924)


    def __init__(self):
        _l_(88856)

        _n_(88850, "self", lambda: self).tail = None
        _l_(88851)
        _n_(88852, "self", lambda: self).head = None
        _l_(88853)
        _n_(88854, "self", lambda: self).count = 0
        _l_(88855)

    def append_item(self, data):
        _l_(88879)

        node = _c_(88859, _n_(88857, "Node", lambda: Node), _n_(88858, "data", lambda: data))
        _l_(88860)
        if _a_(88862, _n_(88861, "self", lambda: self), "head"):
            _l_(88876)

            _a_(88864, _n_(88863, "self", lambda: self), "head").next = _n_(88865, "node", lambda: node)
            _l_(88866)
            _n_(88867, "self", lambda: self).head = _n_(88868, "node", lambda: node)
            _l_(88869)
        else:
            _n_(88870, "self", lambda: self).tail = _n_(88871, "node", lambda: node)
            _l_(88872)
            _n_(88873, "self", lambda: self).head = _n_(88874, "node", lambda: node)
            _l_(88875)
        _n_(88877, "self", lambda: self).count += 1
        _l_(88878)

    def delete_item(self, data):
        _l_(88912)

        current = _a_(88881, _n_(88880, "self", lambda: self), "tail")
        _l_(88882)
        prev = _a_(88884, _n_(88883, "self", lambda: self), "tail")
        _l_(88885)
        while _n_(88886, "current", lambda: current):
            _l_(88911)

            if _a_(88888, _n_(88887, "current", lambda: current), "data") == _n_(88889, "data", lambda: data):
                _l_(88905)

                if _n_(88890, "current", lambda: current) == _a_(88892, _n_(88891, "self", lambda: self), "tail"):
                    _l_(88901)

                    _n_(88893, "self", lambda: self).tail = _a_(88895, _n_(88894, "current", lambda: current), "next")
                    _l_(88896)
                else:
                    _n_(88897, "prev", lambda: prev).next = _a_(88899, _n_(88898, "current", lambda: current), "next")
                    _l_(88900)
                _n_(88902, "self", lambda: self).count -= 1
                _l_(88903)
                aux = ""
                _l_(88904)
                return aux
            prev = _n_(88906, "current", lambda: current)
            _l_(88907)
            current = _a_(88909, _n_(88908, "current", lambda: current), "next")
            _l_(88910)

    def iterate_item(self):
        _l_(88923)

        current_item = _a_(88914, _n_(88913, "self", lambda: self), "tail")
        _l_(88915)
        while _n_(88916, "current_item", lambda: current_item):
            _l_(88922)

            val = _a_(88918, _n_(88917, "current_item", lambda: current_item), "data")
            _l_(88919)
            yield _n_(88920, "val", lambda: val)
            _l_(88921)
items = _c_(88926, _n_(88925, "singly_linked_list", lambda: singly_linked_list))
_l_(88927)
_c_(88930, _a_(88929, _n_(88928, "items", lambda: items), "append_item"), 'PHP')
_l_(88931)
_c_(88934, _a_(88933, _n_(88932, "items", lambda: items), "append_item"), 'Python')
_l_(88935)
_c_(88938, _a_(88937, _n_(88936, "items", lambda: items), "append_item"), 'C#')
_l_(88939)
_c_(88942, _a_(88941, _n_(88940, "items", lambda: items), "append_item"), 'C++')
_l_(88943)
_c_(88946, _a_(88945, _n_(88944, "items", lambda: items), "append_item"), 'Java')
_l_(88947)
_c_(88949, _n_(88948, "print", lambda: print), 'Original list:')
_l_(88950)
for val in _c_(88953, _a_(88952, _n_(88951, "items", lambda: items), "iterate_item")):
    _l_(88958)

    _c_(88956, _n_(88954, "print", lambda: print), _n_(88955, "val", lambda: val))
    _l_(88957)
_c_(88960, _n_(88959, "print", lambda: print), '\nAfter removing the last item from the list:')
_l_(88961)
_c_(88964, _a_(88963, _n_(88962, "items", lambda: items), "delete_item"), 'Java')
_l_(88965)
for val in _c_(88968, _a_(88967, _n_(88966, "items", lambda: items), "iterate_item")):
    _l_(88973)

    _c_(88971, _n_(88969, "print", lambda: print), _n_(88970, "val", lambda: val))
    _l_(88972)