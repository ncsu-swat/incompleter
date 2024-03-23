# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node(_n_(28307, "object", lambda: object)):
    _l_(28318)


    def __init__(self, value=None, next=None, prev=None):
        _l_(28317)

        _n_(28308, "self", lambda: self).value = _n_(28309, "value", lambda: value)
        _l_(28310)
        _n_(28311, "self", lambda: self).next = _n_(28312, "next", lambda: next)
        _l_(28313)
        _n_(28314, "self", lambda: self).prev = _n_(28315, "prev", lambda: prev)
        _l_(28316)

class doubly_linked_list(_n_(28319, "object", lambda: object)):
    _l_(28442)


    def __init__(self):
        _l_(28326)

        _n_(28320, "self", lambda: self).head = None
        _l_(28321)
        _n_(28322, "self", lambda: self).tail = None
        _l_(28323)
        _n_(28324, "self", lambda: self).count = 0
        _l_(28325)

    def append_item(self, value):
        _l_(28350)

        new_item = _c_(28329, _n_(28327, "Node", lambda: Node), _n_(28328, "value", lambda: value), None, None)
        _l_(28330)
        if _a_(28332, _n_(28331, "self", lambda: self), "head") is None:
            _l_(28347)

            _n_(28333, "self", lambda: self).head = _n_(28334, "new_item", lambda: new_item)
            _l_(28335)
        else:
            _n_(28336, "new_item", lambda: new_item).prev = _a_(28338, _n_(28337, "self", lambda: self), "tail")
            _l_(28339)
            _a_(28341, _n_(28340, "self", lambda: self), "tail").next = _n_(28342, "new_item", lambda: new_item)
            _l_(28343)
            _n_(28344, "self", lambda: self).tail = _n_(28345, "new_item", lambda: new_item)
            _l_(28346)
        _n_(28348, "self", lambda: self).count += 1
        _l_(28349)

    def iter(self):
        _l_(28364)

        current = _a_(28352, _n_(28351, "self", lambda: self), "head")
        _l_(28353)
        while _n_(28354, "current", lambda: current):
            _l_(28363)

            item_val = _a_(28356, _n_(28355, "current", lambda: current), "value")
            _l_(28357)
            current = _a_(28359, _n_(28358, "current", lambda: current), "next")
            _l_(28360)
            yield _n_(28361, "item_val", lambda: item_val)
            _l_(28362)

    def print_foward(self):
        _l_(28373)

        for node in _c_(28367, _a_(28366, _n_(28365, "self", lambda: self), "iter")):
            _l_(28372)

            _c_(28370, _n_(28368, "print", lambda: print), _n_(28369, "node", lambda: node))
            _l_(28371)

    def search_item(self, val):
        _l_(28383)

        for node in _c_(28376, _a_(28375, _n_(28374, "self", lambda: self), "iter")):
            _l_(28381)

            if _n_(28377, "val", lambda: val) == _n_(28378, "node", lambda: node):
                _l_(28380)

                aux = True
                _l_(28379)
                return aux
        aux = False
        _l_(28382)
        return aux

    def delete(self, value):
        _l_(28441)

        current = _a_(28385, _n_(28384, "self", lambda: self), "head")
        _l_(28386)
        node_deleted = False
        _l_(28387)
        if _n_(28388, "current", lambda: current) is None:
            _l_(28436)

            node_deleted = False
            _l_(28389)
        elif _a_(28391, _n_(28390, "current", lambda: current), "value") == _n_(28392, "value", lambda: value):
            _l_(28435)

            _n_(28393, "self", lambda: self).head = _a_(28395, _n_(28394, "current", lambda: current), "next")
            _l_(28396)
            _a_(28398, _n_(28397, "self", lambda: self), "head").prev = None
            _l_(28399)
            node_deleted = True
            _l_(28400)
        elif _a_(28403, _a_(28402, _n_(28401, "self", lambda: self), "tail"), "value") == _n_(28404, "value", lambda: value):
            _l_(28434)

            _n_(28405, "self", lambda: self).tail = _a_(28408, _a_(28407, _n_(28406, "self", lambda: self), "tail"), "prev")
            _l_(28409)
            _a_(28411, _n_(28410, "self", lambda: self), "tail").next = None
            _l_(28412)
            node_deleted = True
            _l_(28413)
        else:
            while _n_(28414, "current", lambda: current):
                _l_(28433)

                if _a_(28416, _n_(28415, "current", lambda: current), "value") == _n_(28417, "value", lambda: value):
                    _l_(28429)

                    _a_(28419, _n_(28418, "current", lambda: current), "prev").next = _a_(28421, _n_(28420, "current", lambda: current), "next")
                    _l_(28422)
                    _a_(28424, _n_(28423, "current", lambda: current), "next").prev = _a_(28426, _n_(28425, "current", lambda: current), "prev")
                    _l_(28427)
                    node_deleted = True
                    _l_(28428)
                current = _a_(28431, _n_(28430, "current", lambda: current), "next")
                _l_(28432)
        if _n_(28437, "node_deleted", lambda: node_deleted):
            _l_(28440)

            _n_(28438, "self", lambda: self).count -= 1
            _l_(28439)
items = _c_(28444, _n_(28443, "doubly_linked_list", lambda: doubly_linked_list))
_l_(28445)
_c_(28448, _a_(28447, _n_(28446, "items", lambda: items), "append_item"), 'PHP')
_l_(28449)
_c_(28452, _a_(28451, _n_(28450, "items", lambda: items), "append_item"), 'Python')
_l_(28453)
_c_(28456, _a_(28455, _n_(28454, "items", lambda: items), "append_item"), 'C#')
_l_(28457)
_c_(28460, _a_(28459, _n_(28458, "items", lambda: items), "append_item"), 'C++')
_l_(28461)
_c_(28464, _a_(28463, _n_(28462, "items", lambda: items), "append_item"), 'Java')
_l_(28465)
_c_(28468, _a_(28467, _n_(28466, "items", lambda: items), "append_item"), 'SQL')
_l_(28469)
_c_(28471, _n_(28470, "print", lambda: print), 'Original list:')
_l_(28472)
_c_(28475, _a_(28474, _n_(28473, "items", lambda: items), "print_foward"))
_l_(28476)
_c_(28479, _a_(28478, _n_(28477, "items", lambda: items), "delete"), 'Java')
_l_(28480)
_c_(28483, _a_(28482, _n_(28481, "items", lambda: items), "delete"), 'Python')
_l_(28484)
_c_(28486, _n_(28485, "print", lambda: print), '\nList after deleting two items:')
_l_(28487)
_c_(28490, _a_(28489, _n_(28488, "items", lambda: items), "print_foward"))
_l_(28491)