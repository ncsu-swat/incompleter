# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/77479079/linked-list-typeerror-str-returned-non-string-type-nonetype
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node:
    _l_(619163)

    def __init__(self, data, next=None):
        _l_(619162)

        _n_(619156, "self", lambda: self).data = _n_(619157, "data", lambda: data)
        _l_(619158)
        _n_(619159, "self", lambda: self).next = _n_(619160, "next", lambda: next)
        _l_(619161)

class LinkedList:
    _l_(619271)

    def __init__(self):
        _l_(619166)

        _n_(619164, "self", lambda: self).head = None
        _l_(619165)

    def __str__(self):
        _l_(619180)

        node = _a_(619168, _n_(619167, "self", lambda: self), "head")
        _l_(619169)
        while _n_(619170, "node", lambda: node) is not None:
            _l_(619179)

            _c_(619174, _n_(619171, "print", lambda: print), _a_(619173, _n_(619172, "node", lambda: node), "data"))
            _l_(619175)
            node = _a_(619177, _n_(619176, "node", lambda: node), "next")
            _l_(619178)

    def append(self, data):
        _l_(619204)

        if not _a_(619182, _n_(619181, "self", lambda: self), "head"):
            _l_(619189)

            _n_(619183, "self", lambda: self).head = _c_(619186, _n_(619184, "Node", lambda: Node), _n_(619185, "data", lambda: data))
            _l_(619187)
            aux = ""
            _l_(619188)
            return aux
        current = _a_(619191, _n_(619190, "self", lambda: self), "head")
        _l_(619192)
        while _a_(619194, _n_(619193, "current", lambda: current), "next"):
            _l_(619198)

            current = _a_(619196, _n_(619195, "current", lambda: current), "next")
            _l_(619197)
        _n_(619199, "current", lambda: current).next = _c_(619202, _n_(619200, "Node", lambda: Node), _n_(619201, "data", lambda: data))
        _l_(619203)

    def search(self, target):
        _l_(619220)

        current = _a_(619206, _n_(619205, "self", lambda: self), "head")
        _l_(619207)
        while _a_(619209, _n_(619208, "current", lambda: current), "next"):
            _l_(619218)

            if _a_(619211, _n_(619210, "current", lambda: current), "data") == _n_(619212, "target", lambda: target):
                _l_(619217)

                aux = True
                _l_(619213)
                return aux
            else:
                current = _a_(619215, _n_(619214, "current", lambda: current), "next")
                _l_(619216)
        aux = False
        _l_(619219)
        return aux

    def remove(self, target):
        _l_(619250)

        if _a_(619222, _n_(619221, "self", lambda: self), "head") == _n_(619223, "target", lambda: target):
            _l_(619230)

            _n_(619224, "self", lambda: self).head = _a_(619227, _a_(619226, _n_(619225, "self", lambda: self), "head"), "next")
            _l_(619228)
            aux = ""
            _l_(619229)
            return aux
        current = _a_(619232, _n_(619231, "self", lambda: self), "head")
        _l_(619233)
        previous = None
        _l_(619234)
        while _n_(619235, "current", lambda: current):
            _l_(619249)

            if _a_(619237, _n_(619236, "current", lambda: current), "data") == _n_(619238, "target", lambda: target):
                _l_(619243)

                _n_(619239, "previous", lambda: previous).next = _a_(619241, _n_(619240, "current", lambda: current), "next")
                _l_(619242)
            previous = _n_(619244, "current", lambda: current)
            _l_(619245)
            current = _a_(619247, _n_(619246, "current", lambda: current), "next")
            _l_(619248)

    def reverse_list(self):
        _l_(619270)

        current = _a_(619252, _n_(619251, "self", lambda: self), "head")
        _l_(619253)
        previous = None
        _l_(619254)
        while _n_(619255, "current", lambda: current):
            _l_(619266)

            next = _a_(619257, _n_(619256, "current", lambda: current), "next")
            _l_(619258)
            _n_(619259, "current", lambda: current).next = _n_(619260, "previous", lambda: previous)
            _l_(619261)
            previous = _n_(619262, "current", lambda: current)
            _l_(619263)
            current = _n_(619264, "next", lambda: next)
            _l_(619265)
        _n_(619267, "self", lambda: self).head = _n_(619268, "previous", lambda: previous)
        _l_(619269)

a_list = _c_(619273, _n_(619272, "LinkedList", lambda: LinkedList))
_l_(619274)
_c_(619277, _a_(619276, _n_(619275, "a_list", lambda: a_list), "append"), "Tuesday")
_l_(619278)
_c_(619281, _a_(619280, _n_(619279, "a_list", lambda: a_list), "append"), "Wednesday")
_l_(619282)
_c_(619285, _n_(619283, "print", lambda: print), _n_(619284, "a_list", lambda: a_list))
_l_(619286)
try:
    import random
    _l_(619288)

except ImportError:
    pass

a_list = _c_(619290, _n_(619289, "LinkedList", lambda: LinkedList))
_l_(619291)

for i in _c_(619293, _n_(619292, "range", lambda: range), 0, 20):
    _l_(619307)

    j = _c_(619296, _a_(619295, _n_(619294, "random", lambda: random), "randint"), 1, 30)
    _l_(619297)
    _c_(619301, _a_(619299, _n_(619298, "a_list", lambda: a_list), "search"), _n_(619300, "j", lambda: j))
    _l_(619302)
    _c_(619305, _n_(619303, "print", lambda: print), _n_(619304, "j", lambda: j), end=' ')
    _l_(619306)