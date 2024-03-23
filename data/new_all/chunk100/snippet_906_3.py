# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node:
    _l_(90158)


    def __init__(self, data=None):
        _l_(90157)

        _n_(90152, "self", lambda: self).data = _n_(90153, "data", lambda: data)
        _l_(90154)
        _n_(90155, "self", lambda: self).next = None
        _l_(90156)

class singly_linked_list:
    _l_(90233)


    def __init__(self):
        _l_(90165)

        _n_(90159, "self", lambda: self).tail = None
        _l_(90160)
        _n_(90161, "self", lambda: self).head = None
        _l_(90162)
        _n_(90163, "self", lambda: self).count = 0
        _l_(90164)

    def append_item(self, data):
        _l_(90188)

        node = _c_(90168, _n_(90166, "Node", lambda: Node), _n_(90167, "data", lambda: data))
        _l_(90169)
        if _a_(90171, _n_(90170, "self", lambda: self), "head"):
            _l_(90185)

            _a_(90173, _n_(90172, "self", lambda: self), "head").next = _n_(90174, "node", lambda: node)
            _l_(90175)
            _n_(90176, "self", lambda: self).head = _n_(90177, "node", lambda: node)
            _l_(90178)
        else:
            _n_(90179, "self", lambda: self).tail = _n_(90180, "node", lambda: node)
            _l_(90181)
            _n_(90182, "self", lambda: self).head = _n_(90183, "node", lambda: node)
            _l_(90184)
        _n_(90186, "self", lambda: self).count += 1
        _l_(90187)

    def delete_item(self, data):
        _l_(90218)

        current = _a_(90190, _n_(90189, "self", lambda: self), "tail")
        _l_(90191)
        while _n_(90192, "current", lambda: current):
            _l_(90217)

            if _a_(90194, _n_(90193, "current", lambda: current), "data") == _n_(90195, "data", lambda: data):
                _l_(90211)

                if _n_(90196, "current", lambda: current) == _a_(90198, _n_(90197, "self", lambda: self), "tail"):
                    _l_(90207)

                    _n_(90199, "self", lambda: self).tail = _a_(90201, _n_(90200, "current", lambda: current), "next")
                    _l_(90202)
                else:
                    _n_(90203, "prev", lambda: prev).next = _a_(90205, _n_(90204, "current", lambda: current), "next")
                    _l_(90206)
                _n_(90208, "self", lambda: self).count -= 1
                _l_(90209)
                aux = ""
                _l_(90210)
                return aux
            prev = _n_(90212, "current", lambda: current)
            _l_(90213)
            current = _a_(90215, _n_(90214, "current", lambda: current), "next")
            _l_(90216)

    def iterate_item(self):
        _l_(90232)

        current_item = _a_(90220, _n_(90219, "self", lambda: self), "tail")
        _l_(90221)
        while _n_(90222, "current_item", lambda: current_item):
            _l_(90231)

            val = _a_(90224, _n_(90223, "current_item", lambda: current_item), "data")
            _l_(90225)
            current_item = _a_(90227, _n_(90226, "current_item", lambda: current_item), "next")
            _l_(90228)
            yield _n_(90229, "val", lambda: val)
            _l_(90230)
items = _c_(90235, _n_(90234, "singly_linked_list", lambda: singly_linked_list))
_l_(90236)
_c_(90239, _a_(90238, _n_(90237, "items", lambda: items), "append_item"), 'PHP')
_l_(90240)
_c_(90243, _a_(90242, _n_(90241, "items", lambda: items), "append_item"), 'Python')
_l_(90244)
_c_(90247, _a_(90246, _n_(90245, "items", lambda: items), "append_item"), 'C#')
_l_(90248)
_c_(90251, _a_(90250, _n_(90249, "items", lambda: items), "append_item"), 'C++')
_l_(90252)
_c_(90255, _a_(90254, _n_(90253, "items", lambda: items), "append_item"), 'Java')
_l_(90256)
_c_(90258, _n_(90257, "print", lambda: print), 'Original list:')
_l_(90259)
for val in _c_(90262, _a_(90261, _n_(90260, "items", lambda: items), "iterate_item")):
    _l_(90267)

    _c_(90265, _n_(90263, "print", lambda: print), _n_(90264, "val", lambda: val))
    _l_(90266)
_c_(90269, _n_(90268, "print", lambda: print), '\nAfter removing the last item from the list:')
_l_(90270)
_c_(90273, _a_(90272, _n_(90271, "items", lambda: items), "delete_item"), 'Java')
_l_(90274)
for val in _c_(90277, _a_(90276, _n_(90275, "items", lambda: items), "iterate_item")):
    _l_(90282)

    _c_(90280, _n_(90278, "print", lambda: print), _n_(90279, "val", lambda: val))
    _l_(90281)