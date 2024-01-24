# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/77339705/attributeerror-linkedlist-object-has-no-attribute-insert-head
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class LinkedList:
    _l_(350838)

    def _init_(self):
        _l_(350837)

        # Empty LinkedList
        _n_(350833, "self", lambda: self).head = None
        _l_(350834)
        # no of nodes in the LinkedList
        _n_(350835, "self", lambda: self).n = 0
        _l_(350836)

class Node:
    _l_(350865)

    def __init__(self,value):
        _l_(350844)

        _n_(350839, "self", lambda: self).data = _n_(350840, "value", lambda: value)
        _l_(350841)
        _n_(350842, "self", lambda: self).next = None
        _l_(350843)

    def _len_(self):
        _l_(350848)

        aux = _a_(350846, _n_(350845, "self", lambda: self), "n")
        _l_(350847)
        return aux
    
    def insert_head(self,value):
        _l_(350864)

        #new node
        new_Node = _c_(350851, _n_(350849, "Node", lambda: Node), _n_(350850, "value", lambda: value))
        _l_(350852)

        #Create onnection
        _n_(350853, "new_Node", lambda: new_Node).next = _a_(350855, _n_(350854, "self", lambda: self), "head")
        _l_(350856)

        #Reasign head
        _n_(350857, "self", lambda: self).head = _n_(350858, "new_Node", lambda: new_Node)
        _l_(350859)

        #Increment n
        _n_(350860, "self", lambda: self).n = _a_(350862, _n_(350861, "self", lambda: self), "n") + 1
        _l_(350863)

L = _c_(350867, _n_(350866, "LinkedList", lambda: LinkedList))
_l_(350868)

_c_(350871, _a_(350870, _n_(350869, "L", lambda: L), "insert_head"), 1)
_l_(350872)

_c_(350875, _n_(350873, "len", lambda: len), _n_(350874, "L", lambda: L))
_l_(350876)