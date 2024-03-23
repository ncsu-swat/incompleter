# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node(_n_(27191, "object", lambda: object)):
    _l_(27202)


    def __init__(self, value=None, next=None, prev=None):
        _l_(27201)

        _n_(27192, "self", lambda: self).value = _n_(27193, "value", lambda: value)
        _l_(27194)
        _n_(27195, "self", lambda: self).next = _n_(27196, "next", lambda: next)
        _l_(27197)
        _n_(27198, "self", lambda: self).prev = _n_(27199, "prev", lambda: prev)
        _l_(27200)

class doubly_linked_list(_n_(27203, "object", lambda: object)):
    _l_(27327)


    def __init__(self):
        _l_(27210)

        _n_(27204, "self", lambda: self).head = None
        _l_(27205)
        _n_(27206, "self", lambda: self).tail = None
        _l_(27207)
        _n_(27208, "self", lambda: self).count = 0
        _l_(27209)

    def append_item(self, value):
        _l_(27238)

        new_item = _c_(27213, _n_(27211, "Node", lambda: Node), _n_(27212, "value", lambda: value), None, None)
        _l_(27214)
        if _a_(27216, _n_(27215, "self", lambda: self), "head") is None:
            _l_(27235)

            _n_(27217, "self", lambda: self).head = _n_(27218, "new_item", lambda: new_item)
            _l_(27219)
            _n_(27220, "self", lambda: self).tail = _a_(27222, _n_(27221, "self", lambda: self), "head")
            _l_(27223)
        else:
            _n_(27224, "new_item", lambda: new_item).prev = _a_(27226, _n_(27225, "self", lambda: self), "tail")
            _l_(27227)
            _a_(27229, _n_(27228, "self", lambda: self), "tail").next = _n_(27230, "new_item", lambda: new_item)
            _l_(27231)
            _n_(27232, "self", lambda: self).tail = _n_(27233, "new_item", lambda: new_item)
            _l_(27234)
        _n_(27236, "self", lambda: self).count += 1
        _l_(27237)

    def iter(self):
        _l_(27252)

        current = _a_(27240, _n_(27239, "self", lambda: self), "head")
        _l_(27241)
        while _n_(27242, "current", lambda: current):
            _l_(27251)

            item_val = _a_(27244, _n_(27243, "current", lambda: current), "value")
            _l_(27245)
            current = _a_(27247, _n_(27246, "current", lambda: current), "next")
            _l_(27248)
            yield _n_(27249, "item_val", lambda: item_val)
            _l_(27250)

    def print_foward(self):
        _l_(27261)

        for node in _c_(27255, _a_(27254, _n_(27253, "self", lambda: self), "iter")):
            _l_(27260)

            _c_(27258, _n_(27256, "print", lambda: print), _n_(27257, "node", lambda: node))
            _l_(27259)

    def search_item(self, val):
        _l_(27271)

        for node in _c_(27264, _a_(27263, _n_(27262, "self", lambda: self), "iter")):
            _l_(27269)

            if _n_(27265, "val", lambda: val) == _n_(27266, "node", lambda: node):
                _l_(27268)

                aux = True
                _l_(27267)
                return aux
        aux = False
        _l_(27270)
        return aux

    def delete(self, value):
        _l_(27326)

        node_deleted = False
        _l_(27272)
        if _n_(27273, "current", lambda: current) is None:
            _l_(27321)

            node_deleted = False
            _l_(27274)
        elif _a_(27276, _n_(27275, "current", lambda: current), "value") == _n_(27277, "value", lambda: value):
            _l_(27320)

            _n_(27278, "self", lambda: self).head = _a_(27280, _n_(27279, "current", lambda: current), "next")
            _l_(27281)
            _a_(27283, _n_(27282, "self", lambda: self), "head").prev = None
            _l_(27284)
            node_deleted = True
            _l_(27285)
        elif _a_(27288, _a_(27287, _n_(27286, "self", lambda: self), "tail"), "value") == _n_(27289, "value", lambda: value):
            _l_(27319)

            _n_(27290, "self", lambda: self).tail = _a_(27293, _a_(27292, _n_(27291, "self", lambda: self), "tail"), "prev")
            _l_(27294)
            _a_(27296, _n_(27295, "self", lambda: self), "tail").next = None
            _l_(27297)
            node_deleted = True
            _l_(27298)
        else:
            while _n_(27299, "current", lambda: current):
                _l_(27318)

                if _a_(27301, _n_(27300, "current", lambda: current), "value") == _n_(27302, "value", lambda: value):
                    _l_(27314)

                    _a_(27304, _n_(27303, "current", lambda: current), "prev").next = _a_(27306, _n_(27305, "current", lambda: current), "next")
                    _l_(27307)
                    _a_(27309, _n_(27308, "current", lambda: current), "next").prev = _a_(27311, _n_(27310, "current", lambda: current), "prev")
                    _l_(27312)
                    node_deleted = True
                    _l_(27313)
                current = _a_(27316, _n_(27315, "current", lambda: current), "next")
                _l_(27317)
        if _n_(27322, "node_deleted", lambda: node_deleted):
            _l_(27325)

            _n_(27323, "self", lambda: self).count -= 1
            _l_(27324)
items = _c_(27329, _n_(27328, "doubly_linked_list", lambda: doubly_linked_list))
_l_(27330)
_c_(27333, _a_(27332, _n_(27331, "items", lambda: items), "append_item"), 'PHP')
_l_(27334)
_c_(27337, _a_(27336, _n_(27335, "items", lambda: items), "append_item"), 'Python')
_l_(27338)
_c_(27341, _a_(27340, _n_(27339, "items", lambda: items), "append_item"), 'C#')
_l_(27342)
_c_(27345, _a_(27344, _n_(27343, "items", lambda: items), "append_item"), 'C++')
_l_(27346)
_c_(27349, _a_(27348, _n_(27347, "items", lambda: items), "append_item"), 'Java')
_l_(27350)
_c_(27353, _a_(27352, _n_(27351, "items", lambda: items), "append_item"), 'SQL')
_l_(27354)
_c_(27356, _n_(27355, "print", lambda: print), 'Original list:')
_l_(27357)
_c_(27360, _a_(27359, _n_(27358, "items", lambda: items), "print_foward"))
_l_(27361)
_c_(27364, _a_(27363, _n_(27362, "items", lambda: items), "delete"), 'Java')
_l_(27365)
_c_(27368, _a_(27367, _n_(27366, "items", lambda: items), "delete"), 'Python')
_l_(27369)
_c_(27371, _n_(27370, "print", lambda: print), '\nList after deleting two items:')
_l_(27372)
_c_(27375, _a_(27374, _n_(27373, "items", lambda: items), "print_foward"))
_l_(27376)