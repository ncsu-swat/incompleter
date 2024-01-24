# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70101457/attributeerror-linkedlist-object-has-no-attribute-head
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class LinkedList():
    _l_(344878)

    def __int__(self):
        _l_(344840)

        _n_(344838, "self", lambda: self).head = None
        _l_(344839)

    def insert(self, newNode):
        _l_(344861)

        if _a_(344842, _n_(344841, "self", lambda: self), "head") is None:
            _l_(344860)

            _n_(344843, "self", lambda: self).head = _n_(344844, "newNode", lambda: newNode)
            _l_(344845)
        else:
            #head =>john->Ben->Matthew->None
            lastNode = _a_(344847, _n_(344846, "self", lambda: self), "head")
            _l_(344848)
            while True:
                _l_(344856)

                if _a_(344850, _n_(344849, "lastNode", lambda: lastNode), "next") is None:
                    _l_(344852)

                    break
                    _l_(344851)
                lastNode = _a_(344854, _n_(344853, "lastNode", lambda: lastNode), "next")
                _l_(344855)
            _n_(344857, "lastNode", lambda: lastNode).next = _n_(344858, "newNode", lambda: newNode)
            _l_(344859)

    def printList(self):
        _l_(344877)

        #head=>john->Ben->Matthew->None
        currentNode = _a_(344863, _n_(344862, "self", lambda: self), "head")
        _l_(344864)
        while True:
            _l_(344873)

            if _n_(344865, "currentNode", lambda: currentNode) is None:
                _l_(344867)

                break
                _l_(344866)
            _c_(344871, _n_(344868, "print", lambda: print), _a_(344870, _n_(344869, "currentNode", lambda: currentNode), "data"))
            _l_(344872)
        currentNode = _a_(344875, _n_(344874, "currentNode", lambda: currentNode), "next")
        _l_(344876)

# node => data, next
#firstnode.data => data, firstnode.next => None
firstNode = _c_(344880, _n_(344879, "Node", lambda: Node), 'john')
_l_(344881)
linkedlist = _c_(344883, _n_(344882, "LinkedList", lambda: LinkedList))
_l_(344884)
_c_(344888, _a_(344886, _n_(344885, "linkedlist", lambda: linkedlist), "insert"), _n_(344887, "firstNode", lambda: firstNode))
_l_(344889)
secondNode = _c_(344891, _n_(344890, "Node", lambda: Node), 'Ben')
_l_(344892)
_c_(344896, _a_(344894, _n_(344893, "linkedlist", lambda: linkedlist), "insert"), _n_(344895, "secondNode", lambda: secondNode))
_l_(344897)
thridNode = _c_(344899, _n_(344898, "Node", lambda: Node), 'Matthew')
_l_(344900)
_a_(344902, _n_(344901, "linkedlist", lambda: linkedlist), "insert")
_l_(344903)
_c_(344906, _a_(344905, _n_(344904, "linkedlist", lambda: linkedlist), "printList"))
_l_(344907)