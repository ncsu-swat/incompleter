# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/46656563/how-to-debug-typeerror-str-object-is-not-callable-python3-when-implementing-li
#!python

#from __future__ import print_function


from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node(_n_(661231, "object", lambda: object)):
    _l_(661248)


    def __init__(self, data):
        _l_(661239)

        """Initialize this node with the given data"""
        _n_(661232, "self", lambda: self).data = _n_(661233, "data", lambda: data)
        _l_(661234)
        _n_(661235, "self", lambda: self).next = None
        _l_(661236)
        _n_(661237, "self", lambda: self).previous = None
        _l_(661238)

    def __repr__(self):
        _l_(661247)

        """Return a string representation of this node"""
        aux = _c_(661245, _a_(661240, 'Node({})', "format"), _c_(661244, _n_(661241, "repr", lambda: repr), _a_(661243, _n_(661242, "self", lambda: self), "data")))
        _l_(661246)
        return aux


class LinkedList(_n_(661249, "object", lambda: object)):
    _l_(661487)


    def __init__(self, iterable=None):
        _l_(661265)

        """Initialize this linked list; append the given items, if any"""
        _n_(661250, "self", lambda: self).head = None
        _l_(661251)
        _n_(661252, "self", lambda: self).tail = None
        _l_(661253)
        _n_(661254, "self", lambda: self).nodeCount = 0
        _l_(661255)
        if _n_(661256, "iterable", lambda: iterable):
            _l_(661264)

            for item in _n_(661257, "iterable", lambda: iterable):
                _l_(661263)

                _c_(661261, _a_(661259, _n_(661258, "self", lambda: self), "append"), _n_(661260, "item", lambda: item))
                _l_(661262)

    def __repr__(self):
        _l_(661274)

        """Return a string representation of this linked list"""
        aux = _c_(661272, _a_(661266, 'LinkedList({})', "format"), _c_(661271, _n_(661267, "repr", lambda: repr), _c_(661270, _a_(661269, _n_(661268, "self", lambda: self), "items"))))
        _l_(661273)
        return aux

    def items(self):
        _l_(661292)

        """Return a list of all items in this linked list"""
        result = []
        _l_(661275)
        current = _a_(661277, _n_(661276, "self", lambda: self), "head")
        _l_(661278)
        while _n_(661279, "current", lambda: current) is not None:
            _l_(661289)

            _c_(661284, _a_(661281, _n_(661280, "result", lambda: result), "append"), _a_(661283, _n_(661282, "current", lambda: current), "data"))
            _l_(661285)
            # result.append(current)
            current = _a_(661287, _n_(661286, "current", lambda: current), "next")
            _l_(661288)
        aux = _n_(661290, "result", lambda: result)
        _l_(661291)
        return aux

    def is_empty(self):
        _l_(661296)

        """Return True if this linked list is empty, or False"""
        aux = _a_(661294, _n_(661293, "self", lambda: self), "head") is None
        _l_(661295)
        return aux

    def length(self):
        _l_(661300)

        """Return the length of this linked list by traversing its nodes"""
        aux = _a_(661298, _n_(661297, "self", lambda: self), "nodeCount")
        _l_(661299)
        return aux

    def append(self, item):
        _l_(661337)

        """Insert the given item at the tail of this linked list"""
        new_node = _c_(661303, _n_(661301, "Node", lambda: Node), _n_(661302, "item", lambda: item))
        _l_(661304)
        _n_(661305, "self", lambda: self).nodeCount += 1
        _l_(661306)

        if _a_(661308, _n_(661307, "self", lambda: self), "tail") == None and _a_(661310, _n_(661309, "self", lambda: self), "head") == None:
            _l_(661336)

            _n_(661311, "self", lambda: self).tail = _n_(661312, "new_node", lambda: new_node)
            _l_(661313)
            _n_(661314, "self", lambda: self).head = _n_(661315, "new_node", lambda: new_node)
            _l_(661316)
        elif _a_(661318, _n_(661317, "self", lambda: self), "tail") == _a_(661320, _n_(661319, "self", lambda: self), "head"):
            _l_(661335)

            _n_(661321, "self", lambda: self).tail = _n_(661322, "new_node", lambda: new_node)
            _l_(661323)
            _a_(661325, _n_(661324, "self", lambda: self), "head").next = _n_(661326, "new_node", lambda: new_node)
            _l_(661327)
        else:
            _a_(661329, _n_(661328, "self", lambda: self), "tail").next = _n_(661330, "new_node", lambda: new_node)
            _l_(661331)
            _n_(661332, "self", lambda: self).tail = _n_(661333, "new_node", lambda: new_node)
            _l_(661334)

    def prepend(self, item):
        _l_(661373)

        """Insert the given item at the head of this linked list"""
        new_node = _c_(661340, _n_(661338, "Node", lambda: Node), _n_(661339, "item", lambda: item))
        _l_(661341)

        # if self.is_empty():
        #     self.tail = new_node
        #     self.head = new_node

        if _a_(661343, _n_(661342, "self", lambda: self), "head") == None and _a_(661345, _n_(661344, "self", lambda: self), "tail") == None:
            _l_(661372)

            _n_(661346, "self", lambda: self).tail = _n_(661347, "new_node", lambda: new_node)
            _l_(661348)
            _n_(661349, "self", lambda: self).head = _n_(661350, "new_node", lambda: new_node)
            _l_(661351)
        elif _a_(661353, _n_(661352, "self", lambda: self), "head") == _a_(661355, _n_(661354, "self", lambda: self), "tail"):
            _l_(661371)

            _n_(661356, "self", lambda: self).head = _n_(661357, "new_node", lambda: new_node)
            _l_(661358)
            _a_(661360, _n_(661359, "self", lambda: self), "head").next = _a_(661362, _n_(661361, "self", lambda: self), "tail")
            _l_(661363)
        else:
            _n_(661364, "new_node", lambda: new_node).next = _a_(661366, _n_(661365, "self", lambda: self), "head")
            _l_(661367)
            _n_(661368, "self", lambda: self).head = _n_(661369, "new_node", lambda: new_node)
            _l_(661370)

    def delete(self, item):
        _l_(661431)

        """Delete the given item from this linked list, or raise ValueError"""
        current = _a_(661375, _n_(661374, "self", lambda: self), "head")
        _l_(661376)
        previous = None
        _l_(661377)
        while _n_(661378, "current", lambda: current) is not None:
            _l_(661424)

            if _a_(661380, _n_(661379, "current", lambda: current), "data") == _n_(661381, "item", lambda: item):
                _l_(661418)

                if _n_(661382, "current", lambda: current) is not _a_(661384, _n_(661383, "self", lambda: self), "head") and _n_(661385, "current", lambda: current) is not _a_(661387, _n_(661386, "self", lambda: self), "tail"):
                    _l_(661395)

                    _n_(661388, "previous", lambda: previous).next = _a_(661390, _n_(661389, "current", lambda: current), "next")
                    _l_(661391)
                    _n_(661392, "current", lambda: current).next = None
                    _l_(661393)
                    break
                    _l_(661394)
                if _n_(661396, "current", lambda: current) is _a_(661398, _n_(661397, "self", lambda: self), "head"):
                    _l_(661405)

                    _n_(661399, "self", lambda: self).head = _a_(661401, _n_(661400, "current", lambda: current), "next")
                    _l_(661402)
                    _n_(661403, "current", lambda: current).next = None
                    _l_(661404)
                if _n_(661406, "current", lambda: current) is _a_(661408, _n_(661407, "self", lambda: self), "tail"):
                    _l_(661416)

                    if _n_(661409, "previous", lambda: previous) is not None:
                        _l_(661412)

                        _n_(661410, "previous", lambda: previous).next = None
                        _l_(661411)
                    _n_(661413, "self", lambda: self).tail = _n_(661414, "previous", lambda: previous)
                    _l_(661415)
                aux = ""
                _l_(661417)
                return aux
            previous = _n_(661419, "current", lambda: current)
            _l_(661420)
            current = _a_(661422, _n_(661421, "current", lambda: current), "next")
            _l_(661423)
        raise _c_(661429, _n_(661425, "ValueError", lambda: ValueError), _c_(661428, _a_(661426, 'Item not found: {}', "format"), _n_(661427, "item", lambda: item)))
        _l_(661430)


    def find(self, quality):
        _l_(661442)

        """Return an item from this linked list satisfying the given quality"""
        for item in _c_(661434, _a_(661433, _n_(661432, "self", lambda: self), "items")):
            _l_(661441)

            if _c_(661437, _n_(661435, "quality", lambda: quality), _n_(661436, "item", lambda: item)):
                _l_(661440)

                aux = _n_(661438, "item", lambda: item)
                _l_(661439)
                return aux

    def replace(self, quality, new_data):
        _l_(661462)

        """replace an item from this linked list satisfying the given quality"""
        current = _a_(661444, _n_(661443, "self", lambda: self), "head")
        _l_(661445)

        while _n_(661446, "current", lambda: current) is not None:
            _l_(661456)

            if _c_(661450, _n_(661447, "quality", lambda: quality), _a_(661449, _n_(661448, "current", lambda: current), "data")):
                _l_(661452)

                aux = ""
                _l_(661451)
                return aux
            current = _a_(661454, _n_(661453, "current", lambda: current), "next")
            _l_(661455)
        _c_(661460, _a_(661458, _n_(661457, "self", lambda: self), "append"), _n_(661459, "new_data", lambda: new_data))
        _l_(661461)


    def replace(self, item, new_item):
        _l_(661471)

        """replace an item with new_item by using the helper function finding the item"""
        node = _c_(661466, _a_(661464, _n_(661463, "self", lambda: self), "find_node"), _n_(661465, "item", lambda: item))
        _l_(661467)
        _n_(661468, "node", lambda: node).data = _n_(661469, "new_item", lambda: new_item)
        _l_(661470)

    def find_node(self, item):
        _l_(661486)

        """Returns the first node it encounters where data is equal to item"""
        current_node = _a_(661473, _n_(661472, "self", lambda: self), "head")
        _l_(661474)
        while _n_(661475, "current_node", lambda: current_node) is not None:
            _l_(661485)

            if _a_(661477, _n_(661476, "current_node", lambda: current_node), "data") == _n_(661478, "item", lambda: item):
                _l_(661481)

                aux = _n_(661479, "current_node", lambda: current_node)
                _l_(661480)
                return aux
            current_node = _a_(661483, _n_(661482, "current_node", lambda: current_node), "next")
            _l_(661484)

