# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70101457/attributeerror-linkedlist-object-has-no-attribute-head
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class LinkedList():
    _l_(357295)

    def __int__(self):
        _l_(357257)

        _n_(357255, "self", lambda: self).head = None
        _l_(357256)

    def insert(self, newNode):
        _l_(357278)

        if _a_(357259, _n_(357258, "self", lambda: self), "head") is None:
            _l_(357277)

            _n_(357260, "self", lambda: self).head = _n_(357261, "newNode", lambda: newNode)
            _l_(357262)
        else:
            #head =>john->Ben->Matthew->None
            lastNode = _a_(357264, _n_(357263, "self", lambda: self), "head")
            _l_(357265)
            while True:
                _l_(357273)

                if _a_(357267, _n_(357266, "lastNode", lambda: lastNode), "next") is None:
                    _l_(357269)

                    break
                    _l_(357268)
                lastNode = _a_(357271, _n_(357270, "lastNode", lambda: lastNode), "next")
                _l_(357272)
            _n_(357274, "lastNode", lambda: lastNode).next = _n_(357275, "newNode", lambda: newNode)
            _l_(357276)

    def printList(self):
        _l_(357294)

        #head=>john->Ben->Matthew->None
        currentNode = _a_(357280, _n_(357279, "self", lambda: self), "head")
        _l_(357281)
        while True:
            _l_(357290)

            if _n_(357282, "currentNode", lambda: currentNode) is None:
                _l_(357284)

                break
                _l_(357283)
            _c_(357288, _n_(357285, "print", lambda: print), _a_(357287, _n_(357286, "currentNode", lambda: currentNode), "data"))
            _l_(357289)
        currentNode = _a_(357292, _n_(357291, "currentNode", lambda: currentNode), "next")
        _l_(357293)

# node => data, next
#firstnode.data => data, firstnode.next => None
firstNode = _c_(357297, _n_(357296, "Node", lambda: Node), 'john')
_l_(357298)
linkedlist = _c_(357300, _n_(357299, "LinkedList", lambda: LinkedList))
_l_(357301)
_c_(357305, _a_(357303, _n_(357302, "linkedlist", lambda: linkedlist), "insert"), _n_(357304, "firstNode", lambda: firstNode))
_l_(357306)
secondNode = _c_(357308, _n_(357307, "Node", lambda: Node), 'Ben')
_l_(357309)
_c_(357313, _a_(357311, _n_(357310, "linkedlist", lambda: linkedlist), "insert"), _n_(357312, "secondNode", lambda: secondNode))
_l_(357314)
thridNode = _c_(357316, _n_(357315, "Node", lambda: Node), 'Matthew')
_l_(357317)
_a_(357319, _n_(357318, "linkedlist", lambda: linkedlist), "insert")
_l_(357320)
_c_(357323, _a_(357322, _n_(357321, "linkedlist", lambda: linkedlist), "printList"))
_l_(357324)