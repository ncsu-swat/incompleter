# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70101457/attributeerror-linkedlist-object-has-no-attribute-head
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class LinkedList():
    _l_(363769)

    def __int__(self):
        _l_(363731)

        _n_(363729, "self", lambda: self).head = None
        _l_(363730)

    def insert(self, newNode):
        _l_(363752)

        if _a_(363733, _n_(363732, "self", lambda: self), "head") is None:
            _l_(363751)

            _n_(363734, "self", lambda: self).head = _n_(363735, "newNode", lambda: newNode)
            _l_(363736)
        else:
            #head =>john->Ben->Matthew->None
            lastNode = _a_(363738, _n_(363737, "self", lambda: self), "head")
            _l_(363739)
            while True:
                _l_(363747)

                if _a_(363741, _n_(363740, "lastNode", lambda: lastNode), "next") is None:
                    _l_(363743)

                    break
                    _l_(363742)
                lastNode = _a_(363745, _n_(363744, "lastNode", lambda: lastNode), "next")
                _l_(363746)
            _n_(363748, "lastNode", lambda: lastNode).next = _n_(363749, "newNode", lambda: newNode)
            _l_(363750)

    def printList(self):
        _l_(363768)

        #head=>john->Ben->Matthew->None
        currentNode = _a_(363754, _n_(363753, "self", lambda: self), "head")
        _l_(363755)
        while True:
            _l_(363764)

            if _n_(363756, "currentNode", lambda: currentNode) is None:
                _l_(363758)

                break
                _l_(363757)
            _c_(363762, _n_(363759, "print", lambda: print), _a_(363761, _n_(363760, "currentNode", lambda: currentNode), "data"))
            _l_(363763)
        currentNode = _a_(363766, _n_(363765, "currentNode", lambda: currentNode), "next")
        _l_(363767)

# node => data, next
#firstnode.data => data, firstnode.next => None
firstNode = _c_(363771, _n_(363770, "Node", lambda: Node), 'john')
_l_(363772)
linkedlist = _c_(363774, _n_(363773, "LinkedList", lambda: LinkedList))
_l_(363775)
_c_(363779, _a_(363777, _n_(363776, "linkedlist", lambda: linkedlist), "insert"), _n_(363778, "firstNode", lambda: firstNode))
_l_(363780)
secondNode = _c_(363782, _n_(363781, "Node", lambda: Node), 'Ben')
_l_(363783)
_c_(363787, _a_(363785, _n_(363784, "linkedlist", lambda: linkedlist), "insert"), _n_(363786, "secondNode", lambda: secondNode))
_l_(363788)
thridNode = _c_(363790, _n_(363789, "Node", lambda: Node), 'Matthew')
_l_(363791)
_a_(363793, _n_(363792, "linkedlist", lambda: linkedlist), "insert")
_l_(363794)
_c_(363797, _a_(363796, _n_(363795, "linkedlist", lambda: linkedlist), "printList"))
_l_(363798)