def test_linked_list():
    _l_(661631)

    ll = _c_(661489, _n_(661488, "LinkedList", lambda: LinkedList))
    _l_(661490)
    _c_(661493, _n_(661491, "print", lambda: print), _n_(661492, "ll", lambda: ll))
    _l_(661494)
    _c_(661497, _a_(661496, _n_(661495, "ll", lambda: ll), "append"), 'A')
    _l_(661498)
    _c_(661501, _n_(661499, "print", lambda: print), _n_(661500, "ll", lambda: ll))
    _l_(661502)
    _c_(661505, _a_(661504, _n_(661503, "ll", lambda: ll), "append"), 'B')
    _l_(661506)
    _c_(661509, _n_(661507, "print", lambda: print), _n_(661508, "ll", lambda: ll))
    _l_(661510)
    _c_(661513, _a_(661512, _n_(661511, "ll", lambda: ll), "append"), 'C')
    _l_(661514)
    _c_(661517, _n_(661515, "print", lambda: print), _n_(661516, "ll", lambda: ll))
    _l_(661518)
    _c_(661524, _n_(661519, "print", lambda: print), 'head: ' + _c_(661523, _n_(661520, "str", lambda: str), _a_(661522, _n_(661521, "ll", lambda: ll), "head")))
    _l_(661525)
    _c_(661531, _n_(661526, "print", lambda: print), 'tail: ' + _c_(661530, _n_(661527, "str", lambda: str), _a_(661529, _n_(661528, "ll", lambda: ll), "tail")))
    _l_(661532)
    _c_(661537, _n_(661533, "print", lambda: print), _c_(661536, _a_(661535, _n_(661534, "ll", lambda: ll), "length")))
    _l_(661538)

    # import pdb; pdb.set_trace()
    _c_(661541, _a_(661540, _n_(661539, "ll", lambda: ll), "delete"), 'A')
    _l_(661542)
    _c_(661545, _n_(661543, "print", lambda: print), _n_(661544, "ll", lambda: ll))
    _l_(661546)
    _c_(661549, _a_(661548, _n_(661547, "ll", lambda: ll), "delete"), 'C')
    _l_(661550)
    _c_(661553, _n_(661551, "print", lambda: print), _n_(661552, "ll", lambda: ll))
    _l_(661554)
    _c_(661557, _a_(661556, _n_(661555, "ll", lambda: ll), "delete"), 'B')
    _l_(661558)
    _c_(661561, _n_(661559, "print", lambda: print), _n_(661560, "ll", lambda: ll))
    _l_(661562)
    _c_(661568, _n_(661563, "print", lambda: print), 'head: ' + _c_(661567, _n_(661564, "str", lambda: str), _a_(661566, _n_(661565, "ll", lambda: ll), "head")))
    _l_(661569)
    _c_(661575, _n_(661570, "print", lambda: print), 'tail: ' + _c_(661574, _n_(661571, "str", lambda: str), _a_(661573, _n_(661572, "ll", lambda: ll), "tail")))
    _l_(661576)
    _c_(661581, _n_(661577, "print", lambda: print), _c_(661580, _a_(661579, _n_(661578, "ll", lambda: ll), "length")))
    _l_(661582)

    _c_(661585, _a_(661584, _n_(661583, "ll", lambda: ll), "append"), 'A')
    _l_(661586)
    _c_(661589, _n_(661587, "print", lambda: print), _n_(661588, "ll", lambda: ll))
    _l_(661590)
    _c_(661593, _a_(661592, _n_(661591, "ll", lambda: ll), "append"), 'B')
    _l_(661594)
    _c_(661597, _n_(661595, "print", lambda: print), _n_(661596, "ll", lambda: ll))
    _l_(661598)
    _c_(661601, _a_(661600, _n_(661599, "ll", lambda: ll), "append"), 'C')
    _l_(661602)
    _c_(661605, _n_(661603, "print", lambda: print), _n_(661604, "ll", lambda: ll))
    _l_(661606)
    try:
        import pdb; 
        _l_(661611)

    except ImportError:
        pass

    _c_(661614, _a_(661613, _n_(661612, "ll", lambda: ll), "find_node"), 'A')
    _l_(661615)
    _c_(661617, _n_(661616, "print", lambda: print), "___________________")
    _l_(661618)
    _c_(661621, _a_(661620, _n_(661619, "ll", lambda: ll), "replace"), 'B', 'A')
    _l_(661622)
    _c_(661625, _a_(661624, _n_(661623, "ll", lambda: ll), "replace"), 'A', 'M')
    _l_(661626)
    _c_(661629, _n_(661627, "print", lambda: print), _n_(661628, "ll", lambda: ll))
    _l_(661630)

if _n_(661632, "__name__", lambda: __name__) == '__main__':
    _l_(661636)

    _c_(661634, _n_(661633, "test_linked_list", lambda: test_linked_list))
    _l_(661635)