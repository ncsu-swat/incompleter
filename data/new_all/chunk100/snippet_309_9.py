# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node(_n_(29237, "object", lambda: object)):
    _l_(29248)


    def __init__(self, value=None, next=None, prev=None):
        _l_(29247)

        _n_(29238, "self", lambda: self).value = _n_(29239, "value", lambda: value)
        _l_(29240)
        _n_(29241, "self", lambda: self).next = _n_(29242, "next", lambda: next)
        _l_(29243)
        _n_(29244, "self", lambda: self).prev = _n_(29245, "prev", lambda: prev)
        _l_(29246)

class doubly_linked_list(_n_(29249, "object", lambda: object)):
    _l_(29375)


    def __init__(self):
        _l_(29256)

        _n_(29250, "self", lambda: self).head = None
        _l_(29251)
        _n_(29252, "self", lambda: self).tail = None
        _l_(29253)
        _n_(29254, "self", lambda: self).count = 0
        _l_(29255)

    def append_item(self, value):
        _l_(29284)

        new_item = _c_(29259, _n_(29257, "Node", lambda: Node), _n_(29258, "value", lambda: value), None, None)
        _l_(29260)
        if _a_(29262, _n_(29261, "self", lambda: self), "head") is None:
            _l_(29281)

            _n_(29263, "self", lambda: self).head = _n_(29264, "new_item", lambda: new_item)
            _l_(29265)
            _n_(29266, "self", lambda: self).tail = _a_(29268, _n_(29267, "self", lambda: self), "head")
            _l_(29269)
        else:
            _n_(29270, "new_item", lambda: new_item).prev = _a_(29272, _n_(29271, "self", lambda: self), "tail")
            _l_(29273)
            _a_(29275, _n_(29274, "self", lambda: self), "tail").next = _n_(29276, "new_item", lambda: new_item)
            _l_(29277)
            _n_(29278, "self", lambda: self).tail = _n_(29279, "new_item", lambda: new_item)
            _l_(29280)
        _n_(29282, "self", lambda: self).count += 1
        _l_(29283)

    def iter(self):
        _l_(29298)

        current = _a_(29286, _n_(29285, "self", lambda: self), "head")
        _l_(29287)
        while _n_(29288, "current", lambda: current):
            _l_(29297)

            item_val = _a_(29290, _n_(29289, "current", lambda: current), "value")
            _l_(29291)
            current = _a_(29293, _n_(29292, "current", lambda: current), "next")
            _l_(29294)
            yield _n_(29295, "item_val", lambda: item_val)
            _l_(29296)

    def print_foward(self):
        _l_(29307)

        for node in _c_(29301, _a_(29300, _n_(29299, "self", lambda: self), "iter")):
            _l_(29306)

            _c_(29304, _n_(29302, "print", lambda: print), _n_(29303, "node", lambda: node))
            _l_(29305)

    def search_item(self, val):
        _l_(29317)

        for node in _c_(29310, _a_(29309, _n_(29308, "self", lambda: self), "iter")):
            _l_(29315)

            if _n_(29311, "val", lambda: val) == _n_(29312, "node", lambda: node):
                _l_(29314)

                aux = True
                _l_(29313)
                return aux
        aux = False
        _l_(29316)
        return aux

    def delete(self, value):
        _l_(29374)

        current = _a_(29319, _n_(29318, "self", lambda: self), "head")
        _l_(29320)
        if _n_(29321, "current", lambda: current) is None:
            _l_(29369)

            node_deleted = False
            _l_(29322)
        elif _a_(29324, _n_(29323, "current", lambda: current), "value") == _n_(29325, "value", lambda: value):
            _l_(29368)

            _n_(29326, "self", lambda: self).head = _a_(29328, _n_(29327, "current", lambda: current), "next")
            _l_(29329)
            _a_(29331, _n_(29330, "self", lambda: self), "head").prev = None
            _l_(29332)
            node_deleted = True
            _l_(29333)
        elif _a_(29336, _a_(29335, _n_(29334, "self", lambda: self), "tail"), "value") == _n_(29337, "value", lambda: value):
            _l_(29367)

            _n_(29338, "self", lambda: self).tail = _a_(29341, _a_(29340, _n_(29339, "self", lambda: self), "tail"), "prev")
            _l_(29342)
            _a_(29344, _n_(29343, "self", lambda: self), "tail").next = None
            _l_(29345)
            node_deleted = True
            _l_(29346)
        else:
            while _n_(29347, "current", lambda: current):
                _l_(29366)

                if _a_(29349, _n_(29348, "current", lambda: current), "value") == _n_(29350, "value", lambda: value):
                    _l_(29362)

                    _a_(29352, _n_(29351, "current", lambda: current), "prev").next = _a_(29354, _n_(29353, "current", lambda: current), "next")
                    _l_(29355)
                    _a_(29357, _n_(29356, "current", lambda: current), "next").prev = _a_(29359, _n_(29358, "current", lambda: current), "prev")
                    _l_(29360)
                    node_deleted = True
                    _l_(29361)
                current = _a_(29364, _n_(29363, "current", lambda: current), "next")
                _l_(29365)
        if _n_(29370, "node_deleted", lambda: node_deleted):
            _l_(29373)

            _n_(29371, "self", lambda: self).count -= 1
            _l_(29372)
items = _c_(29377, _n_(29376, "doubly_linked_list", lambda: doubly_linked_list))
_l_(29378)
_c_(29381, _a_(29380, _n_(29379, "items", lambda: items), "append_item"), 'PHP')
_l_(29382)
_c_(29385, _a_(29384, _n_(29383, "items", lambda: items), "append_item"), 'Python')
_l_(29386)
_c_(29389, _a_(29388, _n_(29387, "items", lambda: items), "append_item"), 'C#')
_l_(29390)
_c_(29393, _a_(29392, _n_(29391, "items", lambda: items), "append_item"), 'C++')
_l_(29394)
_c_(29397, _a_(29396, _n_(29395, "items", lambda: items), "append_item"), 'Java')
_l_(29398)
_c_(29401, _a_(29400, _n_(29399, "items", lambda: items), "append_item"), 'SQL')
_l_(29402)
_c_(29404, _n_(29403, "print", lambda: print), 'Original list:')
_l_(29405)
_c_(29408, _a_(29407, _n_(29406, "items", lambda: items), "print_foward"))
_l_(29409)
_c_(29412, _a_(29411, _n_(29410, "items", lambda: items), "delete"), 'Java')
_l_(29413)
_c_(29416, _a_(29415, _n_(29414, "items", lambda: items), "delete"), 'Python')
_l_(29417)
_c_(29419, _n_(29418, "print", lambda: print), '\nList after deleting two items:')
_l_(29420)
_c_(29423, _a_(29422, _n_(29421, "items", lambda: items), "print_foward"))
_l_(29424)