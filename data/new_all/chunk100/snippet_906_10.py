# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node:
    _l_(89110)


    def __init__(self, data=None):
        _l_(89109)

        _n_(89104, "self", lambda: self).data = _n_(89105, "data", lambda: data)
        _l_(89106)
        _n_(89107, "self", lambda: self).next = None
        _l_(89108)

class singly_linked_list:
    _l_(89188)


    def __init__(self):
        _l_(89117)

        _n_(89111, "self", lambda: self).tail = None
        _l_(89112)
        _n_(89113, "self", lambda: self).head = None
        _l_(89114)
        _n_(89115, "self", lambda: self).count = 0
        _l_(89116)

    def append_item(self, data):
        _l_(89140)

        node = _c_(89120, _n_(89118, "Node", lambda: Node), _n_(89119, "data", lambda: data))
        _l_(89121)
        if _a_(89123, _n_(89122, "self", lambda: self), "head"):
            _l_(89137)

            _a_(89125, _n_(89124, "self", lambda: self), "head").next = _n_(89126, "node", lambda: node)
            _l_(89127)
            _n_(89128, "self", lambda: self).head = _n_(89129, "node", lambda: node)
            _l_(89130)
        else:
            _n_(89131, "self", lambda: self).tail = _n_(89132, "node", lambda: node)
            _l_(89133)
            _n_(89134, "self", lambda: self).head = _n_(89135, "node", lambda: node)
            _l_(89136)
        _n_(89138, "self", lambda: self).count += 1
        _l_(89139)

    def delete_item(self, data):
        _l_(89173)

        current = _a_(89142, _n_(89141, "self", lambda: self), "tail")
        _l_(89143)
        prev = _a_(89145, _n_(89144, "self", lambda: self), "tail")
        _l_(89146)
        while _n_(89147, "current", lambda: current):
            _l_(89172)

            if _a_(89149, _n_(89148, "current", lambda: current), "data") == _n_(89150, "data", lambda: data):
                _l_(89166)

                if _n_(89151, "current", lambda: current) == _a_(89153, _n_(89152, "self", lambda: self), "tail"):
                    _l_(89162)

                    _n_(89154, "self", lambda: self).tail = _a_(89156, _n_(89155, "current", lambda: current), "next")
                    _l_(89157)
                else:
                    _n_(89158, "prev", lambda: prev).next = _a_(89160, _n_(89159, "current", lambda: current), "next")
                    _l_(89161)
                _n_(89163, "self", lambda: self).count -= 1
                _l_(89164)
                aux = ""
                _l_(89165)
                return aux
            prev = _n_(89167, "current", lambda: current)
            _l_(89168)
            current = _a_(89170, _n_(89169, "current", lambda: current), "next")
            _l_(89171)

    def iterate_item(self):
        _l_(89187)

        current_item = _a_(89175, _n_(89174, "self", lambda: self), "tail")
        _l_(89176)
        while _n_(89177, "current_item", lambda: current_item):
            _l_(89186)

            val = _a_(89179, _n_(89178, "current_item", lambda: current_item), "data")
            _l_(89180)
            current_item = _a_(89182, _n_(89181, "current_item", lambda: current_item), "next")
            _l_(89183)
            yield _n_(89184, "val", lambda: val)
            _l_(89185)
_c_(89191, _a_(89190, _n_(89189, "items", lambda: items), "append_item"), 'PHP')
_l_(89192)
_c_(89195, _a_(89194, _n_(89193, "items", lambda: items), "append_item"), 'Python')
_l_(89196)
_c_(89199, _a_(89198, _n_(89197, "items", lambda: items), "append_item"), 'C#')
_l_(89200)
_c_(89203, _a_(89202, _n_(89201, "items", lambda: items), "append_item"), 'C++')
_l_(89204)
_c_(89207, _a_(89206, _n_(89205, "items", lambda: items), "append_item"), 'Java')
_l_(89208)
_c_(89210, _n_(89209, "print", lambda: print), 'Original list:')
_l_(89211)
for val in _c_(89214, _a_(89213, _n_(89212, "items", lambda: items), "iterate_item")):
    _l_(89219)

    _c_(89217, _n_(89215, "print", lambda: print), _n_(89216, "val", lambda: val))
    _l_(89218)
_c_(89221, _n_(89220, "print", lambda: print), '\nAfter removing the last item from the list:')
_l_(89222)
_c_(89225, _a_(89224, _n_(89223, "items", lambda: items), "delete_item"), 'Java')
_l_(89226)
for val in _c_(89229, _a_(89228, _n_(89227, "items", lambda: items), "iterate_item")):
    _l_(89234)

    _c_(89232, _n_(89230, "print", lambda: print), _n_(89231, "val", lambda: val))
    _l_(89233)