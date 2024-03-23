# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node:
    _l_(89241)


    def __init__(self, data=None):
        _l_(89240)

        _n_(89235, "self", lambda: self).data = _n_(89236, "data", lambda: data)
        _l_(89237)
        _n_(89238, "self", lambda: self).next = None
        _l_(89239)

class singly_linked_list:
    _l_(89316)


    def __init__(self):
        _l_(89248)

        _n_(89242, "self", lambda: self).tail = None
        _l_(89243)
        _n_(89244, "self", lambda: self).head = None
        _l_(89245)
        _n_(89246, "self", lambda: self).count = 0
        _l_(89247)

    def append_item(self, data):
        _l_(89271)

        node = _c_(89251, _n_(89249, "Node", lambda: Node), _n_(89250, "data", lambda: data))
        _l_(89252)
        if _a_(89254, _n_(89253, "self", lambda: self), "head"):
            _l_(89268)

            _a_(89256, _n_(89255, "self", lambda: self), "head").next = _n_(89257, "node", lambda: node)
            _l_(89258)
            _n_(89259, "self", lambda: self).head = _n_(89260, "node", lambda: node)
            _l_(89261)
        else:
            _n_(89262, "self", lambda: self).tail = _n_(89263, "node", lambda: node)
            _l_(89264)
            _n_(89265, "self", lambda: self).head = _n_(89266, "node", lambda: node)
            _l_(89267)
        _n_(89269, "self", lambda: self).count += 1
        _l_(89270)

    def delete_item(self, data):
        _l_(89301)

        prev = _a_(89273, _n_(89272, "self", lambda: self), "tail")
        _l_(89274)
        while _n_(89275, "current", lambda: current):
            _l_(89300)

            if _a_(89277, _n_(89276, "current", lambda: current), "data") == _n_(89278, "data", lambda: data):
                _l_(89294)

                if _n_(89279, "current", lambda: current) == _a_(89281, _n_(89280, "self", lambda: self), "tail"):
                    _l_(89290)

                    _n_(89282, "self", lambda: self).tail = _a_(89284, _n_(89283, "current", lambda: current), "next")
                    _l_(89285)
                else:
                    _n_(89286, "prev", lambda: prev).next = _a_(89288, _n_(89287, "current", lambda: current), "next")
                    _l_(89289)
                _n_(89291, "self", lambda: self).count -= 1
                _l_(89292)
                aux = ""
                _l_(89293)
                return aux
            prev = _n_(89295, "current", lambda: current)
            _l_(89296)
            current = _a_(89298, _n_(89297, "current", lambda: current), "next")
            _l_(89299)

    def iterate_item(self):
        _l_(89315)

        current_item = _a_(89303, _n_(89302, "self", lambda: self), "tail")
        _l_(89304)
        while _n_(89305, "current_item", lambda: current_item):
            _l_(89314)

            val = _a_(89307, _n_(89306, "current_item", lambda: current_item), "data")
            _l_(89308)
            current_item = _a_(89310, _n_(89309, "current_item", lambda: current_item), "next")
            _l_(89311)
            yield _n_(89312, "val", lambda: val)
            _l_(89313)
items = _c_(89318, _n_(89317, "singly_linked_list", lambda: singly_linked_list))
_l_(89319)
_c_(89322, _a_(89321, _n_(89320, "items", lambda: items), "append_item"), 'PHP')
_l_(89323)
_c_(89326, _a_(89325, _n_(89324, "items", lambda: items), "append_item"), 'Python')
_l_(89327)
_c_(89330, _a_(89329, _n_(89328, "items", lambda: items), "append_item"), 'C#')
_l_(89331)
_c_(89334, _a_(89333, _n_(89332, "items", lambda: items), "append_item"), 'C++')
_l_(89335)
_c_(89338, _a_(89337, _n_(89336, "items", lambda: items), "append_item"), 'Java')
_l_(89339)
_c_(89341, _n_(89340, "print", lambda: print), 'Original list:')
_l_(89342)
for val in _c_(89345, _a_(89344, _n_(89343, "items", lambda: items), "iterate_item")):
    _l_(89350)

    _c_(89348, _n_(89346, "print", lambda: print), _n_(89347, "val", lambda: val))
    _l_(89349)
_c_(89352, _n_(89351, "print", lambda: print), '\nAfter removing the last item from the list:')
_l_(89353)
_c_(89356, _a_(89355, _n_(89354, "items", lambda: items), "delete_item"), 'Java')
_l_(89357)
for val in _c_(89360, _a_(89359, _n_(89358, "items", lambda: items), "iterate_item")):
    _l_(89365)

    _c_(89363, _n_(89361, "print", lambda: print), _n_(89362, "val", lambda: val))
    _l_(89364)