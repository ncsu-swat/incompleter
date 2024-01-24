# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/46656563/how-to-debug-typeerror-str-object-is-not-callable-python3-when-implementing-li
#!python

#from __future__ import print_function


from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node(_n_(691741, "object", lambda: object)):
    _l_(691756)


    def __init__(self, data):
        _l_(691747)

        """Initialize this node with the given data"""
        _n_(691742, "self", lambda: self).data = _n_(691743, "data", lambda: data)
        _l_(691744)
        _n_(691745, "self", lambda: self).next = None
        _l_(691746)

    def __repr__(self):
        _l_(691755)

        """Return a string representation of this node"""
        aux = _c_(691753, _a_(691748, 'Node({})', "format"), _c_(691752, _n_(691749, "repr", lambda: repr), _a_(691751, _n_(691750, "self", lambda: self), "data")))
        _l_(691754)
        return aux


class LinkedList(_n_(691757, "object", lambda: object)):
    _l_(691913)


    def __init__(self, iterable=None):
        _l_(691773)

        """Initialize this linked list; append the given items, if any"""
        _n_(691758, "self", lambda: self).head = None
        _l_(691759)
        _n_(691760, "self", lambda: self).tail = None
        _l_(691761)
        _n_(691762, "self", lambda: self).nodeCount = 0
        _l_(691763)
        if _n_(691764, "iterable", lambda: iterable):
            _l_(691772)

            for item in _n_(691765, "iterable", lambda: iterable):
                _l_(691771)

                _c_(691769, _a_(691767, _n_(691766, "self", lambda: self), "append"), _n_(691768, "item", lambda: item))
                _l_(691770)

    def __repr__(self):
        _l_(691782)

        """Return a string representation of this linked list"""
        aux = _c_(691780, _a_(691774, 'LinkedList({})', "format"), _c_(691779, _n_(691775, "repr", lambda: repr), _c_(691778, _a_(691777, _n_(691776, "self", lambda: self), "items"))))
        _l_(691781)
        return aux

    def items(self):
        _l_(691800)

        """Return a list of all items in this linked list"""
        result = []
        _l_(691783)
        current = _a_(691785, _n_(691784, "self", lambda: self), "head")
        _l_(691786)
        while _n_(691787, "current", lambda: current) is not None:
            _l_(691797)

            _c_(691792, _a_(691789, _n_(691788, "result", lambda: result), "append"), _a_(691791, _n_(691790, "current", lambda: current), "data"))
            _l_(691793)
            # result.append(current)
            current = _a_(691795, _n_(691794, "current", lambda: current), "next")
            _l_(691796)
        aux = _n_(691798, "result", lambda: result)
        _l_(691799)
        return aux

    def is_empty(self):
        _l_(691804)

        """Return True if this linked list is empty, or False"""
        aux = _a_(691802, _n_(691801, "self", lambda: self), "head") is None
        _l_(691803)
        return aux

    def length(self):
        _l_(691808)

        """Return the length of this linked list by traversing its nodes"""
        aux = _a_(691806, _n_(691805, "self", lambda: self), "nodeCount")
        _l_(691807)
        return aux

    def append(self, item):
        _l_(691845)

        """Insert the given item at the tail of this linked list"""
        new_node = _c_(691811, _n_(691809, "Node", lambda: Node), _n_(691810, "item", lambda: item))
        _l_(691812)
        _n_(691813, "self", lambda: self).nodeCount += 1
        _l_(691814)

        if _a_(691816, _n_(691815, "self", lambda: self), "tail") == None and _a_(691818, _n_(691817, "self", lambda: self), "head") == None:
            _l_(691844)

            _n_(691819, "self", lambda: self).tail = _n_(691820, "new_node", lambda: new_node)
            _l_(691821)
            _n_(691822, "self", lambda: self).head = _n_(691823, "new_node", lambda: new_node)
            _l_(691824)
        elif _a_(691826, _n_(691825, "self", lambda: self), "tail") == _a_(691828, _n_(691827, "self", lambda: self), "head"):
            _l_(691843)

            _n_(691829, "self", lambda: self).tail = _n_(691830, "new_node", lambda: new_node)
            _l_(691831)
            _a_(691833, _n_(691832, "self", lambda: self), "head").next = _n_(691834, "new_node", lambda: new_node)
            _l_(691835)
        else:
            _a_(691837, _n_(691836, "self", lambda: self), "tail").next = _n_(691838, "new_node", lambda: new_node)
            _l_(691839)
            _n_(691840, "self", lambda: self).tail = _n_(691841, "new_node", lambda: new_node)
            _l_(691842)

    def prepend(self, item):
        _l_(691881)

        """Insert the given item at the head of this linked list"""
        new_node = _c_(691848, _n_(691846, "Node", lambda: Node), _n_(691847, "item", lambda: item))
        _l_(691849)

        # if self.is_empty():
        #     self.tail = new_node
        #     self.head = new_node

        if _a_(691851, _n_(691850, "self", lambda: self), "head") == None and _a_(691853, _n_(691852, "self", lambda: self), "tail") == None:
            _l_(691880)

            _n_(691854, "self", lambda: self).tail = _n_(691855, "new_node", lambda: new_node)
            _l_(691856)
            _n_(691857, "self", lambda: self).head = _n_(691858, "new_node", lambda: new_node)
            _l_(691859)
        elif _a_(691861, _n_(691860, "self", lambda: self), "head") == _a_(691863, _n_(691862, "self", lambda: self), "tail"):
            _l_(691879)

            _n_(691864, "self", lambda: self).head = _n_(691865, "new_node", lambda: new_node)
            _l_(691866)
            _a_(691868, _n_(691867, "self", lambda: self), "head").next = _a_(691870, _n_(691869, "self", lambda: self), "tail")
            _l_(691871)
        else:
            _n_(691872, "new_node", lambda: new_node).next = _a_(691874, _n_(691873, "self", lambda: self), "head")
            _l_(691875)
            _n_(691876, "self", lambda: self).head = _n_(691877, "new_node", lambda: new_node)
            _l_(691878)

    def find(self, quality):
        _l_(691892)

        """Return an item from this linked list satisfying the given quality"""
        for item in _c_(691884, _a_(691883, _n_(691882, "self", lambda: self), "items")):
            _l_(691891)

            if _c_(691887, _n_(691885, "quality", lambda: quality), _n_(691886, "item", lambda: item)):
                _l_(691890)

                aux = _n_(691888, "item", lambda: item)
                _l_(691889)
                return aux

    def replace(self, quality, new_data):
        _l_(691912)

        """replace an item from this linked list satisfying the given quality"""
        current = _a_(691894, _n_(691893, "self", lambda: self), "head")
        _l_(691895)

        while _n_(691896, "current", lambda: current) is not None:
            _l_(691906)

            if _c_(691900, _n_(691897, "quality", lambda: quality), _a_(691899, _n_(691898, "current", lambda: current), "data")):
                _l_(691902)

                aux = ""
                _l_(691901)
                return aux
            current = _a_(691904, _n_(691903, "current", lambda: current), "next")
            _l_(691905)
        _c_(691910, _a_(691908, _n_(691907, "self", lambda: self), "append"), _n_(691909, "new_data", lambda: new_data))
        _l_(691911)

