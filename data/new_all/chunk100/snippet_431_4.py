# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node(_n_(43206, "object", lambda: object)):
    _l_(43217)


    def __init__(self, data=None, next=None, prev=None):
        _l_(43216)

        _n_(43207, "self", lambda: self).data = _n_(43208, "data", lambda: data)
        _l_(43209)
        _n_(43210, "self", lambda: self).next = _n_(43211, "next", lambda: next)
        _l_(43212)
        _n_(43213, "self", lambda: self).prev = _n_(43214, "prev", lambda: prev)
        _l_(43215)

class doubly_linked_list(_n_(43218, "object", lambda: object)):
    _l_(43284)


    def __init__(self):
        _l_(43225)

        _n_(43219, "self", lambda: self).head = None
        _l_(43220)
        _n_(43221, "self", lambda: self).tail = None
        _l_(43222)
        _n_(43223, "self", lambda: self).count = 0
        _l_(43224)

    def append_item(self, data):
        _l_(43250)

        new_item = _c_(43228, _n_(43226, "Node", lambda: Node), _n_(43227, "data", lambda: data), None, None)
        _l_(43229)
        if _a_(43231, _n_(43230, "self", lambda: self), "head") is None:
            _l_(43247)

            _n_(43232, "self", lambda: self).tail = _a_(43234, _n_(43233, "self", lambda: self), "head")
            _l_(43235)
        else:
            _n_(43236, "new_item", lambda: new_item).prev = _a_(43238, _n_(43237, "self", lambda: self), "tail")
            _l_(43239)
            _a_(43241, _n_(43240, "self", lambda: self), "tail").next = _n_(43242, "new_item", lambda: new_item)
            _l_(43243)
            _n_(43244, "self", lambda: self).tail = _n_(43245, "new_item", lambda: new_item)
            _l_(43246)
        _n_(43248, "self", lambda: self).count += 1
        _l_(43249)

    def iter(self):
        _l_(43264)

        current = _a_(43252, _n_(43251, "self", lambda: self), "head")
        _l_(43253)
        while _n_(43254, "current", lambda: current):
            _l_(43263)

            item_val = _a_(43256, _n_(43255, "current", lambda: current), "data")
            _l_(43257)
            current = _a_(43259, _n_(43258, "current", lambda: current), "next")
            _l_(43260)
            yield _n_(43261, "item_val", lambda: item_val)
            _l_(43262)

    def print_foward(self):
        _l_(43273)

        for node in _c_(43267, _a_(43266, _n_(43265, "self", lambda: self), "iter")):
            _l_(43272)

            _c_(43270, _n_(43268, "print", lambda: print), _n_(43269, "node", lambda: node))
            _l_(43271)

    def search_item(self, val):
        _l_(43283)

        for node in _c_(43276, _a_(43275, _n_(43274, "self", lambda: self), "iter")):
            _l_(43281)

            if _n_(43277, "val", lambda: val) == _n_(43278, "node", lambda: node):
                _l_(43280)

                aux = True
                _l_(43279)
                return aux
        aux = False
        _l_(43282)
        return aux
items = _c_(43286, _n_(43285, "doubly_linked_list", lambda: doubly_linked_list))
_l_(43287)
_c_(43290, _a_(43289, _n_(43288, "items", lambda: items), "append_item"), 'PHP')
_l_(43291)
_c_(43294, _a_(43293, _n_(43292, "items", lambda: items), "append_item"), 'Python')
_l_(43295)
_c_(43298, _a_(43297, _n_(43296, "items", lambda: items), "append_item"), 'C#')
_l_(43299)
_c_(43302, _a_(43301, _n_(43300, "items", lambda: items), "append_item"), 'C++')
_l_(43303)
_c_(43306, _a_(43305, _n_(43304, "items", lambda: items), "append_item"), 'Java')
_l_(43307)
_c_(43310, _a_(43309, _n_(43308, "items", lambda: items), "append_item"), 'SQL')
_l_(43311)
_c_(43313, _n_(43312, "print", lambda: print), 'Original list:')
_l_(43314)
_c_(43317, _a_(43316, _n_(43315, "items", lambda: items), "print_foward"))
_l_(43318)
_c_(43320, _n_(43319, "print", lambda: print), '\n')
_l_(43321)
if _c_(43324, _a_(43323, _n_(43322, "items", lambda: items), "search_item"), 'SQL'):
    _l_(43331)

    _c_(43326, _n_(43325, "print", lambda: print), 'True')
    _l_(43327)
else:
    _c_(43329, _n_(43328, "print", lambda: print), 'False')
    _l_(43330)
if _c_(43334, _a_(43333, _n_(43332, "items", lambda: items), "search_item"), 'C+'):
    _l_(43341)

    _c_(43336, _n_(43335, "print", lambda: print), 'True')
    _l_(43337)
else:
    _c_(43339, _n_(43338, "print", lambda: print), 'False')
    _l_(43340)