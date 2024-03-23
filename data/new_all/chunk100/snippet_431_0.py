# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node(_n_(42117, "object", lambda: object)):
    _l_(42128)


    def __init__(self, data=None, next=None, prev=None):
        _l_(42127)

        _n_(42118, "self", lambda: self).data = _n_(42119, "data", lambda: data)
        _l_(42120)
        _n_(42121, "self", lambda: self).next = _n_(42122, "next", lambda: next)
        _l_(42123)
        _n_(42124, "self", lambda: self).prev = _n_(42125, "prev", lambda: prev)
        _l_(42126)

class doubly_linked_list(_n_(42129, "object", lambda: object)):
    _l_(42196)


    def __init__(self):
        _l_(42134)

        _n_(42130, "self", lambda: self).head = None
        _l_(42131)
        _n_(42132, "self", lambda: self).tail = None
        _l_(42133)

    def append_item(self, data):
        _l_(42162)

        new_item = _c_(42137, _n_(42135, "Node", lambda: Node), _n_(42136, "data", lambda: data), None, None)
        _l_(42138)
        if _a_(42140, _n_(42139, "self", lambda: self), "head") is None:
            _l_(42159)

            _n_(42141, "self", lambda: self).head = _n_(42142, "new_item", lambda: new_item)
            _l_(42143)
            _n_(42144, "self", lambda: self).tail = _a_(42146, _n_(42145, "self", lambda: self), "head")
            _l_(42147)
        else:
            _n_(42148, "new_item", lambda: new_item).prev = _a_(42150, _n_(42149, "self", lambda: self), "tail")
            _l_(42151)
            _a_(42153, _n_(42152, "self", lambda: self), "tail").next = _n_(42154, "new_item", lambda: new_item)
            _l_(42155)
            _n_(42156, "self", lambda: self).tail = _n_(42157, "new_item", lambda: new_item)
            _l_(42158)
        _n_(42160, "self", lambda: self).count += 1
        _l_(42161)

    def iter(self):
        _l_(42176)

        current = _a_(42164, _n_(42163, "self", lambda: self), "head")
        _l_(42165)
        while _n_(42166, "current", lambda: current):
            _l_(42175)

            item_val = _a_(42168, _n_(42167, "current", lambda: current), "data")
            _l_(42169)
            current = _a_(42171, _n_(42170, "current", lambda: current), "next")
            _l_(42172)
            yield _n_(42173, "item_val", lambda: item_val)
            _l_(42174)

    def print_foward(self):
        _l_(42185)

        for node in _c_(42179, _a_(42178, _n_(42177, "self", lambda: self), "iter")):
            _l_(42184)

            _c_(42182, _n_(42180, "print", lambda: print), _n_(42181, "node", lambda: node))
            _l_(42183)

    def search_item(self, val):
        _l_(42195)

        for node in _c_(42188, _a_(42187, _n_(42186, "self", lambda: self), "iter")):
            _l_(42193)

            if _n_(42189, "val", lambda: val) == _n_(42190, "node", lambda: node):
                _l_(42192)

                aux = True
                _l_(42191)
                return aux
        aux = False
        _l_(42194)
        return aux
items = _c_(42198, _n_(42197, "doubly_linked_list", lambda: doubly_linked_list))
_l_(42199)
_c_(42202, _a_(42201, _n_(42200, "items", lambda: items), "append_item"), 'PHP')
_l_(42203)
_c_(42206, _a_(42205, _n_(42204, "items", lambda: items), "append_item"), 'Python')
_l_(42207)
_c_(42210, _a_(42209, _n_(42208, "items", lambda: items), "append_item"), 'C#')
_l_(42211)
_c_(42214, _a_(42213, _n_(42212, "items", lambda: items), "append_item"), 'C++')
_l_(42215)
_c_(42218, _a_(42217, _n_(42216, "items", lambda: items), "append_item"), 'Java')
_l_(42219)
_c_(42222, _a_(42221, _n_(42220, "items", lambda: items), "append_item"), 'SQL')
_l_(42223)
_c_(42225, _n_(42224, "print", lambda: print), 'Original list:')
_l_(42226)
_c_(42229, _a_(42228, _n_(42227, "items", lambda: items), "print_foward"))
_l_(42230)
_c_(42232, _n_(42231, "print", lambda: print), '\n')
_l_(42233)
if _c_(42236, _a_(42235, _n_(42234, "items", lambda: items), "search_item"), 'SQL'):
    _l_(42243)

    _c_(42238, _n_(42237, "print", lambda: print), 'True')
    _l_(42239)
else:
    _c_(42241, _n_(42240, "print", lambda: print), 'False')
    _l_(42242)
if _c_(42246, _a_(42245, _n_(42244, "items", lambda: items), "search_item"), 'C+'):
    _l_(42253)

    _c_(42248, _n_(42247, "print", lambda: print), 'True')
    _l_(42249)
else:
    _c_(42251, _n_(42250, "print", lambda: print), 'False')
    _l_(42252)