def test_linked_list():
    _l_(692030)

    ll = _c_(691915, _n_(691914, "LinkedList", lambda: LinkedList))
    _l_(691916)
    _c_(691919, _n_(691917, "print", lambda: print), _n_(691918, "ll", lambda: ll))
    _l_(691920)
    _c_(691923, _a_(691922, _n_(691921, "ll", lambda: ll), "append"), 'A')
    _l_(691924)
    _c_(691927, _n_(691925, "print", lambda: print), _n_(691926, "ll", lambda: ll))
    _l_(691928)
    _c_(691931, _a_(691930, _n_(691929, "ll", lambda: ll), "append"), 'B')
    _l_(691932)
    _c_(691935, _n_(691933, "print", lambda: print), _n_(691934, "ll", lambda: ll))
    _l_(691936)
    _c_(691939, _a_(691938, _n_(691937, "ll", lambda: ll), "append"), 'C')
    _l_(691940)
    _c_(691943, _n_(691941, "print", lambda: print), _n_(691942, "ll", lambda: ll))
    _l_(691944)
    _c_(691950, _n_(691945, "print", lambda: print), 'head: ' + _c_(691949, _n_(691946, "str", lambda: str), _a_(691948, _n_(691947, "ll", lambda: ll), "head")))
    _l_(691951)
    _c_(691957, _n_(691952, "print", lambda: print), 'tail: ' + _c_(691956, _n_(691953, "str", lambda: str), _a_(691955, _n_(691954, "ll", lambda: ll), "tail")))
    _l_(691958)
    _c_(691965, _n_(691959, "print", lambda: print), 'length: ' + _c_(691964, _n_(691960, "str", lambda: str), _c_(691963, _a_(691962, _n_(691961, "ll", lambda: ll), "length"))))
    _l_(691966)
    _c_(691971, _n_(691967, "print", lambda: print), _c_(691970, _a_(691969, _n_(691968, "ll", lambda: ll), "length")))
    _l_(691972)
    try:
        import pdb; 
        _l_(691977)

    except ImportError:
        pass

    _c_(691980, _a_(691979, _n_(691978, "ll", lambda: ll), "delete"), 'A')
    _l_(691981)
    _c_(691984, _n_(691982, "print", lambda: print), _n_(691983, "ll", lambda: ll))
    _l_(691985)
    _c_(691988, _a_(691987, _n_(691986, "ll", lambda: ll), "delete"), 'C')
    _l_(691989)
    _c_(691992, _n_(691990, "print", lambda: print), _n_(691991, "ll", lambda: ll))
    _l_(691993)
    _c_(691996, _a_(691995, _n_(691994, "ll", lambda: ll), "delete"), 'B')
    _l_(691997)
    _c_(692000, _n_(691998, "print", lambda: print), _n_(691999, "ll", lambda: ll))
    _l_(692001)
    _c_(692007, _n_(692002, "print", lambda: print), 'head: ' + _c_(692006, _n_(692003, "str", lambda: str), _a_(692005, _n_(692004, "ll", lambda: ll), "head")))
    _l_(692008)
    _c_(692014, _n_(692009, "print", lambda: print), 'tail: ' + _c_(692013, _n_(692010, "str", lambda: str), _a_(692012, _n_(692011, "ll", lambda: ll), "tail")))
    _l_(692015)
    _c_(692022, _n_(692016, "print", lambda: print), 'length: ' + _c_(692021, _n_(692017, "str", lambda: str), _c_(692020, _a_(692019, _n_(692018, "ll", lambda: ll), "length"))))
    _l_(692023)
    _c_(692028, _n_(692024, "print", lambda: print), _c_(692027, _a_(692026, _n_(692025, "ll", lambda: ll), "length")))
    _l_(692029)


if _n_(692031, "__name__", lambda: __name__) == '__main__':
    _l_(692035)

    _c_(692033, _n_(692032, "test_linked_list", lambda: test_linked_list))
    _l_(692034)